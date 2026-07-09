# Test-Coverage Loop

## Goal
Drive this project's automated test coverage toward **90%**, one file at a time,
without ever shipping tests that do not actually verify behavior.

## Expected Output
Each run produces or updates:
- `outputs/coverage-plan.md` — the short recommendation for the next target
- `PROGRESS.md` — the coverage ledger (current %, per-file status, next target)

## Scope (starts read-only — Permission Ladder rung 1)
- The loop may READ any file in this project and RUN the test/coverage command.
- In its first phase it only WRITES `outputs/coverage-plan.md` and `PROGRESS.md`.
  It does NOT write tests or modify source yet.
- Writing tests is unlocked later (see `LOOP_INSTRUCTIONS.md` → Phase B), and only
  ever as a **draft pull request** for human approval — never merged automatically.

## Definition of Done
Overall coverage ≥ 90% AND no "coverage theater" — every added test asserts real behavior.
