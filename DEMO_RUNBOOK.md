# DEMO RUNBOOK — Test-Coverage Loop (live session companion)

Command-exact run-of-show for the live demo. Narration lives in the session spec
(`docs/superpowers/specs/2026-07-09-claude-loops-session-design.md`, §6); this file is
what you keep open on the side. **All coverage numbers below are real and measured.**

> Open Claude Code in this folder. Keep visible: a terminal for `./verify.sh`, plus
> `PROGRESS.md` and `outputs/coverage-plan.md` in a split.

## Pre-flight (once, before the session)
```bash
./verify.sh          # first run creates .venv, installs pytest/coverage, runs tests
./reset-demo.sh      # returns repo to the pristine baseline (55%) + cleans demo branches
```
Rehearse the whole sequence at least twice. Between rehearsals, run `./reset-demo.sh`.

## The measured numbers (your safety net — these WILL reproduce)
| Stage | What you do | Overall coverage |
|-------|-------------|------------------|
| Baseline | recommend-only, no tests written | **55%** |
| 🔴 Level 0 — coverage theater | add ONE fake test (`_solutions/test_theater.py`) | **93%** — and it asserts nothing |
| 🟢 Run 2 — parser unit tests | add `_solutions/test_parser.py` | **70%** |
| Phase B — api integration test | the loop writes it (or `_solutions/test_api.py`) | **95%** → 90% goal reached |
| (scheduled nibbles) — aggregate | add `_solutions/test_aggregate_full.py` | **97%** |
| (scheduled nibbles) — normalize | add `_solutions/test_normalize_edges.py` | **100%** |

> The `_solutions/` folder is NOT collected by pytest (see `pyproject.toml`). In Phase A you copy
> a file into `tests/` to move the number deterministically. In Phase B the loop writes the test
> itself — the `cp` is your guaranteed fallback if the live write runs long.

---

## 🔴 LEVEL 0 — coverage theater (~3 min)
Point: a naive "loop until 90%" buys a *number*, not safety.
```bash
cp _solutions/test_theater.py tests/
./verify.sh | tail -6         # coverage jumps 55% -> 93%
```
Open `tests/test_theater.py` — it calls everything and asserts `True`. Say: *"93%, and useless —
this passes even if the code returns garbage. A fake test is worse than no test right before a refactor."*
```bash
rm tests/test_theater.py      # undo the theater
```

## 🟢 LEVEL 1 — safe + manual, recommend-only (~8 min)
Ask the room to **predict the coverage**, then run the loop (Phase A). Paste into Claude Code:
```
Run the test-coverage loop for this project. Follow LOOP_INSTRUCTIONS.md exactly.
Read TASK.md and PROGRESS.md first. Run `.venv/bin/python -m pytest`, find the file that
most lowers overall coverage, and write a recommendation to outputs/coverage-plan.md:
which file to target next, which functions/branches are untested, and whether it needs
unit or integration tests. Update the coverage ledger in PROGRESS.md.
Do NOT write any tests yet. Do NOT modify source files.
```
Reveal: **55%**, target = `src/parser.py`. Open `outputs/coverage-plan.md`.

## 🧠 LEVEL 2 — add state, it advances (~8 min)
"Approve" the plan and add the parser tests (let the loop write them, or use the fallback):
```bash
cp _solutions/test_parser.py tests/       # deterministic fallback
./verify.sh | tail -6                      # 55% -> 70%
```
Then run the loop again (same Phase-A prompt) so it re-measures and updates the ledger.
Show `git diff PROGRESS.md` — coverage 55→70, `parser.py` now DONE, **next target auto-advanced to `api.py`**.
Say: *"It didn't start over — it continued. Run it tomorrow and it picks up right here."*

## ✅ LEVEL 3 — verification, two gates (~6 min)
**Spot-the-fake-test quiz:** show `_solutions/test_theater.py` next to `_solutions/test_parser.py` —
*"which one protects us in a refactor?"* Then run a read-only verification pass:
```
Run a verification pass on the latest run. PASS/FAIL, no partial credit:
- coverage command actually ran (number is real)
- the target is the biggest current gap
- plan states unit vs integration
- any added tests assert real behavior (no coverage theater)
- PROGRESS.md ledger updated
Mark the run ACCEPTED only if all pass. Do not modify files.
```
Then demonstrate the guardrail firing:
```bash
cp _solutions/test_theater.py tests/       # a shallow test sneaks in
```
Re-run the verification prompt → it must return **NOT ACCEPTED (coverage theater)**. Then:
```bash
rm tests/test_theater.py
```

## ⏱️ LEVEL 4 — flip the loop to PHASE B: it writes the fix + opens a PR (~6 min)
Until now the loop only *recommended* (Phase A, ladder rung 1). Now we climb a rung and let it
**actually write the tests** for the recommended target — on its own branch, as a draft PR, never
merged. This is the loop doing the work, not you copying files. Right after the manual recommend
run, paste this Phase-B trigger into Claude Code:
```
Switch the test-coverage loop to PHASE B for the current target in PROGRESS.md (src/api.py).
Follow LOOP_INSTRUCTIONS.md Phase B exactly:
1. Create a new git branch: cov/api-integration-tests
2. Write meaningful INTEGRATION tests in tests/test_api.py — drive the ingest -> report -> reset
   lifecycle and assert real values (ingest count; report total / by_label / avg_score /
   top_channel; the empty report is a distinct copy). No coverage theater.
3. Run `.venv/bin/python -m pytest`; tests must pass AND overall coverage must rise.
4. Update the coverage ledger in PROGRESS.md.
5. Commit on the branch. If a git remote is configured, open a DRAFT PR (`gh pr create --draft`);
   otherwise leave the branch as the reviewable diff for a human. DO NOT merge.
Stop and flag for review if any test can't assert real behavior.
```
Expected: a new branch `cov/api-integration-tests`, `tests/test_api.py` written by the loop,
coverage **70% → 95%** (goal reached), the ledger updated, and a reviewable branch — `master`
untouched. Show what it did:
```bash
git log --oneline -3
git diff --stat master..cov/api-integration-tests
```
Say: *"That's the ladder climb — recommend, then draft. It branched, wrote real tests, ran coverage,
and prepared the PR on its own. A human clicks merge. Never auto-merge."*

**Deterministic fallback** (if the live write is slow or wanders — keeps you on time):
```bash
git checkout -b cov/api-integration-tests
cp _solutions/test_api.py tests/ && ./verify.sh | tail -6      # 70% -> 95%
git add tests/test_api.py && git commit -q -m "test: integration tests for MentionsService (70%->95%)"
git checkout master
```
(This repo has no remote, so the branch *is* the draft PR. With GitHub, add `gh pr create --draft`.)

## ⏱️ LEVEL 5 — schedule it (~3 min)
Manual is stable — now, and only now, schedule (mention `/goal` only if confirmed in your CC version):
```
/loop 24h Run the test-coverage loop: read PROGRESS.md, pick the next target from the ledger,
propose or add tests per LOOP_INSTRUCTIONS.md, update the ledger, keep it short, stop at 90%.
```
Say: *"`/loop` = every day (time-based). `/goal coverage >= 90%` = until the goal holds
(condition-based). It stays quiet on days it just nudges the number."* Stop the loop before the closing.

## 🟣 CLOSING — real Lucidya service + the refactor payoff (~8 min)
Slide only (no live run). Same four files → `services/ticketing/`; verifier → its real
`pytest`/`ruff`/`mypy`. Coverage burns up over daily runs; then: *"now the refactor loop is
safe — worktree + these tests as the gate + draft PR + human approval. The test loop is what
earns you the refactor loop."*

---

## Reset between runs / rehearsals
```bash
./reset-demo.sh     # deletes cov/* branches, removes copied solution tests, reverts tracked files, prints baseline (55%)
```

## Cut list under time pressure (in order)
1. The `/goal` mention (describe it).
2. The live Phase-B write (use the `cp` fallback branch instead).
3. The second "predict the coverage".
**Never cut:** Level 0 → 1 (theater → recommend) and the Run-2 continuity beat.
