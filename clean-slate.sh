#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# clean-slate.sh — reset the demo repo to a pristine, history-free state.
#
# Wipes the entire git history from the build/test session (all our commits and
# branches), restores the demo's state files to their "before first run" values,
# clears caches, and re-initialises a fresh repo with ONE clean baseline commit.
#
# Keeps: src/, the original tests, pyproject.toml, .gitignore, .venv, all docs
#        and helper scripts, and the _solutions/ demo kit.
# Resets: PROGRESS.md + outputs/coverage-plan.md, and removes any tests copied
#         into tests/ during a demo run.
#
# Want ZERO commits instead of one baseline? Comment out the `git commit` line
# near the bottom — you'll get a fresh repo with everything staged, uncommitted.
# ---------------------------------------------------------------------------
set -e
cd "$(dirname "$0")"

# safety guard: only run inside this demo repo
if [ ! -f TASK.md ] || [ ! -f LOOP_INSTRUCTIONS.md ]; then
  echo "Refusing to run: this doesn't look like the claude-loops-demo repo." >&2
  exit 1
fi

echo "Cleaning the demo repo to a pristine, history-free baseline..."

# 1) remove tests copied/written into tests/ during a demo run (keep the originals)
rm -f tests/test_parser.py tests/test_api.py tests/test_aggregate_full.py \
      tests/test_normalize_edges.py tests/test_theater.py

# 2) clear caches / coverage / rendered artifacts (never .venv)
rm -rf .pytest_cache __pycache__ */__pycache__ .coverage .coverage.* coverage.xml htmlcov

# 3) restore the state files to their "before first run" content
cat > PROGRESS.md <<'EOF'
# Loop Progress — Test-Coverage Loop

## Current State
- Status: Manual testing (not yet scheduled)
- Goal: 90% overall coverage
- Current overall coverage: 55%
- Next target: `src/parser.py` (0%, unit tests)
- Last updated: (before first run)

## Coverage Ledger
| File             | Coverage | Kind        | Status       | Notes                                 |
|------------------|----------|-------------|--------------|---------------------------------------|
| src/sentiment.py | 100%     | unit        | DONE         |                                       |
| src/normalize.py | 84%      | unit        | IN PROGRESS  | None-guard + drop_* branches untested |
| src/aggregate.py | 55%      | unit        | IN PROGRESS  | top_channel, summary untested         |
| src/parser.py    | 0%       | unit        | TODO (next)  | parse / parse_many / to_dict untested |
| src/api.py       | 0%       | integration | TODO         | MentionsService ingest/report/reset   |

## Last Run
- Date:
- Trigger:
- Summary:

## Open Items
- Reach 90% overall (currently 55%).

## Needs Human Review
- None yet.

## Next Run Should
- Read this ledger, run coverage, and recommend tests for `src/parser.py`.
- Do not write tests yet (Phase A / recommend-only).

## Decisions Made
- Loop starts recommend-only (Permission Ladder rung 1).
- Writing tests is draft-PR + human approval only; never auto-merge.

## Do Not Repeat
- Do not modify `src/` to inflate coverage.
- Do not add tests that assert nothing ("coverage theater").
EOF

cat > outputs/coverage-plan.md <<'EOF'
# Coverage Plan

No loop run has been completed yet.
EOF

# 4) wipe ALL git history and branches from our session
rm -rf .git

# 5) fresh repo + one clean baseline commit (uses your git identity)
git init -q
git config user.name  "$(git config --global user.name  2>/dev/null || echo 'Ahmed Hashem')"
git config user.email "$(git config --global user.email 2>/dev/null || echo 'aahashim01@gmail.com')"
git add -A
git commit -q -m "baseline: mentions-analytics demo at 55% coverage + test-coverage loop"

echo
echo "Done. History wiped; one clean baseline commit:"
git log --oneline
echo
git status --short >/dev/null && echo "Working tree: clean"
if [ -x .venv/bin/python ]; then
  echo "Baseline coverage:"; .venv/bin/python -m pytest 2>&1 | grep -E "^TOTAL|passed" || true
fi
