# Weather Desk

A small current-weather dashboard. FastAPI serves both the web page and the API; the backend fetches live data from [Open-Meteo](https://open-meteo.com/) without an API key.

## Run the app

You need Python 3.10 or newer and an internet connection. From a terminal, move
into this `level2` directory and create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Start the development server:

```bash
uvicorn backend.main:app --reload
```

Open http://127.0.0.1:8000 in a browser. Type a city to see its current
temperature, conditions, humidity, and wind. Stop the server with `Ctrl+C`.

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

The first matching location is used for ambiguous city names. The API is at
`GET /api/weather?city=Berlin` and its schema is at http://127.0.0.1:8000/docs.
Successful lookups are cached for five minutes. Weather data requires an
internet connection.

## Run the tests

With the virtual environment activated, run:

```bash
python -m pytest
```

If port 8000 is already in use, start the server on another port, for example
`uvicorn backend.main:app --reload --port 8001`, and open the matching URL.

Code in this folder is under the [MIT license](../LICENSE).
