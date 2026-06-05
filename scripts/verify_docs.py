#!/usr/bin/env python3
"""Repository documentation verification for Lithos.

Pure-stdlib checks used by local development and GitHub Actions.
"""

from __future__ import annotations

import re
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
    "docs/local-adoption.md",
    "docs/governed-project-structure.md",
    "docs/verification-standards.md",
    "docs/versioning-and-governance.md",
    "skills/create-local-ai-flow/SKILL.md",
    "skills/audit-local-ai-flow/SKILL.md",
    "skills/adapt-ai-flow-for-governed-project/SKILL.md",
    "templates/minimal-ai-flow.md",
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
    "templates/AGENTS.md.snippet",
    "templates/pr-checklist.md",
    "examples/minimal-project/README.md",
    "examples/minimal-project/AI_FLOW.md",
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
    "scripts/verify_docs.py",
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
    ".gitignore",
}

BINARY_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf"}


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
    check_skill_frontmatter(errors)
    check_markdown_links(errors)
    check_forbidden_text(errors)
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
