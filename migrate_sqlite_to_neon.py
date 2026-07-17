import os
import sqlite3

import psycopg
from dotenv import load_dotenv


load_dotenv()

SQLITE_PATH = r"C:\Users\User\Desktop\weather_collector\weather_data.db"
DATABASE_URL = os.environ["DATABASE_URL"]


SELECT_SQL = """
SELECT
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
FROM weather_observations
ORDER BY weather_time;
"""


INSERT_SQL = """
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
DO NOTHING;
"""


def main() -> None:
    with sqlite3.connect(SQLITE_PATH) as sqlite_connection:
        sqlite_connection.row_factory = sqlite3.Row
        rows = sqlite_connection.execute(SELECT_SQL).fetchall()

    inserted = 0

    with psycopg.connect(DATABASE_URL) as postgres_connection:
        with postgres_connection.cursor() as cursor:
            for row in rows:
                cursor.execute(INSERT_SQL, dict(row))
                inserted += cursor.rowcount

    print(f"SQLite rows read: {len(rows)}")
    print(f"Rows inserted into Neon: {inserted}")
    print(f"Duplicates skipped: {len(rows) - inserted}")


if __name__ == "__main__":
    main()