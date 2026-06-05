#!/usr/bin/env python3
"""Verify the governed Lithos project template after local adoption."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "README.md",
    "README.zh-CN.md",
    "GOAL.md",
    "LESSONS.md",
    "AGENTS.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/verify.yml",
    "docs/AI_FLOW.md",
    "docs/INDEX.md",
    "docs/product/prd.md",
    "docs/design/architecture.md",
    "docs/design/technical-solution.md",
    "docs/roadmap/README.md",
    "docs/roadmap/features.md",
    "docs/roadmap/current-status.md",
    "docs/plans/README.md",
    "docs/dev_log/README.md",
    "docs/lessons/README.md",
    "docs/lessons/_drift_report.md",
    "docs/practices/README.md",
    "docs/evaluation/scenario-regression.md",
    "docs/release/release-governance.md",
    "tools/build_docs_index.py",
    "tools/docs_drift_signal.py",
    "tools/static_safety_scan.py",
]
TEXT_SUFFIXES = {"", ".md", ".py", ".yml", ".yaml", ".toml", ".gitignore"}
SKIP_PARTS = {".git", ".codegraph", "__pycache__", ".pytest_cache", ".venv"}
SECRET_PATTERNS = [
    re.compile("gh" + "p_[A-Za-z0-9_]{20,}"),
    re.compile("github_pat_" + r"[A-Za-z0-9_]{20,}"),
    re.compile("sk-" + r"[A-Za-z0-9_-]{20,}"),
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"verification failed: {message}")


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.is_file() and (path.name == ".gitignore" or path.suffix.lower() in TEXT_SUFFIXES):
            files.append(path)
    return sorted(files)


def run_command(args: list[str], failure_message: str) -> None:
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    require(result.returncode == 0, failure_message)


def check_files() -> None:
    missing = [rel for rel in REQUIRED_FILES if not (ROOT / rel).exists()]
    require(not missing, "missing required files: " + ", ".join(missing))


def check_markers() -> None:
    readme = read("README.md")
    zh = read("README.zh-CN.md")
    for content, rel in ((readme, "README.md"), (zh, "README.zh-CN.md")):
        for marker in ("docs/dev_log/", "docs/lessons/", "docs/practices/", "tools/build_docs_index.py", "tools/docs_drift_signal.py"):
            require(marker in content, f"{rel} missing marker: {marker}")
        require("lithos-adoption-manifest.json" in content, f"{rel} missing adoption manifest marker")
        # P2 release-safety, scenario-regression, and drift-evidence markers.
        for marker in (
            "tools/static_safety_scan.py",
            "docs/evaluation/scenario-regression.md",
            "docs/release/release-governance.md",
            "docs/lessons/_drift_report.md",
        ):
            require(marker in content, f"{rel} missing P2 marker: {marker}")
    require("self-merge" in readme and "vendor-neutral" in readme, "README.md must document autonomous PR and portability rules")
    require("自我合并" in zh and "厂商中立" in zh, "README.zh-CN.md must document autonomous PR and portability rules")
    agents = read("AGENTS.md")
    require("docs/dev_log/" in agents and "docs/practices/" in agents and "README.zh-CN.md" in agents, "AGENTS.md must document knowledge and README sync rules")
    require("self-merge" in agents and "vendor-neutral" in agents and "adoption manifest" in agents and "knowledge records" in agents, "AGENTS.md must document P1 conformance, portability, knowledge, and autonomous PR rules")
    ai_flow = read("docs/AI_FLOW.md")
    require("Autonomous PR policy" in ai_flow and "Conformance and portable artifacts" in ai_flow, "docs/AI_FLOW.md must document P1 PR and portability sections")
    require("self-merge" in ai_flow and "vendor-neutral" in ai_flow and "adoption manifest" in ai_flow, "docs/AI_FLOW.md must document P1 autonomous PR and manifest rules")
    pr_template = read(".github/PULL_REQUEST_TEMPLATE.md")
    require("ownerless auto-merge" in pr_template and "Conformance claim" in pr_template and "knowledge records" in pr_template, "PR template must document P1 review checks")
    require("tools/static_safety_scan.py" in pr_template and "Scenario regression" in pr_template and "provenance evidence" in pr_template, "PR template must document P2 static safety, scenario, and release checks")
    scenario = read("docs/evaluation/scenario-regression.md")
    require("scenario fixture" in scenario and "release gate" in scenario.lower(), "docs/evaluation/scenario-regression.md must define scenario fixtures and the release gate")
    release = read("docs/release/release-governance.md")
    require("self-release" in release and "provenance" in release.lower() and "tools/static_safety_scan.py" in release, "docs/release/release-governance.md must define no-self-release, provenance, and the static safety scan")
    index = read("docs/INDEX.md")
    require("AUTO-GENERATED by tools/build_docs_index.py" in index, "docs/INDEX.md must be generated")
    forbidden_root_links = ("(GOAL.md)", "(../GOAL.md)", "(README.md)", "(../README.md)", "(README.zh-CN.md)", "(../README.zh-CN.md)", "(LESSONS.md)", "(../LESSONS.md)")
    require(not any(link in index for link in forbidden_root_links), "docs/INDEX.md must stay docs-directory-only")


def check_links_and_secrets() -> None:
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in iter_text_files():
        text = path.read_text(encoding="utf-8")
        rel = str(path.relative_to(ROOT))
        for pattern in SECRET_PATTERNS:
            require(not pattern.search(text), f"{rel}: possible secret pattern")
        if path.suffix.lower() != ".md":
            continue
        for raw_target in link_re.findall(text):
            if raw_target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = raw_target.split("#", 1)[0]
            if not target or target.startswith("<"):
                continue
            resolved = (path.parent / target).resolve()
            require(str(resolved).startswith(str(ROOT.resolve())), f"{rel}: link escapes project: {raw_target}")
            require(resolved.exists(), f"{rel}: missing link target: {raw_target}")


def main() -> int:
    check_files()
    check_markers()
    check_links_and_secrets()
    run_command([sys.executable, "tools/build_docs_index.py", "--check"], "docs index check failed")
    run_command([sys.executable, "tools/docs_drift_signal.py", "--check"], "docs drift check failed")
    run_command([sys.executable, "tools/static_safety_scan.py"], "static safety scan failed")
    print(f"Governed Lithos project verification passed. Checked {len(REQUIRED_FILES)} required files and {len(iter_text_files())} text files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
