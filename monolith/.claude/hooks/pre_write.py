#!/usr/bin/env python3
"""PreToolUse hook: Write/Edit 대상 파일 경로를 감지하여 적절한 컨벤션을 주입."""

import json
import sys
from pathlib import Path


def main():
    try:
        tool_input = json.loads(sys.stdin.read())
        file_path = tool_input.get("file_path", "")
    except (json.JSONDecodeError, KeyError):
        file_path = ""

    rules_dir = Path(__file__).parent.parent / "rules"

    if "/backend/" in file_path or file_path.endswith(".py"):
        rules_file = rules_dir / "convention-backend.md"
    elif "/frontend/" in file_path or file_path.endswith((".tsx", ".ts", ".jsx", ".js")):
        rules_file = rules_dir / "convention-frontend.md"
    else:
        return

    if rules_file.exists():
        print(rules_file.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
