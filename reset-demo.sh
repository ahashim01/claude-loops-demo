#!/usr/bin/env bash
# Restore the repo to the pristine "before the demo" state so you can re-run it.
# Removes any solution/theater tests copied into tests/ and reverts tracked files.
set -e
cd "$(dirname "$0")"
git checkout master 2>/dev/null || true
git branch --format="%(refname:short)" | grep -E "^cov/" | xargs -r git branch -D >/dev/null 2>&1 || true
rm -f tests/test_parser.py tests/test_api.py \
      tests/test_aggregate_full.py tests/test_normalize_edges.py \
      tests/test_theater.py
git checkout -- PROGRESS.md outputs/ src/ tests/ 2>/dev/null || true
git clean -fdq tests/ outputs/ 2>/dev/null || true   # drop any loop-written untracked files
echo "Reset done. Baseline coverage:"
.venv/bin/python -m pytest 2>&1 | grep -E "^TOTAL|passed" || true
