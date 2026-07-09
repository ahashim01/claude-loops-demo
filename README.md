# mentions-analytics (demo project)

A tiny, self-contained **mock** social-mentions analytics library used as the sample
project for the **Claude Loops** team session. It is *not* Lucidya code — it just
looks the part (mentions, sentiment, channels) so the demo feels familiar.

The project deliberately ships with **partial test coverage**. The session's loop
drives it toward 90%, one file at a time.

## Layout
```
src/
  sentiment.py   # score / label text            (well tested)
  normalize.py   # clean mention text            (well tested)
  aggregate.py   # counts, averages, summaries   (partly tested)
  parser.py      # raw payload -> Mention         (untested — unit target)
  api.py         # MentionsService (ties it all)  (untested — integration target)
tests/
```

## Run the tests + coverage
```bash
.venv/bin/python -m pytest          # coverage prints automatically
```

See `TASK.md`, `LOOP_INSTRUCTIONS.md`, `PROGRESS.md` for the loop that improves this
project's coverage, and `DEMO_RUNBOOK.md` for the live session run-of-show.
