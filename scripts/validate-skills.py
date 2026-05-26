#!/usr/bin/env python3
"""Validate canonical golden skills under ./skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

MANAGED_SKILLS = [
    "setup-matt-pocock-skills",
    "grill-with-docs",
    "zoom-out",
    "diagnose",
    "tdd",
    "prototype",
    "to-prd",
    "to-issues",
    "handoff",
    "write-a-skill",
    "improve-codebase-architecture",
    "triage",
    "review",
    "setup-pre-commit",
    "git-guardrails-claude-code",
]


def validate() -> list[str]:
    errors: list[str] = []

    for name in MANAGED_SKILLS:
        skill_dir = SKILLS / name
        skill_file = skill_dir / "SKILL.md"

        if not skill_file.exists():
            errors.append(f"missing SKILL.md: {name}")
            continue

        text = skill_file.read_text()
        frontmatter = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not frontmatter:
            errors.append(f"missing frontmatter: {name}")
            continue

        fm = frontmatter.group(1)
        found_name = re.search(r"^name:\s*(.+)$", fm, re.M)
        if not found_name:
            errors.append(f"missing name: {name}")
        elif found_name.group(1).strip() != name:
            errors.append(f"name mismatch: {name} -> {found_name.group(1).strip()}")

        if "description:" not in fm:
            errors.append(f"missing description: {name}")

        no_code = re.sub(r"```.*?```", "", text, flags=re.S)
        for link in re.findall(r"\]\(([^)]+)\)", no_code):
            if link.startswith(("http://", "https://", "#", "<")):
                continue
            target = (skill_dir / link).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"link escapes repo: {name} -> {link}")
                continue
            if not target.exists():
                errors.append(f"broken link: {name} -> {link}")

    unexpected = sorted(
        path.name
        for path in SKILLS.iterdir()
        if path.is_dir() and path.name not in MANAGED_SKILLS
    )
    for name in unexpected:
        errors.append(f"unexpected unmanaged skill directory: {name}")

    policy_checks = {
        "setup-pre-commit": [
            "Do not stage or commit unless the user explicitly asks you to.",
        ],
        "to-prd": [
            "Show the draft to the user and ask for approval before publishing",
        ],
        "triage": [
            "Before changing labels, closing an issue, posting `wontfix`, or marking `ready-for-agent`",
        ],
        "review": [
            "If sub-agents are not available",
        ],
    }

    for name, snippets in policy_checks.items():
        text = (SKILLS / name / "SKILL.md").read_text()
        for snippet in snippets:
            if snippet not in text:
                errors.append(f"missing policy snippet in {name}: {snippet}")

    forbidden_phrases = [
        "Stage all changed/created files",
        "then publish it to the project issue tracker",
        "### 4. Spawn both sub-agents in parallel",
    ]
    for skill_file in SKILLS.glob("*/SKILL.md"):
        text = skill_file.read_text()
        for phrase in forbidden_phrases:
            if phrase in text:
                errors.append(f"forbidden phrase in {skill_file}: {phrase}")

    return errors


def main() -> int:
    errors = validate()
    for error in errors:
        print(f"ERROR {error}")
    print(f"checked {len(MANAGED_SKILLS)} skills")
    print("status", "PASS" if not errors else "FAIL")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
