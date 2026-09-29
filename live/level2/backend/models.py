from pydantic import BaseModel


class WeatherResponse(BaseModel):
    city: str
    country: str
    latitude: float
    longitude: float
    temperature: float
    feels_like: float
    humidity: int
    wind_speed: float
    weather_code: int
    condition: str
    icon: str
    units: str
    observed_at: str
