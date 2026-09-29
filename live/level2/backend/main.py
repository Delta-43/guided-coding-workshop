from pathlib import Path

from fastapi import FastAPI
from fastapi import HTTPException, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from backend.models import WeatherResponse
from backend.weather import (
    CityNotFound,
    WeatherUnavailable,
    get_current_weather,
)

app = FastAPI(title="Weather Dashboard")
FRONTEND = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/assets", StaticFiles(directory=FRONTEND), name="assets")


@app.get("/", include_in_schema=False)
def index() -> FileResponse:
    return FileResponse(FRONTEND / "index.html")


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/weather", response_model=WeatherResponse)
async def weather(city: str = Query(min_length=1)) -> WeatherResponse:
    city = city.strip()
    if not city:
        raise HTTPException(status_code=422, detail="Enter a city name")
    try:
        return await get_current_weather(city)
    except CityNotFound as exc:
        raise HTTPException(status_code=404, detail="City not found") from exc
    except WeatherUnavailable as exc:
        raise HTTPException(
            status_code=502, detail="Weather service unavailable"
        ) from exc
