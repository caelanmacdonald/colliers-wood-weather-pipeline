\# Colliers Wood Weather Pipeline



An end-to-end cloud weather data pipeline built with Python, PostgreSQL, and Power BI.



The project automatically collects weather observations from the Open-Meteo API, stores them in a cloud-hosted PostgreSQL database (Neon), and is designed to power interactive analytics dashboards.



\---



\## Project Goals



This project was built to demonstrate practical data engineering skills including:



\- API integration

\- ETL pipeline design

\- Cloud database management

\- Version control with Git

\- Automation using GitHub Actions

\- Data visualisation with Power BI



\---



\## Technology Stack



Component       : Technology

\-----------------------

Language        : Python

API             : Open-Meteo

Database        : PostgreSQL (Neon)

Version Control : Git \& GitHub

Automation      : GitHub Actions \*(planned)\*

Analytics       : Power BI \*(planned)\*



\---



\## Architecture



```

&#x20;               Open-Meteo API

&#x20;                      │

&#x20;                      V

&#x20;             Python Weather Collector

&#x20;                      │

&#x20;                      V

&#x20;             Neon PostgreSQL Database

&#x20;                      │

&#x20;                      V

&#x20;                Power BI Dashboard

```



\---



\## Repository Structure



```

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



\---



\## Database Schema



The primary table is:



```

weather\_observations

```



Columns include:



\- collected\_at\_utc

\- location

\- weather\_time

\- temperature\_c

\- feels\_like\_c

\- humidity\_percent

\- precipitation\_mm

\- cloud\_cover\_percent

\- wind\_speed\_kmh

\- surface\_pressure\_hpa



Duplicate observations are prevented using a unique constraint on:



```

(location, weather\_time)

```



\---



\## Running Locally



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

DATABASE\_URL=your\_neon\_connection\_string

```



Run the collector:



```bash

python collector.py

```



\---



\## Roadmap



\- \[x] Modular Python application

\- \[x] Cloud PostgreSQL database

\- \[x] Historical SQLite migration

\- \[x] GitHub repository

\- \[ ] GitHub Actions automation

\- \[ ] Power BI dashboard

\- \[ ] Weather trend analysis

\- \[ ] Forecast comparison

\- \[ ] Additional public datasets



\---



\## Future Ideas



Potential future enhancements include:



\- Transport disruption data

\- Exchange rate monitoring

\- Air quality measurements

\- Energy market data

\- Interactive Power BI dashboards

\- Historical weather anomaly detection



\---



\## Author



Caelan Macdonald



GitHub: https://github.com/caelanmacdonald

