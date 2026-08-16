# Colliers Wood Weather Dashboard

An end-to-end Business Intelligence project that automatically collects live weather observations, stores them in a cloud-hosted PostgreSQL database, and visualises historical trends through an interactive Power BI dashboard.

The project demonstrates the complete BI lifecycle, from automated data collection through to modelling, analytics, and reporting.

---

## Project Overview

GitHub Actions wakes the collector approximately hourly. Each run stores a full current-condition snapshot and retrieves an overlapping six-hour window of 15-minute Open-Meteo observations. The overlap allows later runs to repair scheduler delays before Neon PostgreSQL supplies the data to Power BI.

The dashboard provides:

- Current weather conditions
- Historical temperature, humidity and wind trends
- Daily summary statistics
- Dynamic DAX-driven insights
- Automated cloud data collection

---

## Skills Demonstrated

This project showcases practical experience with:

- Python application development
- REST API integration
- ETL pipeline design
- PostgreSQL database design
- Cloud database management (Neon)
- SQL querying
- Git & GitHub version control
- GitHub Actions automation
- Power BI dashboard development
- DAX measures and calculations
- Data storytelling and visualisation

---

## Technology Stack

| Component | Technology |
|----------|------------|
| Language | Python |
| API | Open-Meteo API |
| Database | PostgreSQL (Neon) |
| Automation | GitHub Actions |
| Version Control | Git & GitHub |
| Analytics | Microsoft Power BI |
| Data Modelling | DAX |
| SQL | PostgreSQL |

---

## Architecture

```text
          Open-Meteo API
                 │
                 ▼
     Python Weather Collector
                 │
                 ▼
        GitHub Actions (15 min)
                 │
                 ▼
      Neon PostgreSQL Database
                 │
                 ▼
         Microsoft Power BI
                 │
                 ▼
     Interactive Weather Dashboard
```

---

## Features

### Automated Data Collection

- Collects a recoverable 15-minute weather series
- Cloud-based hourly execution using GitHub Actions
- Six-hour overlapping backfill on every run
- Automatic insertion into PostgreSQL
- Duplicate protection using database constraints

### Dashboard Analytics

Current dashboard includes:

- Current Conditions
  - Temperature
  - Feels Like Temperature
  - Humidity
  - Wind Speed
  - Surface Pressure

- Historical Trends
  - Temperature over time
  - Humidity over time
  - Wind speed over time

- Summary Statistics
  - Daily maximum temperature
  - Daily minimum temperature
  - Average daily temperature
  - Average humidity

- Dynamic Insights
  - Temperature change since previous reading
  - Humidity trend
  - Wind trend
  - Temperature compared to historical average
  - Automated weather summary

---

## Database

Primary table:

```text
weather_observations
```

Example fields:

- collected_at_utc
- location
- weather_time
- temperature_c
- feels_like_c
- humidity_percent
- wind_speed_kmh
- surface_pressure_hpa
- precipitation_mm
- cloud_cover_percent

Duplicate observations are prevented using a unique constraint on:

```sql
(location, weather_time)
```

---

## Repository Structure

```text
colliers-wood-weather-pipeline/

├── .github/workflows/collect-weather.yml
├── docs/
│   ├── architecture.md
│   └── data-dictionary.md
├── power-bi/
│   ├── measures.dax
│   ├── model.md
│   └── screenshots/
├── api.py
├── collector.py
├── config.py
├── database.py
├── schema.sql
├── requirements.txt
├── RESUME-HERE.md
├── README.md
├── .env.example
└── .gitignore
```

To continue development, start with [`RESUME-HERE.md`](RESUME-HERE.md). It records the current state, the next dashboard task and the most useful operational checks.

---

## Running Locally

Clone the repository:

```bash
git clone https://github.com/caelanmacdonald/colliers-wood-weather-pipeline.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Copy the environment template and replace its placeholder value:

```bash
cp .env.example .env
```

Run the collector:

```bash
python collector.py
```

---

## Dashboard Preview

<img width="1302" height="726" alt="image" src="https://github.com/user-attachments/assets/e1bdcfd4-986d-4fc7-b25d-15d94aa4bb38" />

The dashboard presents live weather observations collected automatically every 15 minutes via GitHub Actions. Data is stored in PostgreSQL (Neon) and visualised in Power BI, including current conditions, historical trends, daily statistics, and automatically generated weather insights.

## Future Improvements

Potential future enhancements include:

- Weather forecasting comparison
- Air quality integration
- UV index monitoring
- Interactive location selection
- Alert thresholds
- Forecast accuracy analysis
- Additional environmental datasets

---

## Author

**Caelan Macdonald**

GitHub: https://github.com/caelanmacdonald

---

## Why I Built This

This project was created to demonstrate the complete Business Intelligence workflow—from automated data collection and cloud database management to analytical modelling and dashboard design.

Rather than focusing solely on Power BI, the objective was to build an end-to-end solution that reflects how modern BI systems are developed in production environments.
