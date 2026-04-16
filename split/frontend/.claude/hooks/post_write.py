#!/usr/bin/env python3
"""PostToolUse hook: Write/Edit 완료 후 TS/JS 파일 자동 린트."""

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

    if file_path.endswith((".ts", ".tsx", ".js", ".jsx")):
        # split 구조: 프로젝트 루트가 곧 frontend
        project_root = Path(__file__).parent.parent.parent
        subprocess.run(
            ["npx", "eslint", "--fix", file_path],
            cwd=str(project_root),
            capture_output=True,
            timeout=30,
        )


if __name__ == "__main__":
    main()
