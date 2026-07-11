# Bluestock Mutual Fund Analytics Capstone

## Project Overview

The Bluestock Mutual Fund Analytics Capstone is a data analytics project developed using Python, SQLite, SQL, Jupyter Notebook, and Power BI. The project analyzes Indian mutual fund data to generate performance metrics, investor insights, SIP trends, portfolio analytics, and interactive dashboards.

The project includes a complete ETL pipeline, data cleaning, exploratory data analysis, advanced analytics, and Power BI dashboards for visualization.

---

## Objectives

- Build an automated ETL pipeline for mutual fund data.
- Clean and preprocess multiple datasets.
- Store processed data in SQLite.
- Perform exploratory and advanced analytics.
- Calculate financial performance metrics.
- Build an interactive Power BI dashboard.
- Generate reports and visualizations for decision making.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- SQLite
- SQL
- Jupyter Notebook
- Power BI
- Git & GitHub

---

## Project Structure

```
bluestock_mf_capstone/

├── data/
│   ├── raw/        ← original downloaded files
│   ├── processed/  ← cleaned, merged CSVs
│   └── db/         ← bluestock_mf.db (SQLite)
│
├── notebooks/
│   ├── 01_data_ingestion.py
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_Advanced_Analytics.ipynb
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   ├── compute_metrics.py
│   └── recommender.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
|   ├── Bluestock Mutual Fund Dashboard.png
|   ├── Fund Performance Dashboard.png
|   ├── Investor Analytics Dashboard.png
|   ├── SIP & Market Trends Dashboard.png
│   ├── bluestock_mf_dashboard.pdf
|   └── bluestock_mf_dashboard.pbix
│
├── reports/
│   ├── charts/   <-EDA and analytics visualization outputs
│   ├── data_dictionary.md
│   ├── var_cvar_report.csv
│   ├── rolling_sharpe_chart.png
│   ├── Final_Report.pdf
│   └── Presentation.pptx
│
├── reports/
├── .gitignore
├── validate_amfi.py
├── requirements.txt
└── README.md
```

---

## Features

- Automated ETL Pipeline
- Data Cleaning and Validation
- SQLite Database Integration
- Exploratory Data Analysis (EDA)
- Performance Metrics
  - CAGR
  - Daily Returns
  - Sharpe Ratio
  - Sortino Ratio
  - Alpha & Beta
  - Maximum Drawdown
- Historical VaR and CVaR Analysis
- Rolling 90-Day Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Mutual Fund Recommendation System
- Sector Concentration (HHI)
- Interactive Power BI Dashboard

---

## Dashboard Pages

### Industry Overview

- Total AUM
- SIP Inflows
- Folios
- Industry AUM Trend
- AUM by AMC

### Fund Performance

- Return vs Risk Analysis
- NAV vs Benchmark
- Fund Performance Scorecard
- Interactive Filters

### Investor Analytics

- Transaction Analysis
- SIP vs Lumpsum Distribution
- Investor Demographics
- Monthly Investment Trends

### SIP & Market Trends

- SIP Inflow vs Nifty 50
- Category Inflows
- Top Performing Categories
- Market Trend Analysis

---
## Exploratory Data Analysis (EDA)

The project includes comprehensive Exploratory Data Analysis (EDA) on mutual fund industry data using Python, Pandas, Matplotlib, Seaborn, and Plotly.

### EDA Highlights

- Daily NAV trend analysis for all mutual fund schemes (2022–2026)
- AUM growth comparison across major fund houses
- Monthly SIP inflow trend analysis
- Category-wise inflow heatmap
- Investor demographics analysis
  - Age group distribution
  - Gender distribution
  - SIP amount by age group
- Geographic investment distribution
  - State-wise SIP investments
  - T30 vs B30 city comparison
- Folio count growth analysis
- NAV return correlation matrix for selected funds
- Sector allocation analysis using portfolio holdings
- 10+ business insights documented in Jupyter Notebook

### Visualizations

The project contains 15+ charts including:

- NAV Trend
- AUM Growth
- SIP Trend
- Category Heatmap
- State Distribution
- Gender Distribution
- Age Group Distribution
- SIP Amount Boxplot
- Folio Growth
- Correlation Matrix
- Sector Allocation Donut
- Benchmark Comparison
- Benchmark Trend
- Return Distribution
- Top Fund Houses

All exported visualizations are available in:

```
reports/charts/
```

## Advanced Analytics

- Historical VaR (95%)
- Conditional VaR (CVaR)
- Rolling Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Fund Recommendation Engine
- Sector HHI Concentration

---

## Outputs

- Performance Metrics Reports
- CSV Reports
- Power BI Dashboard (.pbix)
- Interactive Visualizations
- Analytics Notebooks

---

## How to Run

1. Clone the repository

```
git clone https://github.com/abhinayapravallika/mutual-fund-analytics.git
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the ETL pipeline

```
python scripts/etl_pipeline.py
```

4. Run performance metrics

```
python scripts/compute_metrics.py
```

5. Run the recommender

```
python scripts/recommender.py
```

6. Open the Power BI dashboard

```
dashboard/bluestock_mf_dashboard.pbix
```

---

## Author

**Ramena Abhinaya Pravallika**

B.Tech – Computer Science & Engineering

Bluestock Mutual Fund Analytics Capstone Project

2026