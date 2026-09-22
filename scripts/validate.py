#!/usr/bin/env python3
"""Validate the public Yitong PPT skill without external dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_frontmatter() -> str:
    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        fail("SKILL.md must start with YAML frontmatter")
    frontmatter = text.split("---", 2)[1]
    name_match = re.search(r"^name:\s*([a-z0-9-]+)\s*$", frontmatter, re.MULTILINE)
    description_match = re.search(r'^description:\s*["\'](.+)["\']\s*$', frontmatter, re.MULTILINE)
    if not name_match or name_match.group(1) != "yitong-ppt":
        fail("frontmatter name must be yitong-ppt")
    if not description_match or not description_match.group(1).strip():
        fail("frontmatter description must be non-empty")
    return text


def validate_links(skill_text: str) -> None:
    for target in re.findall(r"\]\(([^)]+)\)", skill_text):
        if "://" in target or target.startswith("#"):
            continue
        path = ROOT / target.split("#", 1)[0]
        if not path.exists():
            fail(f"missing referenced file: {target}")


def validate_agent_metadata() -> None:
    metadata = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
    if "$yitong-ppt" not in metadata:
        fail("agents/openai.yaml must invoke $yitong-ppt")


def validate_privacy() -> None:
    macos_home = "/" + "Users/"
    linux_home = "/" + "home/"
    forbidden = [
        re.compile(r"[A-Za-z]:\\\\"),
        re.compile(re.escape(macos_home) + r"[^/\s]+/"),
        re.compile(re.escape(linux_home) + r"[^/\s]+/"),
    ]
    suffixes = {".md", ".yaml", ".yml", ".json", ".py", ".txt"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in suffixes:
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in forbidden:
            if pattern.search(text):
                fail(f"possible private absolute path in {path.relative_to(ROOT)}")


def main() -> None:
    skill_text = validate_frontmatter()
    validate_links(skill_text)
    validate_agent_metadata()
    validate_privacy()
    print("Yitong PPT validation passed.")


if __name__ == "__main__":
    main()
