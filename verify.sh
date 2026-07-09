#!/usr/bin/env bash
# Bootstrap the venv (first run) and run the tests + coverage.
set -e
cd "$(dirname "$0")"
if [ ! -d .venv ]; then
  echo "Creating venv + installing pytest/coverage..."
  python3 -m venv .venv
  .venv/bin/python -m pip install --quiet --upgrade pip
  .venv/bin/python -m pip install --quiet pytest pytest-cov coverage
fi
.venv/bin/python -m pytest "$@"
