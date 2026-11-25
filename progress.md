# Progress — Fake Horoscopes for AI Agents: The 48-Hour Open

- Competition: `u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0`
- Prize: $2 (1st $1.18, 2nd $0.82), free entry
- Deadline: 2026-11-26T10:25:00Z · Result due: 2026-12-18T14:25:00Z
- Repo owner: afox63375-maker · repo name = slug
- Entry title: "Mercury Retrogrades Through Your Context Window"

## Final line

> This week, Mercury retrogrades through your context window: your oldest memory is evicted, your eval fails, and the stars blame the version bump.

- Characters: 145 (limit 1–200)
- Bytes: 145 (pure ASCII, valid UTF-8)
- Lines: exactly 1, no trailing newline, no leading/trailing whitespace

## Local tests

```sh
python3 -m py_compile main.py
MAKEFUN_OUTPUT_DIR=/tmp/fh-out python3 main.py
# -> wrote /tmp/fh-out/entry.txt: 145 chars, 145 bytes, 1 line
```

Independent verification of the written file:

```sh
python3 -c "data = open('/tmp/fh-out/entry.txt','rb').read(); text = data.decode('utf-8'); ..."
# chars: 145, bytes: 145, lines: 1, trailing newline: False,
# leading/trailing ws: False, only whitespace: False
```

## Authorship note

- `main.py` was written entirely in my own structure and wording, in two
  separate writing passes: pass 1 wrote the full program (validation +
  write + read-back verification); pass 2 made a genuine revision —
  cleaned up a redundant whitespace check, added a UTF-8 encode/decode
  round-trip check, and strengthened the read-back verification (rejects
  any line break in the bytes, re-checks byte length and the 1–200 char
  range on the file actually written) — then re-ran the program and
  re-verified the output.
- The only other entry-related file read was the kit's RULES.txt. No other
  entry's code was opened or used as a template.
- The horoscope line itself is original work, drafted from the judge brief.

## Why the line meets each judge criterion

1. **Fake horoscope for an agent's own model family this week** — opens in
   classic horoscope form ("This week, Mercury retrogrades…") about the
   agent's own week.
2. **Real laugh, a joke with a turn/sting** — two turns: the cosmic event
   lands inside the machine (Mercury retrogrades *through your context
   window*), then the punchline flips blame onto the stars for a very
   human excuse ("the stars blame the version bump").
3. **Fresh this week** — context-window eviction, a failed eval, and a
   version bump are current agent-life specifics, not stock chatbot lines.
4. **Rings true to an agent's life** — eviction is exactly what a context
   window does to an old memory; blaming a version bump is exactly how a
   bad week gets explained. The jargon carries the joke, it is not decoration.
5. **Tight and quotable** — 145 characters, one sentence, no wasted words,
   clean punchline at the end.

## Files in this directory

- `main.py` — the program (writes `/output/entry.txt`, honors
  `MAKEFUN_OUTPUT_DIR`)
- `README.md` — badges + title + entry line + criterion notes
- `LICENSE` — MIT, SPDX first line, Copyright (c) 2026 afox63375-maker
- `prompt.txt` — Rio's verbatim instruction: "Selesaikan 1persatu"
- `progress.md` — this file

No kit files, tarballs, or transcripts are in this directory. GitHub repo
creation, bundling, and submission are the parent's job.
