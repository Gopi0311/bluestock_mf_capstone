# Bluestock Fintech — Mutual Fund Analytics Capstone

## Project Overview
End-to-end Mutual Fund Analytics Platform built for Bluestock Fintech.
Ingests public AMFI data, transforms through ETL pipeline, stores in
SQLite database, and presents insights via Power BI dashboard.

## Tech Stack
- Python 3.14, Pandas, NumPy, Matplotlib, Seaborn, Plotly
- SQLite, SQLAlchemy
- Power BI Desktop
- Jupyter Notebook
- Git, GitHub

## Project Structure
```
bluestock_mf_capstone/
├── data/
│   ├── raw/          ← Original CSV files
│   ├── processed/    ← Cleaned CSVs
│   └── db/           ← SQLite database
├── notebooks/        ← Jupyter notebooks
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
├── scripts/          ← Python ETL scripts
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   ├── live_nav_fetch.py
│   ├── load_database.py
│   ├── run_queries.py
│   └── recommender.py
├── sql/
│   ├── schema.sql    ← Database schema
│   └── queries.sql   ← Analytical queries
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
├── reports/          ← Charts and PDF
├── data_dictionary.md
├── requirements.txt
└── README.md
```

## How to Run

### 1. Install dependencies
```
pip install -r requirements.txt
```

### 2. Run ETL Pipeline
```
python scripts/data_ingestion.py
python scripts/data_cleaning.py
python scripts/load_database.py
```

### 3. Fetch Live NAV Data
```
python scripts/live_nav_fetch.py
```

### 4. Run SQL Queries
```
python scripts/run_queries.py
```

### 5. Get Fund Recommendations
```
python scripts/recommender.py
```

### 6. Open Dashboard
Open `dashboard/bluestock_mf_dashboard.pbix` in Power BI Desktop

## Key Findings
- SBI Mutual Fund leads AUM at Rs.12.5 Lakh Crore
- SIP inflows hit all-time high of Rs.31,002 Cr in Dec 2025
- Total folios doubled from 13.26 Cr to 26.12 Cr in 4 years
- 26-35 age group is largest investor segment
- Consumer Goods sector dominates equity fund portfolios
- Large cap funds show 0.85+ correlation with each other
- T30 cities contribute 70% of total investments

## Dataset Details
- 40 mutual fund schemes across 10 AMCs
- 46,000+ daily NAV records (Jan 2022 - May 2026)
- 32,000+ investor transactions
- 8,050 benchmark index records
- Source: AMFI India, mfapi.in (public APIs)

## Deliverables
| # | Deliverable | Format | Status |
|---|-------------|--------|--------|
| D1 | ETL Pipeline Script | .py | Done |
| D2 | SQLite Database | .db | Done |
| D3 | EDA Notebook | .ipynb | Done |
| D4 | Performance Metrics | .ipynb + CSV | Done |
| D5 | Power BI Dashboard | .pbix | Done |
| D6 | Advanced Analytics | .ipynb | Done |
| D7 | Final Report + Slides | .pdf + .pptx | Done |

## Author
**Upputholla Gopi**
Data Analyst Intern — Bluestock Fintech
VVIT, Guntur | June 2026
GitHub: https://github.com/Gopi0311/bluestock_mf_capstone