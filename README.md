# Colliers Wood Weather Dashboard

An end-to-end Business Intelligence project that automatically collects live weather observations, stores them in a cloud-hosted PostgreSQL database, and visualises historical trends through an interactive Power BI dashboard.

The project demonstrates the complete BI lifecycle, from automated data collection through to modelling, analytics, and reporting.

---

## Project Overview

Weather observations are collected automatically every 15 minutes using the Open-Meteo API. A Python ETL pipeline cleans and loads the data into a Neon PostgreSQL database, where it is consumed by Power BI for interactive analysis.

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

- Collects weather observations every 15 minutes
- Cloud-based scheduled execution using GitHub Actions
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
weather-pipeline/

├── api.py
├── collector.py
├── config.py
├── database.py
├── schema.sql
├── requirements.txt
├── README.md
└── .gitignore
```

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

Create a `.env` file:

```text
DATABASE_URL=your_neon_connection_string
```

Run the collector:

```bash
python collector.py
```

---

## Dashboard Preview

> *(Add one or two screenshots of your completed Power BI dashboard here.)*

Suggested screenshots:

- Full dashboard
- Dashboard showing trends over multiple days

---

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