from datetime import datetime

from api import fetch_weather
from config import LOCATION
from database import save_weather, setup_database


def collect_once() -> None:
    """Fetch one weather observation and store it in Neon."""

    weather = fetch_weather()
    save_weather(weather)

    now = datetime.now().strftime("%H:%M:%S")

    print(
        f"[{now}] SAVED {LOCATION} "
        f"{weather['temperature_c']}°C "
        f"feels like {weather['feels_like_c']}°C "
        f"humidity {weather['humidity_percent']}% "
        f"wind {weather['wind_speed_kmh']} km/h "
        f"pressure {weather['surface_pressure_hpa']} hPa"
    )


def main() -> None:
    setup_database()
    collect_once()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        now = datetime.now().strftime("%H:%M:%S")
        print(f"[{now}] ERROR: {error}")
        raise