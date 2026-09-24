# Live build

The Weather Dashboard as it gets built during the workshop, one folder per level. The layout follows Section 1.3 of the [handout](../materials/PROJECT-SPEC.pdf):

```
live/
├── level1/   web chat: files created and pasted by hand
├── level2/   VS Code + AI extension, with PLAN.md and MEMORY.md
└── level3/   CLI agent, with AGENTS.md and TASKS.md
```

Each level has `backend/` (FastAPI) and `frontend/` (a single `index.html`). To run one, see Section 1.4 of the handout. In short:

```bash
# terminal 1
cd live/level1/backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

# terminal 2
cd live/level1/frontend
python3 -m http.server 5500
```

Then open http://localhost:5500.

This code was written with AI assistance, live and on purpose unpolished. It shows the process, not a reference implementation. Code in this folder is under the [MIT license](LICENSE).
