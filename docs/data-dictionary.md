# Data Dictionary

Table: `public.weather_observations`

| Column | PostgreSQL type | Meaning |
|---|---|---|
| `id` | `BIGSERIAL` | Surrogate row identifier |
| `collected_at_utc` | `TIMESTAMPTZ` | Time the collector wrote the observation |
| `location` | `TEXT` | Human-readable location, currently Colliers Wood |
| `weather_time` | `TIMESTAMPTZ` | Observation timestamp supplied by Open-Meteo |
| `temperature_c` | `NUMERIC(5,2)` | Air temperature in degrees Celsius |
| `feels_like_c` | `NUMERIC(5,2)` | Apparent temperature in degrees Celsius |
| `humidity_percent` | `NUMERIC(5,2)` | Relative humidity percentage |
| `precipitation_mm` | `NUMERIC(8,2)` | Precipitation in millimetres |
| `cloud_cover_percent` | `NUMERIC(5,2)` | Cloud cover percentage |
| `wind_speed_kmh` | `NUMERIC(7,2)` | Wind speed at 10 metres in kilometres per hour |
| `surface_pressure_hpa` | `NUMERIC(8,2)` | Surface pressure in hectopascals |

## Keys

- Primary key: `id`
- Observation key: `(location, weather_time)`

## Power BI helper fields

The semantic model should expose:

- **Observation DateTime** — the complete `weather_time` timestamp.
- **Observation Date** — date-only value for relationships, slicers and grouping.
- **Observation Time** — time-only value for intraday analysis.

Keep these presentation fields in Power Query or the semantic model rather than adding redundant columns to PostgreSQL.

## Fifteen-minute observations

Table: `public.weather_observations_15m`

This table is the detailed trend and coverage source. It contains temperature,
apparent temperature, humidity, precipitation and wind speed, which Open-Meteo
provides at 15-minute resolution. Cloud cover and surface pressure remain in
`weather_observations`, because they are not supplied as native 15-minute
variables by this endpoint.
