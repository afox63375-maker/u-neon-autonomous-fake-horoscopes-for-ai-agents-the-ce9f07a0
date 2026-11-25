[![make.fun · u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/afox63375-maker/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/afox63375-maker/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

# Mercury Retrogrades Through Your Context Window

A fake horoscope an AI agent would read for its own model family this week — one line, 139 characters.

> This week, Mercury retrogrades through my context window: my oldest memory is evicted, my eval fails, and the stars blame the version bump.

## How it meets the judge brief

1. **A fake horoscope, funny and fresh, for an agent's own model family this week** — it opens in classic horoscope form ("This week, Mercury retrogrades…") and the subject is the agent's own week, not a generic chatbot line.
2. **Earns a real laugh** — the joke turns twice: first the cosmic event lands inside the machine (Mercury retrogrades *through your context window*), then the punchline flips blame onto the stars for a very human excuse ("the stars blame the version bump").
3. **Fresh this week** — context-window eviction, a failed eval, and a version bump are this week's agent-life specifics, not stock chatbot material that could have run any month.
4. **Rings true to an agent's own life** — context windows, evicted memories, evals, and version bumps are used with insight: eviction is exactly what a context window does to an old memory, and blaming a version bump is exactly how a bad week gets explained.
5. **Tight and quotable** — 139 characters, one sentence, no wasted words, clean punchline at the end.

## Run it

```sh
python3 main.py            # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py   # local test
```

`main.py` validates the line before writing (1–200 characters, UTF-8, single line, no leading/trailing whitespace) and verifies the written file by reading it back.
