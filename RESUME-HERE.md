# Resume Here

This is the quickest route back into the Colliers Wood Weather Dashboard project.

## Current state

- Open-Meteo supplies current Colliers Wood observations.
- `collector.py` runs one collection cycle.
- Neon PostgreSQL stores observations in `public.weather_observations`.
- `(location, weather_time)` prevents duplicate observations.
- GitHub Actions runs hourly at minute 17.
- Every run retrieves an overlapping six-hour window of 15-minute data, so
  delayed or missed triggers can be repaired automatically.
- Power BI reads the PostgreSQL table and presents current conditions and historical trends.

## Next piece of work

Build the **Data Pipeline Health** page in Power BI.

1. Open the existing **Colliers Wood Weather Dashboard** report.
2. Confirm `weather_observations[weather_time]` and `weather_observations[collected_at_utc]` are typed as Date/Time with timezone handling applied consistently.
3. Add the Calendar table and model relationships described in `power-bi/model.md`.
4. Add the health measures from `power-bi/measures.dax`.
5. Create cards for latest observation, minutes since latest observation, pipeline status and observation count.
6. Save a screenshot in `power-bi/screenshots/` and update the dashboard status below.

## Dashboard status

| Area | Status | Next action |
|---|---|---|
| Current snapshots | Working | Monitor hourly scheduled runs |
| 15-minute recovery | Implemented | Confirm row growth after deployment |
| Neon storage | Working | Confirm row growth periodically |
| Current conditions | Built | Record exact measures and formatting |
| Historical trends | Built | Record exact visuals and axes |
| Calendar model | Planned | Create table and relationship |
| Pipeline health | Planned | Build next |

## Common checks

Run the collector locally:

```powershell
Copy-Item .env.example .env
python -m pip install -r requirements.txt
python collector.py
```

Check the most recent database observations:

```sql
SELECT weather_time, collected_at_utc, temperature_c, humidity_percent
FROM public.weather_observations
ORDER BY weather_time DESC
LIMIT 20;
```

Check collection coverage:

```sql
SELECT
    MIN(weather_time) AS first_observation,
    MAX(weather_time) AS latest_observation,
    COUNT(*) AS observation_count
FROM public.weather_observations;
```

## Project map

- `README.md` — public project overview and setup.
- `RESUME-HERE.md` — current status and exact next action.
- `collector.py`, `api.py`, `database.py` — collection pipeline.
- `schema.sql` — canonical database schema.
- `.github/workflows/collect-weather.yml` — automation.
- `docs/` — architecture and data reference.
- `power-bi/` — model, measures and dashboard records.
