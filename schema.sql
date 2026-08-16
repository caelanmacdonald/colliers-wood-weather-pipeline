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

CREATE TABLE IF NOT EXISTS weather_observations_15m (
    id BIGSERIAL PRIMARY KEY,
    collected_at_utc TIMESTAMPTZ NOT NULL,
    location TEXT NOT NULL,
    weather_time TIMESTAMPTZ NOT NULL,

    temperature_c NUMERIC(5, 2),
    feels_like_c NUMERIC(5, 2),
    humidity_percent NUMERIC(5, 2),
    precipitation_mm NUMERIC(8, 2),
    wind_speed_kmh NUMERIC(7, 2),

    CONSTRAINT uq_weather_observation_15m
        UNIQUE (location, weather_time)
);
