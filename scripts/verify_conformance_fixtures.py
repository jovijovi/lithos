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
  ``invalid-autonomous-self-approval.json`` on ``agent_self_approval``, and
  ``invalid-live-runtime-without-controls.json`` on ``live_runtime``).

A manifest declares conformance; it never authorizes anything. These checks
verify the declaration is internally consistent with the governance model.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas/lithos-adoption-manifest.schema.json"
TEMPLATE_PATH = ROOT / "templates/lithos-adoption-manifest.json"
FIXTURES_DIR = ROOT / "fixtures/conformance"

ADOPTION_PROFILES = {"lighter-governed-workflow", "full-governed-project"}

REQUIRED_TOP_LEVEL = [
    "manifest_version",
    "lithos_version",
    "adoption_profile",
    "conformance_claim",
    "local_workflow_file",
    "roles",
    "approval_gates",
    "approval_authority",
    "verification",
    "autonomous_pr_policy",
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
}


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def is_nonempty_str(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_manifest(data: object) -> list[str]:
    """Return a list of governance-invariant violations; empty means conforming."""
    reasons: list[str] = []

    if not isinstance(data, dict):
        return ["manifest must be a JSON object"]

    for key in REQUIRED_TOP_LEVEL:
        if key not in data:
            reasons.append(f"missing required field: {key}")

    profile = data.get("adoption_profile")
    if profile not in ADOPTION_PROFILES:
        reasons.append(
            "adoption_profile must be one of "
            f"{sorted(ADOPTION_PROFILES)} (got {profile!r})"
        )

    workflow = data.get("local_workflow_file")
    if isinstance(workflow, list):
        reasons.append("local_workflow_file must be a single string, not an array")
    elif not is_nonempty_str(workflow):
        reasons.append("local_workflow_file must be a single non-empty string")

    reasons.extend(_validate_roles(data.get("roles")))
    reasons.extend(_validate_gates(data.get("approval_gates")))
    reasons.extend(_validate_authority(data.get("approval_authority")))
    reasons.extend(_validate_verification(data.get("verification")))
    reasons.extend(_validate_pr_policy(data.get("autonomous_pr_policy")))

    if profile == "full-governed-project":
        reasons.extend(_validate_knowledge_governance(data.get("knowledge_governance")))

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
            "knowledge_governance is required for full-governed-project and must be an object"
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
    enum = (
        schema.get("properties", {})
        .get("adoption_profile", {})
        .get("enum")
    )
    if not isinstance(enum, list) or set(enum) != ADOPTION_PROFILES:
        errors.append("schema adoption_profile.enum does not match the checker's profiles")


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


def main() -> int:
    errors: list[str] = []
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
