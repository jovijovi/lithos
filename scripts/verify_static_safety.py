#!/usr/bin/env python3
"""Static safety scan for the Lithos repository.

A first-class, machine-runnable governance gate. This pure-stdlib scanner reads
the repository's committed text and rejects three classes of value that must
never enter the governed evidence chain:

* secret-shaped tokens (credential, key, and private-key material);
* private, machine-local absolute filesystem paths that leak a contributor's
  environment into shared text;
* unfinished-work placeholders that mark text as not yet real.

It is reproducible evidence in the sense of ``docs/verification-standards.md``:
anyone can re-run it and observe the same pass/fail result, so a green run is
proof rather than testimony. The normative description of this gate lives in
``docs/static-safety-scan.md``.

Two design rules keep the scanner honest:

1. **No self-match.** Every sensitive needle is assembled from split fragments,
   so this file never contains a value that one of its own patterns would flag.
2. **Self-test.** Before scanning, the engine runs on dynamically constructed
   probes — secret-like strings built at runtime by concatenation, never stored
   as literals — and confirms it flags the bad ones and clears a clean one. A
   reviewer can therefore trust that a clean scan means the engine works, not
   that it silently matched nothing.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_PARTS = {".git", ".codegraph", "__pycache__", ".pytest_cache", ".venv", "node_modules"}
BINARY_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".zip", ".gz"}
TEXT_SUFFIXES = {
    "",
    ".md",
    ".txt",
    ".yml",
    ".yaml",
    ".py",
    ".json",
    ".toml",
    ".cfg",
    ".ini",
    ".gitignore",
}

# Secret/token shapes. Each needle is assembled from fragments so this file
# never contains a value that matches one of its own patterns.
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
# whole scanned text -- lets the patterns catch a private path embedded in
# prose, wrapped in quotes or backticks, or sitting just before a newline.
PRIVATE_PATH_BOUNDARY = r"""(?=$|[/\s`'")\]},:;.])"""

# The root account's home directory is a bare machine-local path with no
# username segment, so the literal itself is a private value. Assemble it from
# fragments so this file never stores the raw literal, mirroring the
# "no self-match" rule the secret needles follow.
_ROOT_HOME = "/" + "root"

# Private, machine-local absolute paths. Covers Unix/macOS per-user home
# directories whether the path ends at the username leaf or continues deeper,
# the root account's home directory whether bare or with a subpath, and Windows
# per-user home directories on any drive letter with either separator style.
# Each may appear anywhere in a document -- mid-sentence, quoted, in backticks,
# or before a newline -- via the shared boundary above.
PRIVATE_PATH_PATTERNS = [
    re.compile(r"/(?:home|Users)/[A-Za-z0-9._-]+" + PRIVATE_PATH_BOUNDARY),
    re.compile(_ROOT_HOME + PRIVATE_PATH_BOUNDARY),
    re.compile(r"(?i)[A-Za-z]:[\\/]Users[\\/][^\\/\s]+"),
]

# Unfinished-work placeholders, assembled from fragments for the same reason.
# Matched case-sensitively except for the filler-text needle.
PLACEHOLDER_NEEDLES = [
    "TO" + "DO",
    "FIX" + "ME",
    "T" + "BD",
]
FILLER_NEEDLE = "lor" + "em"


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        if not path.is_file():
            continue
        if path.suffix.lower() in BINARY_SUFFIXES:
            continue
        if path.name == ".gitignore" or path.suffix.lower() in TEXT_SUFFIXES:
            files.append(path)
    return sorted(files)


def scan_text(label: str, text: str) -> list[str]:
    """Return a list of findings for a single document; empty means clean."""
    findings: list[str] = []
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            findings.append(f"{label}: secret/token-shaped value")
            break
    for pattern in PRIVATE_PATH_PATTERNS:
        if pattern.search(text):
            findings.append(f"{label}: private machine-local absolute path")
            break
    for needle in PLACEHOLDER_NEEDLES:
        if needle in text:
            findings.append(f"{label}: unfinished-work placeholder ({needle})")
            break
    if FILLER_NEEDLE in text.lower():
        findings.append(f"{label}: filler placeholder text")
    return findings


def run_self_tests() -> list[str]:
    """Confirm the engine flags dynamically built bad probes and clears a clean one.

    Probes are constructed at runtime by concatenation so no credential-shaped
    literal is ever stored in this file.
    """
    failures: list[str] = []
    bad_probes = {
        "token-prefix-shape": "gh" + "p_" + "A" * 36,
        "long-access-token-shape": "github" + "_pat_" + "B" * 24,
        "secret-prefix-shape": "sk-" + "C" * 32,
        "hyphenated-secret-shape": "sk-" + "proj-" + "D" * 28,
        "cloud-access-key-shape": "AK" + "IA" + "E" * 16,
        "service-token-shape": "xox" + "b-" + "1" * 14,
        "private-key-header": "-----BEGIN" + " RSA PRIVATE KEY-----",
        "key-assignment": "api" + "_token" + "=" + "F" * 24,
        "home-path-nested": "/" + "home/" + "examplecontributor/" + "project",
        "home-path-leaf": "/" + "home/" + "examplecontributor",
        "users-path-leaf": "/" + "Users/" + "examplecontributor",
        "root-path-leaf": "/" + "root",
        "root-dotfile": "/" + "root/" + ".bash" + "rc",
        "windows-home": "C:" + chr(92) + "Users" + chr(92) + "alice" + chr(92) + "project",
        # Private paths embedded in text, not just terminating it: a dynamically
        # built quoted path, a path mid-sentence, a path wrapped in backticks,
        # and a root leaf sitting just before a newline. All built from
        # fragments so this file stores no raw private literal.
        "home-path-quoted": "path=" + chr(34) + "/" + "home/" + "alice" + chr(34),
        "home-path-in-prose": "see " + "/" + "home/" + "examplecontributor" + " for details",
        "root-path-in-prose": "see " + "/" + "root" + " for details",
        "home-path-in-backticks": chr(96) + "/" + "home/" + "examplecontributor" + chr(96),
        "root-path-before-newline": "/" + "root" + chr(10) + "next line",
        "placeholder": "left a " + "TO" + "DO marker",
    }
    for label, probe in bad_probes.items():
        if not scan_text(label, probe):
            failures.append(f"self-test: scanner failed to flag {label!r}")
    clean_probes = {
        "prose": "A governed change ships with reproducible evidence and no secrets.",
        # 'task-' embeds the substring 'sk-' but is an ordinary hyphenated
        # token, not a secret; the secret pattern's left boundary must keep it
        # clean. Built from fragments at runtime.
        "hyphenated-task-token": "task-" + "1" * 30,
    }
    for label, probe in clean_probes.items():
        if scan_text(label, probe):
            failures.append(f"self-test: scanner flagged a known-clean probe ({label})")
    return failures


def main() -> int:
    self_test_failures = run_self_tests()
    if self_test_failures:
        print("Static safety scan self-test failed:")
        for failure in self_test_failures:
            print(f"- {failure}")
        return 2

    findings: list[str] = []
    files = iter_text_files()
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue  # treat as binary; nothing textual to scan
        findings.extend(scan_text(str(path.relative_to(ROOT)), text))

    if findings:
        print("Static safety scan failed:")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("Static safety scan passed.")
    print(f"Self-tested the engine and scanned {len(files)} text files; no findings.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
