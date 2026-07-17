import os
from datetime import datetime, timezone
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


CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS weather_observations (
    id BIGSERIAL PRIMARY KEY,
    collected_at_utc TIMESTAMPTZ NOT NULL,
    location TEXT NOT NULL,
    weather_time TIMESTAMPTZ NOT NULL,
    temperature_c NUMERIC(5, 2),
    feels_like_c NUMERIC(5, 2),
    humidity_percent NUMERIC(5, 2),
    precipitation_mm NUMERIC(8, 2),
    cloud_cover_percent NUMERIC(5, 2),
    wind_speed_kmh NUMERIC(7, 2),
    surface_pressure_hpa NUMERIC(8, 2),
    CONSTRAINT uq_weather_observation
        UNIQUE (location, weather_time)
);
"""


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


def setup_database() -> None:
    with psycopg.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_TABLE_SQL)


def save_weather(weather: dict[str, Any]) -> None:
    row = {
        "collected_at_utc": datetime.now(timezone.utc),
        "location": "Colliers Wood",
        **weather,
    }

    with psycopg.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_WEATHER_SQL, row)