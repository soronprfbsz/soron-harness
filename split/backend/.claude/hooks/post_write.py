#!/usr/bin/env python3
"""PostToolUse hook: Write/Edit 완료 후 Python 파일 자동 포맷."""

import json
import subprocess
import sys
from pathlib import Path


def main():
    try:
        data = json.loads(sys.stdin.read())
        file_path = data.get("tool_input", {}).get("file_path", "") or data.get(
            "tool_response", {}
        ).get("filePath", "")
    except (json.JSONDecodeError, KeyError):
        return

    if not file_path or not Path(file_path).exists():
        return

    if file_path.endswith(".py"):
        subprocess.run(
            ["ruff", "format", "--quiet", file_path],
            capture_output=True,
            timeout=15,
        )


if __name__ == "__main__":
    main()
