"""WMO weather interpretation codes used by Open-Meteo."""

_CODES: dict[int, tuple[str, str]] = {
    0: ("Clear sky", "\u2600\ufe0f"),
    1: ("Mainly clear", "\U0001f324\ufe0f"),
    2: ("Partly cloudy", "\u26c5"),
    3: ("Overcast", "\u2601\ufe0f"),
    45: ("Fog", "\U0001f32b\ufe0f"),
    48: ("Depositing rime fog", "\U0001f32b\ufe0f"),
    51: ("Light drizzle", "\U0001f326\ufe0f"),
    53: ("Moderate drizzle", "\U0001f326\ufe0f"),
    55: ("Dense drizzle", "\U0001f327\ufe0f"),
    56: ("Light freezing drizzle", "\U0001f328\ufe0f"),
    57: ("Dense freezing drizzle", "\U0001f328\ufe0f"),
    61: ("Slight rain", "\U0001f327\ufe0f"),
    63: ("Moderate rain", "\U0001f327\ufe0f"),
    65: ("Heavy rain", "\U0001f327\ufe0f"),
    66: ("Light freezing rain", "\U0001f328\ufe0f"),
    67: ("Heavy freezing rain", "\U0001f328\ufe0f"),
    71: ("Slight snow fall", "\U0001f328\ufe0f"),
    73: ("Moderate snow fall", "\U0001f328\ufe0f"),
    75: ("Heavy snow fall", "\u2744\ufe0f"),
    77: ("Snow grains", "\u2744\ufe0f"),
    80: ("Slight rain showers", "\U0001f326\ufe0f"),
    81: ("Moderate rain showers", "\U0001f327\ufe0f"),
    82: ("Violent rain showers", "\u26c8\ufe0f"),
    85: ("Slight snow showers", "\U0001f328\ufe0f"),
    86: ("Heavy snow showers", "\u2744\ufe0f"),
    95: ("Thunderstorm", "\u26c8\ufe0f"),
    96: ("Thunderstorm with slight hail", "\u26c8\ufe0f"),
    99: ("Thunderstorm with heavy hail", "\u26c8\ufe0f"),
}

_UNKNOWN = ("Unknown", "\u2753")


def describe(code: int | None) -> tuple[str, str]:
    """Return (description, icon) for a WMO weather code."""
    if code is None:
        return _UNKNOWN
    return _CODES.get(code, _UNKNOWN)
