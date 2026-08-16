from datetime import datetime, timezone
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

MINUTELY_15_PARAMETERS = {
    "latitude": 51.418,
    "longitude": -0.178,
    "minutely_15": (
        "temperature_2m,"
        "relative_humidity_2m,"
        "apparent_temperature,"
        "precipitation,"
        "wind_speed_10m,"
        "surface_pressure"
    ),
    # Every run deliberately overlaps the previous six hours. PostgreSQL's
    # unique key makes the overlap safe and allows a later run to repair gaps.
    "past_minutely_15": 24,
    "forecast_minutely_15": 1,
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


def fetch_recent_15m_weather() -> list[dict[str, Any]]:
    """Return recent completed 15-minute observations for gap recovery."""

    response = requests.get(
        API_URL,
        params=MINUTELY_15_PARAMETERS,
        timeout=30,
    )
    response.raise_for_status()

    payload = response.json()["minutely_15"]
    now_utc = datetime.now(timezone.utc)
    observations: list[dict[str, Any]] = []

    for index, timestamp in enumerate(payload["time"]):
        weather_time = datetime.fromisoformat(timestamp).replace(
            tzinfo=timezone.utc
        )

        # The API request includes one forecast step so that the current
        # completed quarter-hour is available. Never store a future timestamp.
        if weather_time > now_utc:
            continue

        observations.append(
            {
                "weather_time": timestamp,
                "temperature_c": payload["temperature_2m"][index],
                "feels_like_c": payload["apparent_temperature"][index],
                "humidity_percent": payload[
                    "relative_humidity_2m"
                ][index],
                "precipitation_mm": payload["precipitation"][index],
                "wind_speed_kmh": payload["wind_speed_10m"][index],
                "surface_pressure_hpa": payload["surface_pressure"][index],
            }
        )

    return observations
