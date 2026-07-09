# Loop Instructions — Test-Coverage Loop

You are running a test-coverage loop on this project.

## Before You Start (Context)
1. Read `TASK.md`.
2. Read `PROGRESS.md` (the coverage ledger) — especially "Next target" and "Do Not Repeat".
3. Run the coverage command and read the result:
   `.venv/bin/python -m pytest`   (coverage prints automatically)

## Action — What You Should Do
### Phase A — Recommend only (default, safest rung)
1. From the coverage report, identify the file that most lowers overall coverage.
2. Write a SHORT recommendation to `outputs/coverage-plan.md`:
   - the next target file and its current coverage,
   - the specific untested functions / branches (use the "Missing" column),
   - whether it needs **unit** tests (pure functions) or **integration** tests
     (crosses modules, e.g. `api.py`),
   - one line on what a *meaningful* assertion would check (not just "call it").
3. Update the coverage ledger in `PROGRESS.md`.
4. DO NOT write tests or modify source in this phase.

### Phase B — Write tests (only when the run prompt explicitly allows it)
1. Work on ONE target file only.
2. Create tests in a NEW git branch (never on the main branch).
3. Tests must assert real behavior — see "Two Gates". No coverage theater.
4. Run `.venv/bin/python -m pytest`. Tests must pass AND coverage for the target must rise.
5. Open a **draft** pull request summarizing the change. DO NOT merge.
6. If you cannot write a safe, meaningful test, stop and mark it for human review.

## Verification — Two Gates (checker phase)
A run is ACCEPTED only if BOTH pass:
- **Gate 1 — the number:** the coverage command actually ran; the reported number is real, not guessed.
- **Gate 2 — the quality:** any added test asserts real behavior. A test that executes
  code but asserts nothing (`assert True`, or never checks the result) is "coverage
  theater" and must be REJECTED even if coverage went up.

Run the checklist, return PASS/FAIL per item, no partial credit:
- [ ] coverage command was run (number is real)
- [ ] the recommended target is the biggest current gap
- [ ] the plan states unit vs integration for the target
- [ ] (Phase B) added tests assert real behavior — no coverage theater
- [ ] `PROGRESS.md` ledger updated (current %, next target)
- [ ] (Phase A) no tests or source files were modified

## Safety Rules
- Phase A: only write `outputs/coverage-plan.md` and `PROGRESS.md`.
- Never modify files under `src/` to make coverage go up.
- Never delete or weaken existing tests.
- Never edit files outside this project.
- If unsure whether an action is allowed, stop and ask for human review.

## Stop Conditions & Failure Policy
- **Iteration cap:** at most 2 attempts per run. If verification still fails, stop and
  mark the run "Needs human review" in `PROGRESS.md`.
- If overall coverage ≥ 90% (the goal), switch to **quiet mode**: make at most one small
  improvement or write "No meaningful gap left" — do not manufacture work.
- If the same target fails twice across runs, escalate to human review.

## Scheduled Run Policy
- `/loop 24h` — pick the next target from the ledger, do one file, keep the report short.
- `/goal coverage >= 90%` — keep going (one target per iteration) until the goal holds, then stop.
- On a run with no meaningful change, update the ledger quietly and stop.

## State Update Rule
Before ending EVERY run, update `PROGRESS.md`:
- current overall coverage, per-file coverage/status,
- the target just worked on and the next target,
- anything needing human review.
If you cannot update `PROGRESS.md`, stop and report why.
