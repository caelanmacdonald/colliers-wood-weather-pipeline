# Semantic Model

## Observation table

Use `public.weather_observations` as the fact table. Preserve the source timestamps and add three presentation fields:

- `Observation DateTime` — full observation timestamp.
- `Observation Date` — date-only field.
- `Observation Time` — time-only field.

## Calendar table

Create the table after the first and latest observation dates are available:

```dax
Calendar =
ADDCOLUMNS (
    CALENDAR (
        MIN ( weather_observations[Observation Date] ),
        MAX ( weather_observations[Observation Date] )
    ),
    "Year", YEAR ( [Date] ),
    "Month Number", MONTH ( [Date] ),
    "Month", FORMAT ( [Date], "MMM" ),
    "Year Month", FORMAT ( [Date], "YYYY-MM" ),
    "Day", DAY ( [Date] ),
    "Day Name", FORMAT ( [Date], "DDD" )
)
```

Mark `Calendar[Date]` as the date table and create a one-to-many relationship from `Calendar[Date]` to `weather_observations[Observation Date]`.

## Dashboard pages

| Page | Purpose | Status |
|---|---|---|
| Current Conditions | Latest temperature, feels-like, humidity, wind and pressure | Built |
| Historical Trends | Weather movement over the selected period | Built |
| Daily Summary | Minimum, maximum and average daily conditions | Partly documented |
| Data Pipeline Health | Freshness, observation coverage and scheduled collection status | Next |

## Data Pipeline Health layout

Use a compact operational page:

- Top cards: Pipeline Status, Latest Observation, Minutes Since Latest, Observation Count.
- Main chart: observation count by `Calendar[Date]`.
- Supporting table: latest 20 observations with observation and collection timestamps.
- Status logic: healthy at 30 minutes or less, delayed at 31–60 minutes, stale above 60 minutes.
