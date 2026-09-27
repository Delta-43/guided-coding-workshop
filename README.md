# Guided Coding Workshop

**Code with more than just vibes.** This hands-on workshop builds one tiny full-stack app three times, each time with a more capable kind of AI assistance:

| Level | Workflow | What changes |
|---|---|---|
| 01 | **Web chat** | The AI only writes text; you create, paste and run everything yourself. |
| 02 | **Editor + memory** | The AI lives in VS Code; `PLAN.md` and `MEMORY.md` give it a memory; OpenRouter lets you switch models. |
| 03 | **CLI agents** | An agent in the terminal reads and writes files and runs commands, guided by `AGENTS.md`. |

**Live showcase:** [delta-43.github.io/guided-coding-workshop](https://delta-43.github.io/guided-coding-workshop/). This is where the app can go: search any city for its weather, a 24-hour chart, a 7-day outlook, and a live contour map of the terrain.

The app is a **Weather Dashboard**: a Python (FastAPI) backend that fetches current weather from [Open-Meteo](https://open-meteo.com) (free, no API key), and a single-page React frontend with a search box and a result card.

The habits underneath all three levels matter as much as the tools: plan before code, one file at a time, and the debugging loop (run → copy the exact error → paste it back → re-run).

## What's in here

```
PROJECT-SPEC.pdf       Participant handout: get-ready guide, spec, step-by-step levels, prompts, fixes
POSTER.pdf             Event poster (A4)
SLIDES.html            Shortcut: opens the slide deck
materials/
├── FREE-AGENT-SETUP.pdf  Side guide: a free AI coding agent (Kilo Code, Cline or Cursor Hobby + OpenRouter free models)
└── slides/            Slide deck: open index.html in a browser
live/                  The app as built live during the workshop, one folder per level
output/                The finished showcase dashboard (static, published on GitHub Pages)
```

## Participants: start here

1. Open **[`PROJECT-SPEC.pdf`](PROJECT-SPEC.pdf)** and work through **Section 00 – Get ready** *before* the workshop (30–45 minutes). It covers Windows (WSL2 + Ubuntu), Linux and macOS, VS Code, Python, Node.js, and the accounts you'll need.
2. On the day, follow Sections 01–05. Build in your own `~/guided-coding` folder, as the handout describes. You don't need to clone this repo to take part.
3. Want to compare against the instructor's version afterwards? Look in [`live/`](live/).

No paid AI plan yet? **[`materials/FREE-AGENT-SETUP.pdf`](materials/FREE-AGENT-SETUP.pdf)** sets up a free coding agent (Kilo Code, Cline or Cursor's free plan, with OpenRouter's free models) that you can use for Levels 2 and 3.

## Presenting the slides

Open `SLIDES.html` (or `materials/slides/index.html`) in a browser; it needs an internet connection the first time (React and the fonts load from a CDN). There's no build step.

| Key | Action |
|---|---|
| → / Space / Page Down | Next slide |
| ← / Page Up | Previous slide |
| Home / End | First / last slide |
| F | Fullscreen |

The URL keeps the slide number (`index.html#8`), so reloading keeps your place.

## Credits

- The "Four Ps" mindset is adapted from Darren Coxon's *[The Four Ps of Vibe Coding](https://darrencoxon.substack.com/p/the-four-ps-of-vibe-coding)*.
- The product-maturity ladder is adapted from FreshVanRoot's *[Levels of VibeCoding](https://freshvanroot.com/blog/levels-of-vibecoding/)*.
- The prompt / context / harness slides draw on Caleb Writes Code's *[Agent Harness explained in 8min](https://youtu.be/1a1VXDdIyrk)*.
- Weather data: [Open-Meteo](https://open-meteo.com).
- Typefaces: [Anton](https://fonts.google.com/specimen/Anton) and [JetBrains Mono](https://www.jetbrains.com/lp/mono/) (SIL Open Font License), loaded from Google Fonts.

## License

- **Workshop materials** (everything except `live/`): [CC BY-NC 4.0](LICENSE). You're welcome to reuse and adapt them for non-commercial workshops, with credit.
- **Code in `live/`**: [MIT](live/LICENSE).

Part of [Delta-43/workshops](https://github.com/Delta-43/workshops).
