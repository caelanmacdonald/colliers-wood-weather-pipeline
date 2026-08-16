import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import psycopg
from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL was not found. Check that .env exists "
        "in the project folder."
    )


SCHEMA_PATH = Path(__file__).with_name("schema.sql")


INSERT_WEATHER_SQL = """
INSERT INTO weather_observations (
    collected_at_utc,
    location,
    weather_time,
    temperature_c,
    feels_like_c,
    humidity_percent,
    precipitation_mm,
    cloud_cover_percent,
    wind_speed_kmh,
    surface_pressure_hpa
)
VALUES (
    %(collected_at_utc)s,
    %(location)s,
    %(weather_time)s,
    %(temperature_c)s,
    %(feels_like_c)s,
    %(humidity_percent)s,
    %(precipitation_mm)s,
    %(cloud_cover_percent)s,
    %(wind_speed_kmh)s,
    %(surface_pressure_hpa)s
)
ON CONFLICT (location, weather_time)
DO UPDATE SET
    collected_at_utc = EXCLUDED.collected_at_utc,
    temperature_c = EXCLUDED.temperature_c,
    feels_like_c = EXCLUDED.feels_like_c,
    humidity_percent = EXCLUDED.humidity_percent,
    precipitation_mm = EXCLUDED.precipitation_mm,
    cloud_cover_percent = EXCLUDED.cloud_cover_percent,
    wind_speed_kmh = EXCLUDED.wind_speed_kmh,
    surface_pressure_hpa = EXCLUDED.surface_pressure_hpa;
"""

INSERT_15M_WEATHER_SQL = """
INSERT INTO weather_observations_15m (
    collected_at_utc,
    location,
    weather_time,
    temperature_c,
    feels_like_c,
    humidity_percent,
    precipitation_mm,
    wind_speed_kmh
)
VALUES (
    %(collected_at_utc)s,
    %(location)s,
    %(weather_time)s,
    %(temperature_c)s,
    %(feels_like_c)s,
    %(humidity_percent)s,
    %(precipitation_mm)s,
    %(wind_speed_kmh)s
)
ON CONFLICT (location, weather_time)
DO UPDATE SET
    temperature_c = EXCLUDED.temperature_c,
    feels_like_c = EXCLUDED.feels_like_c,
    humidity_percent = EXCLUDED.humidity_percent,
    precipitation_mm = EXCLUDED.precipitation_mm,
    wind_speed_kmh = EXCLUDED.wind_speed_kmh;
"""


def setup_database() -> None:
    create_table_sql = SCHEMA_PATH.read_text(encoding="utf-8")

    with psycopg.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.execute(create_table_sql)


def save_weather(weather: dict[str, Any]) -> None:
    row = {
        "collected_at_utc": datetime.now(timezone.utc),
        "location": "Colliers Wood",
        **weather,
    }

    with psycopg.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_WEATHER_SQL, row)


def save_15m_weather(observations: list[dict[str, Any]]) -> None:
    """Upsert a recoverable window of quarter-hour observations."""

    if not observations:
        return

    collected_at_utc = datetime.now(timezone.utc)
    rows = [
        {
            "collected_at_utc": collected_at_utc,
            "location": "Colliers Wood",
            **observation,
        }
        for observation in observations
    ]

    with psycopg.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.executemany(INSERT_15M_WEATHER_SQL, rows)
