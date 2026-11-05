#!/usr/bin/env python3
"""Structural validator for the Recruiter Skills collection.

Usage: python3 tools/validate_skills.py [REPO_ROOT]

Checks structure only. It cannot judge whether natural-language instructions
are safe; every instruction change still needs a human diff review.
Detected credential-like values are never printed, only file, line and kind.
"""
from __future__ import annotations

import os
import re
import stat
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install --require-hashes -r tools/requirements.txt")

EXPECTED_SKILLS = frozenset({
    "recruiter-assess-candidate",
    "recruiter-assess-job-offers",
    "recruiter-define-job-targets",
    "recruiter-develop-skill-evidence",
    "recruiter-diagnose-job-search-funnel",
    "recruiter-discover-verify-vacancies",
    "recruiter-execute-track-applications",
    "recruiter-guard-recruitment-workflow",
    "recruiter-manage-job-followups",
    "recruiter-match-candidate-to-job",
    "recruiter-prepare-job-interview",
    "recruiter-prepare-recruiter-outreach",
    "recruiter-prioritize-applications",
    "recruiter-research-hiring-context",
    "recruiter-run-daily-vacancy-scan",
    "recruiter-screen-job-eligibility",
    "recruiter-tailor-job-application",
})

# Only these files may exist inside a skill directory.
ALLOWED_SKILL_FILES = frozenset({"SKILL.md", "agents/openai.yaml"})

# Allowed top-level entries (files and directories) in the repository root.
ALLOWED_TOP_LEVEL = frozenset({
    ".git", ".github", ".gitignore", ".gitattributes",
    "skills", "tools", "tests",
    "README.md", "SECURITY.md", "CONTRIBUTING.md", "LICENSE",
})

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FRONTMATTER_KEYS = frozenset({"name", "description", "license", "compatibility", "metadata", "allowed-tools"})
MAX_NAME = 64
MAX_DESCRIPTION = 1024
MAX_SKILL_MD = 20_000
MAX_YAML = 4_000
MAX_OTHER_FILE = 100_000
SHARED_BLOCK = "Operating contract"
# Whole-word key tokens (split on _ or -) whose string values are treated as file paths.
PATH_KEY_TOKENS = frozenset({"icon", "path", "file", "asset", "script"})

SECRET_PATTERNS = {
    "private key block": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "AWS access key id": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "GitHub token": re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),
    "API key (sk- style)": re.compile(r"\bsk-[A-Za-z0-9_-]{24,}\b"),
    "credential assignment": re.compile(
        r"(?i)\b(?:password|passwd|secret|api[_-]?key|access[_-]?token)\b\s*[:=]\s*['\"]?[A-Za-z0-9/+_=.-]{12,}"
    ),
}
SKIP_SECRET_SCAN_DIRS = {".git"}


def split_frontmatter(text: str):
    """Return (yaml_text, body) or (None, text) if no frontmatter."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 5:]


def read_text(path: Path, errors: list[str], rel: str):
    try:
        data = path.read_bytes()
    except OSError as exc:
        errors.append(f"{rel}: cannot read ({exc.__class__.__name__})")
        return None
    if b"\x00" in data:
        errors.append(f"{rel}: binary content is not allowed")
        return None
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        errors.append(f"{rel}: not valid UTF-8 text")
        return None


def check_file_hygiene(root: Path, errors: list[str]) -> list[Path]:
    """Walk the repo without following links. Return regular files to scan."""
    files: list[Path] = []
    for entry in sorted(root.iterdir()):
        if entry.name not in ALLOWED_TOP_LEVEL:
            errors.append(f"{entry.name}: unapproved top-level entry")
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_SECRET_SCAN_DIRS or Path(dirpath) != root)
        for name in list(dirnames) + sorted(filenames):
            full = Path(dirpath) / name
            rel = full.relative_to(root).as_posix()
            if ".." in Path(rel).parts:
                errors.append(f"{rel}: path traversal")
                continue
            st = os.lstat(full)
            if stat.S_ISLNK(st.st_mode):
                errors.append(f"{rel}: symlinks are not allowed")
            elif stat.S_ISREG(st.st_mode):
                if st.st_mode & 0o111:
                    errors.append(f"{rel}: executable file mode is not allowed")
                if st.st_size > MAX_OTHER_FILE:
                    errors.append(f"{rel}: file exceeds {MAX_OTHER_FILE} bytes")
                files.append(full)
    return files


def check_skill(root: Path, skill_dir: Path, errors: list[str], names: dict[str, str]) -> str | None:
    rel_dir = skill_dir.relative_to(root).as_posix()
    present = set()
    for path in skill_dir.rglob("*"):
        if path.is_symlink() or not path.is_file():
            continue
        present.add(path.relative_to(skill_dir).as_posix())
    for extra in sorted(present - ALLOWED_SKILL_FILES):
        errors.append(f"{rel_dir}/{extra}: unapproved file under skills/")
    for required in sorted(ALLOWED_SKILL_FILES - present):
        errors.append(f"{rel_dir}/{required}: required file is missing")

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file() or skill_md.is_symlink():
        return None
    rel_md = f"{rel_dir}/SKILL.md"
    if skill_md.stat().st_size > MAX_SKILL_MD:
        errors.append(f"{rel_md}: exceeds {MAX_SKILL_MD} bytes")
    text = read_text(skill_md, errors, rel_md)
    if text is None:
        return None
    fm_text, body = split_frontmatter(text)
    if fm_text is None:
        errors.append(f"{rel_md}: missing YAML frontmatter")
        return None
    try:
        meta = yaml.safe_load(fm_text)
    except yaml.YAMLError:
        errors.append(f"{rel_md}: malformed YAML frontmatter")
        return None
    if not isinstance(meta, dict):
        errors.append(f"{rel_md}: frontmatter must be a mapping")
        return None
    for key in sorted(set(meta) - FRONTMATTER_KEYS):
        errors.append(f"{rel_md}: unexpected frontmatter key '{key}'")
    name = meta.get("name")
    if not isinstance(name, str) or not NAME_RE.match(name) or len(name) > MAX_NAME:
        errors.append(f"{rel_md}: 'name' must be lowercase letters, digits and single hyphens, max {MAX_NAME}")
    elif name != skill_dir.name:
        errors.append(f"{rel_md}: name '{name}' does not match folder '{skill_dir.name}'")
    elif name in names:
        errors.append(f"{rel_md}: duplicate skill name (also in {names[name]})")
    else:
        names[name] = rel_dir
    desc = meta.get("description")
    if not isinstance(desc, str) or not desc.strip():
        errors.append(f"{rel_md}: 'description' must be a nonempty string")
    elif len(desc) > MAX_DESCRIPTION:
        errors.append(f"{rel_md}: description exceeds {MAX_DESCRIPTION} characters")
    if not body.strip():
        errors.append(f"{rel_md}: instruction body is empty")

    check_openai_yaml(root, skill_dir, errors)
    return shared_block(body)


def shared_block(body: str) -> str | None:
    match = re.search(rf"^## {SHARED_BLOCK}\n(.*?)(?=^## )", body, re.S | re.M)
    return match.group(1).strip() if match else None


def iter_path_values(node):
    """Yield string values stored under keys that look like file references."""
    if isinstance(node, dict):
        for key, value in node.items():
            tokens = re.split(r"[_\-\s]+", str(key).lower())
            if isinstance(value, str) and any(t in PATH_KEY_TOKENS for t in tokens):
                yield str(key), value
            else:
                yield from iter_path_values(value)
    elif isinstance(node, list):
        for item in node:
            yield from iter_path_values(item)


def check_openai_yaml(root: Path, skill_dir: Path, errors: list[str]) -> None:
    path = skill_dir / "agents" / "openai.yaml"
    if not path.is_file() or path.is_symlink():
        return
    rel = path.relative_to(root).as_posix()
    if path.stat().st_size > MAX_YAML:
        errors.append(f"{rel}: exceeds {MAX_YAML} bytes")
    text = read_text(path, errors, rel)
    if text is None:
        return
    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError:
        errors.append(f"{rel}: malformed YAML")
        return
    if not isinstance(data, dict):
        errors.append(f"{rel}: must be a YAML mapping")
        return
    skill_root = skill_dir.resolve()
    for key, value in iter_path_values(data):
        target = (skill_dir / value).resolve()
        if os.path.isabs(value) or ".." in Path(value).parts or skill_root not in target.parents:
            errors.append(f"{rel}: '{key}' path escapes the skill directory")
        elif not target.is_file():
            errors.append(f"{rel}: '{key}' references a missing file")


def scan_for_secrets(root: Path, files: list[Path], errors: list[str]) -> None:
    for path in files:
        try:
            data = path.read_bytes()
        except OSError:
            continue
        if b"\x00" in data:
            continue
        rel = path.relative_to(root).as_posix()
        if rel.startswith(".git/"):
            continue
        for lineno, line in enumerate(data.decode("utf-8", "replace").splitlines(), 1):
            for kind, pattern in SECRET_PATTERNS.items():
                if pattern.search(line):
                    errors.append(f"{rel}:{lineno}: possible {kind} (value not shown)")


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    files = check_file_hygiene(root, errors)
    skills_root = root / "skills"
    if not skills_root.is_dir() or skills_root.is_symlink():
        return errors + ["skills/: directory is missing"]
    found = {p.name for p in skills_root.iterdir() if p.is_dir() and not p.is_symlink()}
    for stray in sorted(p.name for p in skills_root.iterdir() if not p.is_dir() and not p.is_symlink()):
        errors.append(f"skills/{stray}: unapproved file under skills/")
    for missing in sorted(EXPECTED_SKILLS - found):
        errors.append(f"skills/{missing}: expected skill directory is missing")
    for extra in sorted(found - EXPECTED_SKILLS):
        errors.append(f"skills/{extra}: unexpected skill directory for this release")

    names: dict[str, str] = {}
    blocks: dict[str, str] = {}
    for name in sorted(found & EXPECTED_SKILLS):
        block = check_skill(root, skills_root / name, errors, names)
        if block is None:
            errors.append(f"skills/{name}/SKILL.md: missing '## {SHARED_BLOCK}' section")
        else:
            blocks[name] = block
    if len(set(blocks.values())) > 1:
        errors.append(
            f"skills/: '## {SHARED_BLOCK}' differs between skills; edit all copies together"
        )
    scan_for_secrets(root, files, errors)
    return errors


def main(argv: list[str]) -> int:
    root = Path(argv[1] if len(argv) > 1 else ".").resolve()
    errors = validate(root)
    if errors:
        print(f"FAILED: {len(errors)} problem(s)")
        for line in errors:
            print(f"  - {line}")
        return 1
    print(f"OK: {len(EXPECTED_SKILLS)} skills validated")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
