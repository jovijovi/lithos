#!/usr/bin/env python3
"""Repository documentation verification for Lithos.

Pure-stdlib checks used by local development and GitHub Actions.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "README.zh-CN.md",
    "README.fr.md",
    "README.ru.md",
    "README.es.md",
    "LICENSE",
    "AGENTS.md",
    "assets/lithos-logo-horizontal.png",
    "docs/philosophy.md",
    "docs/core-concepts.md",
    "docs/roles.md",
    "docs/approval-semantics.md",
    "docs/environment-and-sandbox-policy.md",
    "docs/local-adoption.md",
    "docs/governed-project-structure.md",
    "docs/verification-standards.md",
    "docs/agent-run-manifest.md",
    "docs/versioning-and-governance.md",
    "docs/knowledge-governance.md",
    "docs/conformance-and-fixtures.md",
    "docs/tooling-interoperability.md",
    "docs/autonomous-pr-policy.md",
    "docs/static-safety-scan.md",
    "docs/scenario-regression-governance.md",
    "docs/release-and-supply-chain-governance.md",
    "skills/lithos/SKILL.md",
    "skills/lithos/references/adopt-project.md",
    "skills/lithos/references/audit-project.md",
    "skills/lithos/references/governed-upgrade.md",
    "skills/lithos/references/version-upgrade.md",
    "skills/lithos/references/pr-review.md",
    "skills/lithos/references/release-gate.md",
    "skills/lithos/references/agent-role-boundaries.md",
    "skills/lithos/references/conformance-truthfulness.md",
    "templates/governed-ai-flow.md",
    "templates/governed-project/GOAL.md",
    "templates/governed-project/AGENTS.md",
    "templates/governed-project/docs/AI_FLOW.md",
    "templates/governed-project/docs/INDEX.md",
    "templates/governed-project/docs/product/prd.md",
    "templates/governed-project/docs/design/architecture.md",
    "templates/governed-project/docs/design/technical-solution.md",
    "templates/governed-project/docs/roadmap/README.md",
    "templates/governed-project/docs/roadmap/features.md",
    "templates/governed-project/docs/roadmap/current-status.md",
    "templates/governed-project/docs/plans/README.md",
    "templates/governed-project/README.md",
    "templates/governed-project/README.zh-CN.md",
    "templates/governed-project/LESSONS.md",
    "templates/governed-project/.github/PULL_REQUEST_TEMPLATE.md",
    "templates/governed-project/.github/workflows/verify.yml",
    "templates/governed-project/scripts/verify_project.py",
    "templates/governed-project/docs/dev_log/README.md",
    "templates/governed-project/docs/lessons/README.md",
    "templates/governed-project/docs/lessons/_drift_report.md",
    "templates/governed-project/docs/practices/README.md",
    "templates/governed-project/docs/evaluation/scenario-regression.md",
    "templates/governed-project/docs/release/release-governance.md",
    "templates/governed-project/tools/build_docs_index.py",
    "templates/governed-project/tools/docs_drift_signal.py",
    "templates/governed-project/tools/static_safety_scan.py",
    "templates/AGENTS.md.snippet",
    "templates/pr-checklist.md",
    "templates/environment-policy.md",
    "templates/agent-run-manifest.json",
    "schemas/lithos-adoption-manifest.schema.json",
    "templates/lithos-adoption-manifest.json",
    "fixtures/conformance/valid-full-governed-project.json",
    "fixtures/conformance/valid-lighter-governed-workflow.json",
    "fixtures/conformance/invalid-autonomous-self-merge.json",
    "fixtures/conformance/invalid-autonomous-self-approval.json",
    "fixtures/conformance/invalid-live-runtime-without-controls.json",
    "fixtures/conformance/invalid-live-runtime-non-object.json",
    "fixtures/conformance/invalid-workflow-path-traversal.json",
    "fixtures/conformance/invalid-conformance-claim-false.json",
    "examples/governed-project/README.md",
    "examples/governed-project/ai-collaborative-development-standards.md",
    "examples/governed-project/GOAL.md",
    "examples/governed-project/AGENTS.md",
    "examples/governed-project/.github/PULL_REQUEST_TEMPLATE.md",
    "examples/governed-project/docs/AI_FLOW.md",
    "examples/governed-project/docs/INDEX.md",
    "examples/governed-project/docs/product/prd.md",
    "examples/governed-project/docs/design/architecture.md",
    "examples/governed-project/docs/design/technical-solution.md",
    "examples/governed-project/docs/roadmap/README.md",
    "examples/governed-project/docs/roadmap/features.md",
    "examples/governed-project/docs/roadmap/current-status.md",
    "examples/governed-project/docs/plans/README.md",
    "examples/governed-project/README.zh-CN.md",
    "examples/governed-project/LESSONS.md",
    "examples/governed-project/docs/dev_log/2026-06-05-governance-spine-adoption.md",
    "examples/governed-project/docs/lessons/2026-06-05-docs-index-boundary.md",
    "examples/governed-project/docs/lessons/_drift_report.md",
    "examples/governed-project/docs/practices/README.md",
    "examples/governed-project/docs/practices/2026-06-05-governed-project-knowledge-spine.md",
    "examples/governed-project/docs/evaluation/scenario-regression.md",
    "examples/governed-project/docs/release/release-governance.md",
    "examples/governed-project/scripts/verify_project.py",
    "examples/governed-project/tools/build_docs_index.py",
    "examples/governed-project/tools/docs_drift_signal.py",
    "examples/governed-project/tools/static_safety_scan.py",
    "scripts/verify_docs.py",
    "scripts/verify_conformance_fixtures.py",
    "scripts/verify_static_safety.py",
    ".github/workflows/verify.yml",
    ".gitignore",
]

README_FILES = [
    "README.md",
    "README.zh-CN.md",
    "README.fr.md",
    "README.ru.md",
    "README.es.md",
]

LANG_LINKS = {
    "English": "README.md",
    "中文": "README.zh-CN.md",
    "Français": "README.fr.md",
    "Русский": "README.ru.md",
    "Español": "README.es.md",
}

# Construct sensitive / placeholder needles so this checker does not match its
# own source text while scanning repository files.
FORBIDDEN_SUBSTRINGS = [
    "TO" + "DO",
    "T" + "BD",
    "lor" + "em",
    "/home/" + "ecs-user",
    "/data/" + "agents",
    "." + "hermes",
    "Claude" + " Code",
    "Sach" + "ima",
]

SECRET_PATTERNS = [
    re.compile("gh" + "p_[A-Za-z0-9_]{20,}"),
    re.compile("sk-" + r"[A-Za-z0-9_-]{20,}"),
    re.compile(r"(?i)(api|access|secret|private)[_-]?key\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{16,}"),
]

TEXT_SUFFIXES = {
    "",
    ".md",
    ".txt",
    ".yml",
    ".yaml",
    ".py",
    ".json",
    ".gitignore",
}

# JSON files that must parse as valid JSON.
JSON_FILES = [
    "templates/agent-run-manifest.json",
    "schemas/lithos-adoption-manifest.schema.json",
    "templates/lithos-adoption-manifest.json",
    "fixtures/conformance/valid-full-governed-project.json",
    "fixtures/conformance/valid-lighter-governed-workflow.json",
    "fixtures/conformance/invalid-autonomous-self-merge.json",
    "fixtures/conformance/invalid-autonomous-self-approval.json",
    "fixtures/conformance/invalid-live-runtime-without-controls.json",
    "fixtures/conformance/invalid-live-runtime-non-object.json",
    "fixtures/conformance/invalid-workflow-path-traversal.json",
    "fixtures/conformance/invalid-conformance-claim-false.json",
]

BINARY_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf"}

# Plan B single-entry-point invariant: `skills/lithos` is the only first-class
# top-level Lithos skill. The three older focused skills were retired and their
# capability absorbed into `skills/lithos/references/`. These directory names
# must not reappear as independent peer skills, and README/local-adoption prose
# must not present them as four peer top-level skills. The umbrella skill and its
# references carry the standard's load-bearing concepts under
# LITHOS_UMBRELLA_MARKERS below, so a concept cannot silently disappear.
RETIRED_PEER_SKILLS = [
    "create-local-ai-flow",
    "audit-local-ai-flow",
    "adapt-ai-flow-for-governed-project",
]

# The umbrella `lithos` skill is the agent-facing operational entry point an
# installed agent uses to apply Lithos to a real project, plus one reference per
# intent it routes. These markers are exact, vendor-neutral invariants — the
# references it links, the absorbed create/audit/upgrade procedures now inlined
# in those references (proven without linking to the retired peer skills), the
# docs that remain the authority, and the load-bearing boundaries (no
# self-approval/self-merge/ownerless auto-merge, no agent self-release, the
# static safety scan is not behavior proof, the manifest is not authorization) —
# so the capability pack cannot quietly drift behind the standard or drop a
# boundary. Markers are lowercased substrings, matched case-insensitively.
LITHOS_UMBRELLA_MARKERS = {
    "skills/lithos/SKILL.md": [
        "references/adopt-project.md",
        "references/audit-project.md",
        "references/governed-upgrade.md",
        "references/version-upgrade.md",
        "references/pr-review.md",
        "references/release-gate.md",
        "references/agent-role-boundaries.md",
        "references/conformance-truthfulness.md",
        "operational entry point",
        "are the authority",
        "does not make a project conformant",
        "not authorization",
    ],
    "skills/lithos/references/adopt-project.md": [
        "write the local workflow file",
        "lighter governed workflow",
        "full governed project",
        "no minimal profile",
        "adoption manifest",
        "not authorization",
    ],
    "skills/lithos/references/audit-project.md": [
        "walk the conformance checklist",
        "no minimal profile",
        "adoption manifest",
        "conformance fixtures",
        "static safety scan",
        "not behavior proof",
        "scenario regression",
    ],
    "skills/lithos/references/governed-upgrade.md": [
        "what the upgrade adds",
        "lighter governed workflow",
        "full governed project",
        "never loosen",
        "knowledge spine",
        "scenario regression",
        "release and supply-chain",
    ],
    "skills/lithos/references/version-upgrade.md": [
        "../../../docs/versioning-and-governance.md",
        "claimed lithos version",
        "missing deltas",
        "adoption manifest",
        "re-verified fresh",
    ],
    "skills/lithos/references/pr-review.md": [
        "../../../docs/autonomous-pr-policy.md",
        "role and gate drift",
        "manifest truthfulness",
        "self-approval",
        "self-merge",
        "ownerless auto-merge",
        "static safety scan",
        "scenario regression",
    ],
    "skills/lithos/references/release-gate.md": [
        "../../../docs/release-and-supply-chain-governance.md",
        "separate blockers from notes",
        "no agent self-release",
        "owner approval",
        "provenance record",
        "static safety scan",
    ],
    "skills/lithos/references/agent-role-boundaries.md": [
        "../../../docs/roles.md",
        "../../../docs/approval-semantics.md",
        "approval authority is human-only",
        "independent of the implementation",
        "self-approval",
        "self-merge",
        "ownerless auto-merge",
        "not authorization",
    ],
    "skills/lithos/references/conformance-truthfulness.md": [
        "../../../docs/conformance-and-fixtures.md",
        "what the project says must match what the project does",
        "manifest, schema, and checker",
        "worked-example commands",
        "static safety scan",
        "not behavior proof",
    ],
    "docs/local-adoption.md": [
        "../skills/lithos/SKILL.md",
        "operational entry point",
        "focused create, audit, governed-upgrade, version-upgrade, pr-review, and release-gate procedures",
        "docs/` authoritative",
    ],
}


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def iter_text_files() -> list[Path]:
    paths: list[Path] = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or ".codegraph" in path.parts:
            continue
        if path.is_dir():
            continue
        if path.suffix.lower() in BINARY_SUFFIXES:
            continue
        if path.name == ".gitignore" or path.suffix.lower() in TEXT_SUFFIXES:
            paths.append(path)
    return sorted(paths)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_required_files(errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if not path.exists():
            fail(f"missing required file: {rel}", errors)


def check_readme_language_links(errors: list[str]) -> None:
    for rel in README_FILES:
        path = ROOT / rel
        if not path.exists():
            continue
        content = read_text(path)
        for label, target in LANG_LINKS.items():
            if f"[{label}]({target})" not in content:
                fail(f"{rel}: missing language link [{label}]({target})", errors)
            if not (ROOT / target).exists():
                fail(f"{rel}: language link target missing: {target}", errors)



def check_readme_semantic_sync(errors: list[str]) -> None:
    shared_markers = [
        "docs/governed-project-structure.md",
        "docs/environment-and-sandbox-policy.md",
        "docs/agent-run-manifest.md",
        "docs/knowledge-governance.md",
        "docs/conformance-and-fixtures.md",
        "docs/tooling-interoperability.md",
        "docs/autonomous-pr-policy.md",
        "docs/static-safety-scan.md",
        "docs/scenario-regression-governance.md",
        "docs/release-and-supply-chain-governance.md",
        "schemas/lithos-adoption-manifest.schema.json",
        "templates/lithos-adoption-manifest.json",
        "fixtures/conformance/",
        "templates/governed-project/",
        "skills/lithos/SKILL.md",
        "docs/dev_log/",
        "docs/lessons/",
        "docs/practices/",
        "tools/",
    ]
    for rel in README_FILES:
        path = ROOT / rel
        if not path.exists():
            continue
        content = read_text(path)
        for marker in shared_markers:
            if marker not in content:
                fail(f"{rel}: missing synchronized README marker: {marker}", errors)


def run_subcheck(cwd: Path, args: list[str], errors: list[str]) -> None:
    result = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    if result.returncode != 0:
        detail = (result.stdout + result.stderr).strip().splitlines()
        suffix = f": {detail[-1]}" if detail else ""
        fail(f"{cwd.relative_to(ROOT)}: subcheck failed: {' '.join(args)}{suffix}", errors)


def check_governed_project_generators(errors: list[str]) -> None:
    # Both the template and the example ship their own scripts/verify_project.py
    # wrapper. Each wrapper runs the docs index check, the drift self-test and
    # check, and the static safety scan, so running the wrapper exercises that
    # surface's full generator/boundary logic as a single entry point.
    for rel in ("templates/governed-project", "examples/governed-project"):
        run_subcheck(ROOT / rel, [sys.executable, "scripts/verify_project.py"], errors)


def check_example_verification_truthfulness(errors: list[str]) -> None:
    """Keep the worked example's self-declared gates runnable and truthful.

    The example ships no ``tests/`` directory and no ``scripts/verify_docs.py``,
    so a verification block listing those commands is a broken gate that fails
    the moment a contributor runs it. Forbid those two commands in the example's
    ``docs/AI_FLOW.md`` and require the runnable local verifier and static safety
    scan across the example's verifier surface (AI_FLOW plus AGENTS). This is a
    narrow truthfulness guard, not a general command parser.
    """
    ai_flow_rel = "examples/governed-project/docs/AI_FLOW.md"
    agents_rel = "examples/governed-project/AGENTS.md"
    ai_flow_path = ROOT / ai_flow_rel
    if not ai_flow_path.exists():
        fail(f"missing required file: {ai_flow_rel}", errors)
        return
    ai_flow = read_text(ai_flow_path)
    broken_commands = (
        "python -m unittest discover -s tests",
        "python3 -m unittest discover -s tests",
        "python scripts/verify_docs.py",
        "python3 scripts/verify_docs.py",
    )
    for command in broken_commands:
        if command in ai_flow:
            fail(f"{ai_flow_rel}: lists a command that cannot run in the example: {command}", errors)
    surface = ai_flow
    agents_path = ROOT / agents_rel
    if agents_path.exists():
        surface += "\n" + read_text(agents_path)
    for command in ("python scripts/verify_project.py", "python tools/static_safety_scan.py"):
        if command not in surface:
            fail(f"example verification surface missing runnable gate: {command}", errors)


def check_conformance_fixtures(errors: list[str]) -> None:
    run_subcheck(ROOT, [sys.executable, "scripts/verify_conformance_fixtures.py"], errors)


def check_static_safety(errors: list[str]) -> None:
    run_subcheck(ROOT, [sys.executable, "scripts/verify_static_safety.py"], errors)


def check_skill_frontmatter(errors: list[str]) -> None:
    for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
        content = read_text(path)
        if not content.startswith("---\n"):
            fail(f"{path.relative_to(ROOT)}: missing YAML frontmatter", errors)
            continue
        parts = content.split("---", 2)
        if len(parts) < 3:
            fail(f"{path.relative_to(ROOT)}: malformed YAML frontmatter", errors)
            continue
        frontmatter = parts[1]
        for field in ("name:", "description:"):
            if field not in frontmatter:
                fail(f"{path.relative_to(ROOT)}: frontmatter missing {field}", errors)


def check_retired_peer_skills_absent(errors: list[str]) -> None:
    """Plan B single-entry-point invariant: the three retired focused skills must
    not reappear as independent peer skills. Fail if any retired peer skill ships
    its own ``skills/<old-name>/SKILL.md`` or its old peer directory comes back."""
    for name in RETIRED_PEER_SKILLS:
        skill_dir = ROOT / "skills" / name
        skill_file = skill_dir / "SKILL.md"
        if skill_file.exists():
            fail(f"retired peer skill reappeared as a first-class skill: skills/{name}/SKILL.md", errors)
        elif skill_dir.exists():
            fail(f"retired peer skill directory reappeared: skills/{name}/", errors)


def check_public_surface_retired_skills_absent(errors: list[str]) -> None:
    """Plan B single-entry-point invariant on public adoption prose: the README
    localizations and ``docs/local-adoption.md`` must not present the three
    retired focused skills as peer top-level skills. Fail if any retired peer
    skill name appears in those surfaces, whether as a bare name
    (``create-local-ai-flow``) or as a peer-skill path
    (``skills/create-local-ai-flow/``); matching the bare name catches both
    because the path embeds it. This scans only the public surfaces below, never
    this verifier, so listing the retired names in ``RETIRED_PEER_SKILLS`` does
    not self-fail."""
    public_surfaces = list(README_FILES) + ["docs/local-adoption.md"]
    for rel in public_surfaces:
        path = ROOT / rel
        if not path.exists():
            continue
        content = read_text(path)
        for name in RETIRED_PEER_SKILLS:
            if name in content:
                fail(
                    f"{rel}: retired peer skill presented as a peer top-level skill: {name}",
                    errors,
                )


def check_lithos_umbrella_sync(errors: list[str]) -> None:
    """Require the umbrella `lithos` skill and its references to keep markers for
    the standard's load-bearing concepts, so the operational entry point cannot
    drift behind the docs or quietly drop a boundary."""
    for rel, markers in LITHOS_UMBRELLA_MARKERS.items():
        path = ROOT / rel
        if not path.exists():
            fail(f"missing required file: {rel}", errors)
            continue
        lowered = read_text(path).lower()
        for marker in markers:
            if marker.lower() not in lowered:
                fail(f"{rel}: missing umbrella skill marker: {marker}", errors)


def check_markdown_links(errors: list[str]) -> None:
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in iter_text_files():
        if path.suffix.lower() != ".md":
            continue
        content = read_text(path)
        for raw_target in link_re.findall(content):
            if raw_target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = raw_target.split("#", 1)[0]
            if not target or target.startswith("<"):
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                fail(f"{path.relative_to(ROOT)}: link escapes repo: {raw_target}", errors)
                continue
            if not resolved.exists():
                fail(f"{path.relative_to(ROOT)}: missing link target: {raw_target}", errors)


def check_forbidden_text(errors: list[str]) -> None:
    for path in iter_text_files():
        rel = str(path.relative_to(ROOT))
        content = read_text(path)
        lowered = content.lower()
        for needle in FORBIDDEN_SUBSTRINGS:
            haystack = lowered if needle == "lor" + "em" else content
            query = needle.lower() if needle == "lor" + "em" else needle
            if query in haystack:
                fail(f"{rel}: forbidden placeholder/private reference: {needle}", errors)
        for pattern in SECRET_PATTERNS:
            if pattern.search(content):
                fail(f"{rel}: possible secret/token pattern", errors)


def check_json_files(errors: list[str]) -> None:
    for rel in JSON_FILES:
        path = ROOT / rel
        if not path.exists():
            continue
        try:
            json.loads(read_text(path))
        except json.JSONDecodeError as exc:
            fail(f"{rel}: invalid JSON: {exc}", errors)


def check_license(errors: list[str]) -> None:
    license_path = ROOT / "LICENSE"
    if not license_path.exists():
        return
    content = read_text(license_path)
    if "MIT License" not in content:
        fail("LICENSE: missing MIT License heading", errors)
    if "jovijovi and Lithos Contributors" not in content:
        fail("LICENSE: missing expected copyright holder", errors)


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_readme_language_links(errors)
    check_readme_semantic_sync(errors)
    check_governed_project_generators(errors)
    check_example_verification_truthfulness(errors)
    check_conformance_fixtures(errors)
    check_static_safety(errors)
    check_skill_frontmatter(errors)
    check_retired_peer_skills_absent(errors)
    check_public_surface_retired_skills_absent(errors)
    check_lithos_umbrella_sync(errors)
    check_markdown_links(errors)
    check_forbidden_text(errors)
    check_json_files(errors)
    check_license(errors)

    if errors:
        print("Lithos verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Lithos verification passed.")
    print(f"Checked {len(REQUIRED_FILES)} required files and {len(iter_text_files())} text files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
