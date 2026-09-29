import pytest
import respx
from httpx import Response

from backend.weather import (
    FORECAST_URL,
    GEOCODING_URL,
    CityNotFound,
    WeatherUnavailable,
    _cache,
    get_current_weather,
)


@pytest.fixture(autouse=True)
def clear_cache():
    _cache.clear()


@pytest.mark.asyncio
@respx.mock
async def test_weather_lookup_and_cache():
    geocode = respx.get(GEOCODING_URL).mock(return_value=Response(200, json={
        "results": [{
            "name": "Berlin", "country": "Germany",
            "latitude": 52.52, "longitude": 13.41,
        }],
    }))
    forecast = respx.get(FORECAST_URL).mock(return_value=Response(200, json={
        "current": {
            "temperature_2m": 18.3, "apparent_temperature": 17.1,
            "relative_humidity_2m": 62, "wind_speed_10m": 11.2,
            "weather_code": 3, "time": "2026-09-29T12:00",
        },
    }))

    result = await get_current_weather("Berlin")
    assert result.city == "Berlin"
    assert result.temperature == 18.3
    assert result.condition == "Overcast"
    assert result.observed_at == "2026-09-29T12:00"
    assert await get_current_weather("berlin") == result
    assert geocode.call_count == forecast.call_count == 1


@pytest.mark.asyncio
@respx.mock
async def test_missing_city():
    respx.get(GEOCODING_URL).mock(
        return_value=Response(200, json={"results": []})
    )
    with pytest.raises(CityNotFound):
        await get_current_weather("no such city")


@pytest.mark.asyncio
@respx.mock
async def test_upstream_failure():
    respx.get(GEOCODING_URL).mock(return_value=Response(503))
    with pytest.raises(WeatherUnavailable):
        await get_current_weather("Berlin")
