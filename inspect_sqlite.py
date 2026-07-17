import sqlite3


DATABASE_PATH = (
    r"C:\Users\User\Desktop\weather_collector\weather_data.db"
)


def main() -> None:
    with sqlite3.connect(DATABASE_PATH) as connection:
        tables = connection.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
            ORDER BY name;
            """
        ).fetchall()

        print("Tables:")
        for (table_name,) in tables:
            print(f"  {table_name}")

        print("\nColumns in weather_observations:")
        columns = connection.execute(
            "PRAGMA table_info(weather_observations);"
        ).fetchall()

        for column in columns:
            print(column)


if __name__ == "__main__":
    main()