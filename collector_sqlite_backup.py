import time
from datetime import datetime

from config import POLL_INTERVAL
from api import fetch_weather
from database import setup_database, save_weather


def main():
    setup_database()

    last_weather_time = None

    print("Weather collector started.")
    print(f"Polling every {POLL_INTERVAL} seconds...\n")

    while True:
        try:
            weather = fetch_weather()
            now = datetime.now().strftime("%H:%M:%S")

            if weather["weather_time"] != last_weather_time:
                save_weather(weather)
                last_weather_time = weather["weather_time"]

                print(
                    f"[{now}] SAVED London "
                    f"{weather['temperature_c']}°C "
                    f"feels like {weather['feels_like_c']}°C "
                    f"humidity {weather['humidity_percent']}% "
                    f"wind {weather['wind_speed_kmh']} km/h "
                    f"pressure {weather['surface_pressure_hpa']} hPa"
                )
            else:
                print(f"[{now}] No new weather observation yet.")

        except Exception as e:
            now = datetime.now().strftime("%H:%M:%S")
            print(f"[{now}] ERROR: {e}")
            print("Will try again on the next scheduled poll.\n")

        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()