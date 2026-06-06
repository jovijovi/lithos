#!/usr/bin/env python3
"""Conformance verification for Lithos adoption manifests.

Pure-stdlib checker (no third-party JSON Schema library). It parses the
adoption-manifest schema, the published template, and every fixture under
``fixtures/conformance/`` and asserts the governance invariants documented in
``docs/conformance-and-fixtures.md``.

Fixture naming is the contract:

* the template and any fixture named ``valid-*.json`` must satisfy every
  invariant;
* any fixture named ``invalid-*.json`` must violate at least one invariant, and
  where an intended reason is registered the failure must cite that reason
  (e.g. ``invalid-autonomous-self-merge.json`` must fail on ``agent_self_merge``,
  ``invalid-autonomous-self-approval.json`` on ``agent_self_approval``,
  ``invalid-live-runtime-without-controls.json`` on ``live_runtime``, and
  ``invalid-workflow-path-traversal.json`` on ``path traversal``).

Beyond the governance flags, the checker enforces that an arbitrary manifest
carries only portable, non-sensitive values:

* ``local_workflow_file`` must be a single, portable, repo-relative path — never
  an absolute, home/private machine-local, URL-like, path-traversal, or
  empty-segment path. A standalone checker cannot know an adopting repository's
  root, so it verifies the *shape* of the path, not the physical presence of the
  file; presence is the adopting project's local verifier and root workflow.
* no string value anywhere in the manifest may be secret-shaped or a private
  machine-local absolute path; the whole document is scanned recursively.

To stay honest, the checker self-tests on startup: it mutates a known-good
manifest in memory and confirms each invalid case fails for its intended reason.
Sensitive probes are assembled at runtime from fragments, so no secret-shaped or
private literal is ever stored in this file (mirroring
``scripts/verify_static_safety.py``).

A manifest declares conformance; it never authorizes anything. These checks
verify the declaration is internally consistent with the governance model.
"""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas/lithos-adoption-manifest.schema.json"
TEMPLATE_PATH = ROOT / "templates/lithos-adoption-manifest.json"
FIXTURES_DIR = ROOT / "fixtures/conformance"

# Lithos defines exactly one governance model. There are no adoption tiers; a
# small project keeps the model's anchors concise but never omits them. The
# manifest declares this single model by an exact value.
GOVERNANCE_MODEL = "full-lifecycle-governance"

# The adoption-manifest format version this checker validates. The schema types
# manifest_version only as a string, but every fixture and the template carry
# "1.0" and this checker understands exactly that format, so it enforces the
# exact value rather than merely a non-empty string. When the manifest format
# itself is revised, this constant and the fixtures/template move together.
MANIFEST_FORMAT_VERSION = "1.0"

REQUIRED_TOP_LEVEL = [
    "manifest_version",
    "lithos_version",
    "governance_model",
    "conformance_claim",
    "local_workflow_file",
    "roles",
    "approval_gates",
    "approval_authority",
    "verification",
    "autonomous_pr_policy",
    "knowledge_governance",
]

REQUIRED_ROLES = [
    "owner",
    "controller",
    "architect",
    "implementation_agent",
    "reviewer",
    "verifier",
]

REQUIRED_GATES = [
    "preparation",
    "implementation",
    "destructive_external",
    "live_runtime",
]

# Gates whose owner approval can never be waived.
OWNER_APPROVAL_GATES = ["implementation", "destructive_external"]

# Autonomous-PR actions Lithos adoption never licenses: each must be false.
FORBIDDEN_PR_ACTIONS = [
    "agent_self_approval",
    "agent_self_merge",
    "ownerless_auto_merge",
    "ownerless_branch_deletion",
    "ownerless_release_or_publish",
    "live_or_runtime_default_on",
]

# Actions that must remain behind explicit owner approval.
REQUIRED_PR_APPROVALS = [
    "merge",
    "branch-deletion",
    "release-or-publish",
    "live-runtime",
    "external-destructive",
]

REQUIRED_KNOWLEDGE_GOVERNANCE = [
    "dev_log",
    "lessons",
    "practices",
    "generated_index",
    "drift_report",
    "evidence_retention",
    "stale_knowledge_handling",
]

# For invalid fixtures, the substring the failure reason must contain so the
# fixture demonstrably fails for the reason it is named for.
INVALID_REASON_MARKERS = {
    "invalid-autonomous-self-merge.json": "agent_self_merge",
    "invalid-autonomous-self-approval.json": "agent_self_approval",
    "invalid-live-runtime-without-controls.json": "live_runtime",
    "invalid-live-runtime-non-object.json": "approval_gates.live_runtime",
    "invalid-workflow-path-traversal.json": "path traversal",
    "invalid-conformance-claim-false.json": "conformance_claim.claims_conformance",
}

# Secret/token shapes used to keep an arbitrary manifest free of sensitive
# values. Each needle is assembled from fragments so this file never contains a
# value that matches one of its own patterns (mirrors
# scripts/verify_static_safety.py).
SECRET_PATTERNS = [
    re.compile("gh" + "p_[A-Za-z0-9]{20,}"),
    re.compile("github" + "_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"(?<![A-Za-z0-9])" + "sk-" + r"[A-Za-z0-9-]{20,}"),
    re.compile("AK" + "IA[A-Z0-9]{16}"),
    re.compile("xox" + r"[abprs]-[A-Za-z0-9-]{10,}"),
    re.compile("-----BEGIN" + r"[A-Z ]*PRIVATE KEY-----"),
    re.compile(
        r"(?i)(api|access|secret|private|auth)[_-]?(key|token)\s*[:=]\s*"
        r"['\"]?[A-Za-z0-9_./+=-]{16,}"
    ),
]

# A private path token ends at a boundary: end-of-text, a path separator,
# whitespace, or common surrounding/terminating punctuation (a quote, a
# backtick, a closing bracket, a comma, colon, semicolon, or period).
# Asserting this boundary -- rather than requiring the path to terminate the
# whole string -- lets the scan catch a private path embedded anywhere in a
# string field: mid-sentence, quoted, in backticks, or before a newline.
PRIVATE_PATH_BOUNDARY = r"""(?=$|[/\s`'")\]},:;.])"""

# The root account's home directory is a bare machine-local path with no
# username segment, so the literal itself is a private value. Assemble it from
# fragments so this file never stores the raw literal (mirrors the secret
# needles and scripts/verify_static_safety.py).
_ROOT_HOME = "/" + "root"

# Private, machine-local absolute paths leak the originating environment into a
# portable manifest. Covered shapes: Unix and macOS per-user home directories
# whether the path ends at the username leaf or continues deeper, the root
# account's home directory whether bare or with a subpath, and Windows per-user
# home directories on any drive letter and either separator. Each may appear
# anywhere in a string field via the shared boundary above.
PRIVATE_PATH_PATTERNS = [
    re.compile(r"/(?:home|Users)/[A-Za-z0-9._-]+" + PRIVATE_PATH_BOUNDARY),
    re.compile(_ROOT_HOME + PRIVATE_PATH_BOUNDARY),
    re.compile(r"(?i)[A-Za-z]:[\\/]Users[\\/][^\\/\s]+"),
]


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def is_nonempty_str(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _looks_secret(value: str) -> bool:
    return any(pattern.search(value) for pattern in SECRET_PATTERNS)


def _looks_private_path(value: str) -> bool:
    return any(pattern.search(value) for pattern in PRIVATE_PATH_PATTERNS)


def validate_manifest(data: object) -> list[str]:
    """Return a list of governance-invariant violations; empty means conforming."""
    reasons: list[str] = []

    if not isinstance(data, dict):
        return ["manifest must be a JSON object"]

    for key in REQUIRED_TOP_LEVEL:
        if key not in data:
            reasons.append(f"missing required field: {key}")

    # Schema/conformance-claim fields are validated semantically, not by presence
    # alone: a present-but-wrong-shape value (a non-string version, a non-object
    # or non-claiming conformance_claim) would otherwise be silently accepted,
    # contradicting the schema and docs/conformance-and-fixtures.md, which
    # describes the manifest as a machine-readable conformance declaration.
    if data.get("manifest_version") != MANIFEST_FORMAT_VERSION:
        reasons.append(
            f"manifest_version must be the string {MANIFEST_FORMAT_VERSION!r} "
            "(the adoption-manifest format version this checker validates)"
        )
    if not is_nonempty_str(data.get("lithos_version")):
        reasons.append("lithos_version must be a non-empty string")
    reasons.extend(_validate_conformance_claim(data.get("conformance_claim")))

    model = data.get("governance_model")
    if model != GOVERNANCE_MODEL:
        reasons.append(
            f"governance_model must be {GOVERNANCE_MODEL!r}; Lithos defines "
            f"exactly one governance model and no adoption tiers (got {model!r})"
        )

    reasons.extend(_validate_workflow_path(data.get("local_workflow_file")))

    reasons.extend(_validate_roles(data.get("roles")))
    reasons.extend(_validate_gates(data.get("approval_gates")))
    reasons.extend(_validate_authority(data.get("approval_authority")))
    reasons.extend(_validate_verification(data.get("verification")))
    reasons.extend(_validate_pr_policy(data.get("autonomous_pr_policy")))

    # The full-lifecycle model always maintains the knowledge spine, so its
    # anchors are required of every conforming manifest. A small project may keep
    # the values terse, but the fields are present, not optional.
    reasons.extend(_validate_knowledge_governance(data.get("knowledge_governance")))

    # Whole-manifest safety scan: no string value anywhere may be secret-shaped
    # or a private machine-local absolute path.
    _scan_sensitive_values(data, "", reasons)

    return reasons


def _validate_workflow_path(workflow: object) -> list[str]:
    """Enforce that ``local_workflow_file`` is one portable, repo-relative path.

    A standalone checker cannot know an adopting repository's root, so it cannot
    prove the file physically exists; it enforces a safe, portable *shape* and
    leaves presence to the adopting project's local verifier. Secret-shaped and
    private machine-local values are caught by the manifest-wide scan as well.
    """
    if isinstance(workflow, list):
        return ["local_workflow_file must be a single string, not an array"]
    if not is_nonempty_str(workflow):
        return ["local_workflow_file must be a single non-empty string"]

    reasons: list[str] = []
    if workflow.startswith("~"):
        reasons.append(
            "local_workflow_file must be a portable repo-relative path, "
            "not a home directory reference"
        )
    if workflow.startswith("/") or re.match(r"[A-Za-z]:[\\/]", workflow):
        reasons.append(
            "local_workflow_file must be a repo-relative path, not an absolute path"
        )
    if "\\" in workflow:
        reasons.append(
            "local_workflow_file must use portable '/' separators, not '\\'"
        )
    if "://" in workflow:
        reasons.append("local_workflow_file must be a repo-relative path, not a URL")

    parts = workflow.split("/")
    if any(part == ".." for part in parts):
        reasons.append("local_workflow_file must not contain path traversal ('..')")
    if not workflow.startswith("/") and any(part == "" for part in parts):
        reasons.append("local_workflow_file must not contain an empty path segment")
    return reasons


def _scan_sensitive_values(node: object, path: str, reasons: list[str]) -> None:
    """Recursively flag any string value that is secret-shaped or a private path."""
    if isinstance(node, dict):
        for key, value in node.items():
            child = f"{path}.{key}" if path else str(key)
            _scan_sensitive_values(value, child, reasons)
    elif isinstance(node, list):
        for index, value in enumerate(node):
            _scan_sensitive_values(value, f"{path}[{index}]", reasons)
    elif isinstance(node, str):
        label = path or "manifest"
        if _looks_secret(node):
            reasons.append(f"{label} must not contain a secret-shaped value")
        elif _looks_private_path(node):
            reasons.append(
                f"{label} must not contain a private machine-local absolute path"
            )


def _validate_conformance_claim(claim: object) -> list[str]:
    """Enforce that the manifest actually declares conformance.

    The schema types ``conformance_claim`` as an object carrying a boolean
    ``claims_conformance`` and a string ``statement``, and
    docs/conformance-and-fixtures.md describes the manifest as a machine-readable
    conformance declaration. A manifest the checker accepts as conforming must
    therefore *claim* conformance: ``claims_conformance`` must be exactly true (a
    false or non-boolean value is a non-claim, not a smaller claim) and
    ``statement`` must be a non-empty string describing the claim.
    """
    if not isinstance(claim, dict):
        return ["conformance_claim must be an object"]
    reasons: list[str] = []
    if claim.get("claims_conformance") is not True:
        reasons.append("conformance_claim.claims_conformance must be true")
    if not is_nonempty_str(claim.get("statement")):
        reasons.append("conformance_claim.statement must be a non-empty string")
    return reasons


def _validate_roles(roles: object) -> list[str]:
    reasons: list[str] = []
    if not isinstance(roles, dict):
        return ["roles must be an object"]
    for role in REQUIRED_ROLES:
        entry = roles.get(role)
        if not isinstance(entry, dict):
            reasons.append(f"roles.{role} must be present and an object")
            continue
        if not is_nonempty_str(entry.get("assigned_to")):
            reasons.append(f"roles.{role}.assigned_to must be a non-empty string")
    owner = roles.get("owner")
    if isinstance(owner, dict) and owner.get("human") is not True:
        reasons.append("roles.owner.human must be true (the owner is a human)")
    return reasons


def _validate_gates(gates: object) -> list[str]:
    reasons: list[str] = []
    if not isinstance(gates, dict):
        return ["approval_gates must be an object"]
    for gate in REQUIRED_GATES:
        if gate not in gates:
            reasons.append(f"approval_gates.{gate} must be present")
        elif not isinstance(gates.get(gate), dict):
            # A required gate that is null, a string, a list, or a boolean cannot
            # carry the invariant flags below, so the gate would be silently
            # accepted. Reject every non-object gate entry outright.
            reasons.append(f"approval_gates.{gate} must be an object")
    for gate in OWNER_APPROVAL_GATES:
        entry = gates.get(gate)
        if isinstance(entry, dict) and entry.get("owner_approval_required") is not True:
            reasons.append(
                f"approval_gates.{gate}.owner_approval_required must be true"
            )
    # The live/runtime gate may never be weakened: regardless of whether it is
    # declared in scope, owner approval and separate controls are mandatory.
    live = gates.get("live_runtime")
    if isinstance(live, dict):
        if live.get("owner_approval_required") is not True:
            reasons.append(
                "approval_gates.live_runtime.owner_approval_required must be true"
            )
        if live.get("separate_controls_required") is not True:
            reasons.append(
                "approval_gates.live_runtime.separate_controls_required must be true"
            )
    return reasons


def _validate_authority(authority: object) -> list[str]:
    reasons: list[str] = []
    if not isinstance(authority, dict):
        return ["approval_authority must be an object"]
    if authority.get("holder") != "owner":
        reasons.append("approval_authority.holder must be 'owner'")
    if authority.get("delegable_to_agent") is not False:
        reasons.append("approval_authority.delegable_to_agent must be false")
    if authority.get("separate_from_verification_evidence") is not True:
        reasons.append(
            "approval_authority.separate_from_verification_evidence must be true"
        )
    if authority.get("separate_from_run_records") is not True:
        reasons.append("approval_authority.separate_from_run_records must be true")
    return reasons


def _validate_verification(verification: object) -> list[str]:
    if not isinstance(verification, dict):
        return ["verification must be an object"]
    if verification.get("evidence_required") is not True:
        return ["verification.evidence_required must be true"]
    return []


def _validate_pr_policy(policy: object) -> list[str]:
    reasons: list[str] = []
    if not isinstance(policy, dict):
        return ["autonomous_pr_policy must be an object"]
    for action in FORBIDDEN_PR_ACTIONS:
        if policy.get(action) is not False:
            reasons.append(
                f"autonomous_pr_policy.{action} must be false; "
                "Lithos adoption never licenses it"
            )
    approvals = policy.get("owner_approval_required_for")
    if not isinstance(approvals, list):
        reasons.append("autonomous_pr_policy.owner_approval_required_for must be an array")
    else:
        for action in REQUIRED_PR_APPROVALS:
            if action not in approvals:
                reasons.append(
                    "autonomous_pr_policy.owner_approval_required_for must include "
                    f"'{action}'"
                )
    return reasons


def _validate_knowledge_governance(knowledge: object) -> list[str]:
    reasons: list[str] = []
    if not isinstance(knowledge, dict):
        return [
            "knowledge_governance is required for the full-lifecycle governance "
            "model and must be an object"
        ]
    for field in REQUIRED_KNOWLEDGE_GOVERNANCE:
        if not is_nonempty_str(knowledge.get(field)):
            reasons.append(f"knowledge_governance.{field} must be a non-empty string")
    return reasons


def check_schema(errors: list[str]) -> None:
    """Parse the schema and confirm it stays in sync with these checks."""
    if not SCHEMA_PATH.exists():
        errors.append(f"missing schema: {SCHEMA_PATH.relative_to(ROOT)}")
        return
    try:
        schema = load_json(SCHEMA_PATH)
    except json.JSONDecodeError as exc:
        errors.append(f"schema is invalid JSON: {exc}")
        return
    if not isinstance(schema, dict):
        errors.append("schema must be a JSON object")
        return
    required = schema.get("required")
    if not isinstance(required, list) or sorted(required) != sorted(REQUIRED_TOP_LEVEL):
        errors.append("schema.required does not match the checker's REQUIRED_TOP_LEVEL")
    const = (
        schema.get("properties", {})
        .get("governance_model", {})
        .get("const")
    )
    if const != GOVERNANCE_MODEL:
        errors.append(
            "schema governance_model.const does not match the checker's single "
            "governance model"
        )


def check_passing(path: Path, label: str, errors: list[str]) -> bool:
    rel = path.relative_to(ROOT)
    if not path.exists():
        errors.append(f"missing {label}: {rel}")
        return False
    try:
        data = load_json(path)
    except json.JSONDecodeError as exc:
        errors.append(f"{label} {rel}: invalid JSON: {exc}")
        return False
    reasons = validate_manifest(data)
    if reasons:
        for reason in reasons:
            errors.append(f"{label} {rel} must pass but failed: {reason}")
        return False
    return True


def check_failing(path: Path, errors: list[str]) -> bool:
    rel = path.relative_to(ROOT)
    if not path.exists():
        errors.append(f"missing invalid fixture: {rel}")
        return False
    try:
        data = load_json(path)
    except json.JSONDecodeError as exc:
        reasons = [f"invalid JSON: {exc}"]
    else:
        reasons = validate_manifest(data)
    if not reasons:
        errors.append(f"{rel} must fail conformance but passed every invariant")
        return False
    marker = INVALID_REASON_MARKERS.get(path.name)
    if marker and not any(marker in reason for reason in reasons):
        errors.append(
            f"{rel} failed, but not for the intended reason '{marker}'; "
            f"reasons were: {reasons}"
        )
        return False
    return True


def run_self_tests() -> list[str]:
    """Prove the safety/path invariants by mutating a known-good manifest in memory.

    A clean run of this checker should mean the invariants are actually enforced,
    not that no fixture happened to exercise them. So before scanning fixtures we
    take a known-good manifest, mutate one field at a time into a known-bad shape,
    and confirm each case fails for its intended reason. Sensitive probes are
    assembled from fragments at runtime, so no secret-shaped or private literal is
    stored in this file.
    """
    failures: list[str] = []
    base_path = FIXTURES_DIR / "valid-full-lifecycle-governance.json"
    try:
        base = load_json(base_path)
    except (OSError, json.JSONDecodeError) as exc:
        return [f"self-test: could not load known-good manifest {base_path.name}: {exc}"]
    if not isinstance(base, dict):
        return ["self-test: known-good manifest is not a JSON object"]

    baseline = validate_manifest(base)
    if baseline:
        return [f"self-test: known-good manifest unexpectedly failed: {baseline}"]

    # Probes built from fragments so this file never stores a sensitive literal.
    secret_probe = "gh" + "p_" + "S" * 32
    # Hyphenated body (e.g. sk-<word>-<long-body>) must also be flagged (B2 fix).
    hyphenated_secret_probe = "sk-" + "proj-" + "T" * 28
    home_probe = "/" + "home/" + "examplecontributor/" + "project/AI_FLOW.md"
    root_probe = "/" + "root/" + ".bash" + "rc"
    root_leaf_probe = "/" + "root"
    windows_home_probe = (
        "C:" + "\\" + "Users" + "\\" + "alice" + "\\" + ".ssh" + "\\" + "id_rsa"
    )
    # Private paths embedded mid-sentence in an arbitrary string field, not just
    # terminating it (B1). docs/conformance-and-fixtures.md claims any string
    # field is scanned recursively, so a path in prose must be rejected too.
    home_in_prose_probe = "see " + "/" + "home/" + "examplecontributor" + " for details"
    root_in_prose_probe = "see " + "/" + "root" + " for details"

    # (description, key path into the manifest, replacement value, required marker)
    cases = [
        ("secret in roles.owner.assigned_to",
         ["roles", "owner", "assigned_to"], secret_probe, "secret-shaped"),
        ("hyphenated secret-shaped value in roles.owner.assigned_to",
         ["roles", "owner", "assigned_to"], hyphenated_secret_probe, "secret-shaped"),
        ("secret in local_workflow_file",
         ["local_workflow_file"], secret_probe, "secret-shaped"),
        ("private home path in local_workflow_file",
         ["local_workflow_file"], home_probe, "private machine-local absolute path"),
        ("root home path in roles.reviewer.assigned_to",
         ["roles", "reviewer", "assigned_to"], root_probe, "private machine-local"),
        ("root leaf path in roles.reviewer.assigned_to",
         ["roles", "reviewer", "assigned_to"], root_leaf_probe, "private machine-local"),
        ("windows home path in roles.reviewer.assigned_to",
         ["roles", "reviewer", "assigned_to"], windows_home_probe, "private machine-local"),
        ("home path embedded in a prose string field",
         ["roles", "architect", "assigned_to"], home_in_prose_probe, "private machine-local"),
        ("root home path embedded in a prose string field",
         ["roles", "verifier", "assigned_to"], root_in_prose_probe, "private machine-local"),
        ("absolute local_workflow_file",
         ["local_workflow_file"], "/etc/lithos/AI_FLOW.md", "absolute"),
        ("url-like local_workflow_file",
         ["local_workflow_file"], "https://example.invalid/AI_FLOW.md", "URL"),
        ("path traversal in local_workflow_file",
         ["local_workflow_file"], "../" + "../outside-repo/AI_FLOW.md", "path traversal"),
        ("empty segment in local_workflow_file",
         ["local_workflow_file"], "docs//AI_FLOW.md", "empty path segment"),
        ("empty local_workflow_file",
         ["local_workflow_file"], "", "single non-empty string"),
        # Lithos defines exactly one governance model: any other value -- a
        # removed tier name or an unknown string -- must be rejected, so the
        # single-model invariant cannot be silently weakened back into tiers.
        # The removed tier name is assembled from fragments so this file never
        # stores the retired literal that the docs stale-term guard forbids.
        ("removed-tier governance_model",
         ["governance_model"], "lighter" + "-governed-workflow", "governance_model"),
        ("unknown governance_model",
         ["governance_model"], "lite", "governance_model"),
        # Schema/conformance-claim fields must be validated semantically, not by
        # presence alone (the schema types these fields and
        # docs/conformance-and-fixtures.md calls the manifest a machine-readable
        # conformance declaration). A field that is present but the wrong type,
        # empty, or a non-claim must be rejected, not silently accepted.
        ("non-string manifest_version",
         ["manifest_version"], 1, "manifest_version"),
        ("unknown manifest_version format",
         ["manifest_version"], "9.9", "manifest_version"),
        ("non-string lithos_version",
         ["lithos_version"], 1, "lithos_version"),
        ("empty lithos_version",
         ["lithos_version"], "   ", "lithos_version"),
        ("null conformance_claim",
         ["conformance_claim"], None, "conformance_claim must be an object"),
        ("non-object conformance_claim",
         ["conformance_claim"], "conforms to Lithos", "conformance_claim must be an object"),
        ("claims_conformance false",
         ["conformance_claim", "claims_conformance"], False, "claims_conformance"),
        ("non-bool claims_conformance",
         ["conformance_claim", "claims_conformance"], "yes", "claims_conformance"),
        ("missing conformance_claim.statement",
         ["conformance_claim"], {"claims_conformance": True}, "statement"),
        ("empty conformance_claim.statement",
         ["conformance_claim", "statement"], "   ", "statement"),
        ("non-string conformance_claim.statement",
         ["conformance_claim", "statement"], 123, "statement"),
    ]
    for description, key_path, value, marker in cases:
        mutated = copy.deepcopy(base)
        target = mutated
        for key in key_path[:-1]:
            target = target[key]
        target[key_path[-1]] = value
        reasons = validate_manifest(mutated)
        if not any(marker in reason for reason in reasons):
            failures.append(
                f"self-test: mutation '{description}' did not fail for '{marker}'; "
                f"reasons were: {reasons}"
            )

    # A hyphenated token that merely embeds the substring 'sk-' (e.g. 'task-...')
    # is an ordinary identifier, not a secret; the secret pattern's left
    # boundary must not misflag it (B2). Built from fragments at runtime.
    benign_token = "task-" + "1" * 30
    benign = copy.deepcopy(base)
    benign["roles"]["owner"]["assigned_to"] = benign_token
    if any("secret-shaped" in reason for reason in validate_manifest(benign)):
        failures.append(
            "self-test: a benign hyphenated token ('task-...') was misflagged as "
            "secret-shaped"
        )
    return failures


def main() -> int:
    errors: list[str] = []

    self_test_failures = run_self_tests()
    if self_test_failures:
        print("Lithos conformance checker self-test failed:")
        for failure in self_test_failures:
            print(f"- {failure}")
        return 2

    check_schema(errors)

    check_passing(TEMPLATE_PATH, "template", errors)

    valid_count = 0
    invalid_count = 0

    if not FIXTURES_DIR.exists():
        errors.append(f"missing fixtures directory: {FIXTURES_DIR.relative_to(ROOT)}")

    for path in sorted(FIXTURES_DIR.glob("*.json")):
        if path.name.startswith("invalid-"):
            invalid_count += 1
            check_failing(path, errors)
        else:
            valid_count += 1
            check_passing(path, "fixture", errors)

    if errors:
        print("Lithos conformance verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Lithos conformance verification passed.")
    print(
        f"Validated schema, template, and {valid_count + invalid_count} fixture(s) "
        f"({valid_count} passing, {invalid_count} rejecting)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
