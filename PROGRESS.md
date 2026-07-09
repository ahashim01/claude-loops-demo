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
