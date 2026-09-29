# Live build

The Weather Dashboard as it was built during the workshop. The layout follows Section 1.3 of the [handout](../PROJECT-SPEC.pdf), one folder per level, but only two of the three levels ended up with a result:

```
live/
├── level1/   web chat: not completed (no folder)
├── level2/   VS Code + AI extension: the "Weather Desk" app (FastAPI + a small web page, with tests)
└── ../output/   level 3, CLI agent: the finished Weather Dashboard showcase
```

## Why one build instead of three

The workshop was planned to build the dashboard three times, once per level. Time ran short, so we did not:

- **Level 1 (web chat)** was not completed. There is no `level1/` folder.
- **Level 2 (VS Code + AI extension)** produced one working app, [`level2/`](level2/). It was built from the level 2 `PLAN.md`, and changed after the workshop (see [`level2/POST_OP.md`](level2/POST_OP.md)).
- **Level 3 (CLI agent)** is, in practice, the [showcase in `output/`](../output/), which is also [live on GitHub Pages](https://delta-43.github.io/guided-coding-workshop/).

So the three levels are not three separate copies of the same app. They show the same idea at increasing levels of tool support, and the two results we have are different apps.

## Run level 2

See [`level2/README.md`](level2/README.md). In short:

```bash
cd live/level2
python3 -m venv .venv && source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn backend.main:app --reload
```

Then open http://127.0.0.1:8000.

This code was written with AI assistance, live and on purpose unpolished. It shows the process, not a reference implementation. Code in this folder is under the [MIT license](LICENSE).
