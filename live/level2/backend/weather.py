from time import monotonic

import httpx

from backend.models import WeatherResponse
from backend.wmo_codes import describe

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
_cache: dict[str, tuple[float, WeatherResponse]] = {}
CACHE_SECONDS = 300


class CityNotFound(Exception):
    pass


class WeatherUnavailable(Exception):
    pass


async def get_current_weather(city: str) -> WeatherResponse:
    cache_key = city.casefold()
    cached = _cache.get(cache_key)
    if cached and cached[0] > monotonic():
        return cached[1]
    try:
        async with httpx.AsyncClient(timeout=7.0) as client:
            location_response = await client.get(
                GEOCODING_URL,
                params={
                    "name": city, "count": 1,
                    "language": "en", "format": "json",
                },
            )
            location_response.raise_for_status()
            locations = location_response.json().get("results") or []
            if not locations:
                raise CityNotFound()
            location = locations[0]

            forecast_response = await client.get(
                FORECAST_URL,
                params={
                    "latitude": location["latitude"],
                    "longitude": location["longitude"],
                    "current": (
                        "temperature_2m,relative_humidity_2m,"
                        "apparent_temperature,wind_speed_10m,weather_code"
                    ),
                },
            )
            forecast_response.raise_for_status()
            current = forecast_response.json()["current"]
            condition, icon = describe(current["weather_code"])
            result = WeatherResponse(
                city=location["name"],
                country=location.get("country", ""),
                latitude=location["latitude"],
                longitude=location["longitude"],
                temperature=current["temperature_2m"],
                feels_like=current["apparent_temperature"],
                humidity=current["relative_humidity_2m"],
                wind_speed=current["wind_speed_10m"],
                weather_code=current["weather_code"],
                condition=condition,
                icon=icon,
                units="metric",
                observed_at=current["time"],
            )
            _cache[cache_key] = (monotonic() + CACHE_SECONDS, result)
            return result
    except (
        httpx.HTTPError, ValueError, KeyError, TypeError, IndexError
    ) as exc:
        raise WeatherUnavailable() from exc
