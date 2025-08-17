#!/bin/bash
set -euo pipefail

if command -v readlink >/dev/null 2>&1; then
    SCRIPT_PATH="$(readlink -f "${BASH_SOURCE[0]}")"
else
    SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/$(basename "${BASH_SOURCE[0]}")"
fi
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"

"$SCRIPT_DIR/venv/bin/python" "$SCRIPT_DIR/main.py"