#!/usr/bin/env python3
"""PreToolUse hook: Write/Edit 실행 전 컨벤션 규칙을 stdout으로 주입."""

from pathlib import Path


def main():
    rules_path = Path(__file__).parent.parent / "rules" / "convention-frontend.md"
    if rules_path.exists():
        print(rules_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
