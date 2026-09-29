from fastapi.testclient import TestClient
from httpx import Response
import pytest
import respx

from backend.main import app
from backend.weather import FORECAST_URL, GEOCODING_URL, _cache


@pytest.fixture(autouse=True)
def clear_cache():
    _cache.clear()


client = TestClient(app)


def test_page_and_assets():
    assert client.get("/api/health").json() == {"status": "ok"}
    assert 'id="search-form"' in client.get("/").text
    assert client.get("/assets/app.js").status_code == 200
    assert client.get("/assets/styles.css").status_code == 200


def test_invalid_city_input():
    assert client.get("/api/weather").status_code == 422
    assert client.get("/api/weather?city=%20%20").status_code == 422


@respx.mock
def test_city_not_found():
    respx.get(GEOCODING_URL).mock(return_value=Response(200, json={}))
    response = client.get("/api/weather?city=zzzzzz")
    assert response.status_code == 404
    assert response.json() == {"detail": "City not found"}


@respx.mock
def test_forecast_failure():
    respx.get(GEOCODING_URL).mock(return_value=Response(200, json={
        "results": [{"name": "Paris", "latitude": 48.85, "longitude": 2.35}],
    }))
    respx.get(FORECAST_URL).mock(return_value=Response(503))
    response = client.get("/api/weather?city=Paris")
    assert response.status_code == 502
    assert response.json() == {"detail": "Weather service unavailable"}
