CREATE TABLE IF NOT EXISTS weather_observations (
    id BIGSERIAL PRIMARY KEY,
    collected_at_utc TIMESTAMPTZ NOT NULL,
    location TEXT NOT NULL,
    weather_time TIMESTAMPTZ NOT NULL,

    temperature_c NUMERIC(5,2),
    feels_like_c NUMERIC(5,2),
    humidity_percent NUMERIC(5,2),
    precipitation_mm NUMERIC(5,2),
    cloud_cover_percent NUMERIC(5,2),
    wind_speed_kmh NUMERIC(5,2),
    surface_pressure_hpa NUMERIC(6,2),

    UNIQUE(location, weather_time)
);