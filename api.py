from typing import Any

import requests


API_URL = "https://api.open-meteo.com/v1/forecast"

PARAMETERS = {
    "latitude": 51.418,
    "longitude": -0.178,
    "current": (
        "temperature_2m,"
        "relative_humidity_2m,"
        "apparent_temperature,"
        "precipitation,"
        "cloud_cover,"
        "wind_speed_10m,"
        "surface_pressure"
    ),
    "timezone": "UTC",
}


def fetch_weather() -> dict[str, Any]:
    response = requests.get(
        API_URL,
        params=PARAMETERS,
        timeout=30,
    )
    response.raise_for_status()

    payload = response.json()
    current = payload["current"]

    return {
        "weather_time": current["time"],
        "temperature_c": current.get("temperature_2m"),
        "feels_like_c": current.get("apparent_temperature"),
        "humidity_percent": current.get("relative_humidity_2m"),
        "precipitation_mm": current.get("precipitation"),
        "cloud_cover_percent": current.get("cloud_cover"),
        "wind_speed_kmh": current.get("wind_speed_10m"),
        "surface_pressure_hpa": current.get("surface_pressure"),
    }