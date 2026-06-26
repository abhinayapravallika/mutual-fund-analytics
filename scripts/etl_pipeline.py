import pandas as pd
from sqlalchemy import create_engine

# Create SQLite connection
engine = create_engine("sqlite:///db/bluestock_mf.db")

# Read all cleaned CSV files

fund_master = pd.read_csv("./data/processed/01_fund_master_clean.csv")
nav = pd.read_csv("./data/processed/02_nav_history_clean.csv")
aum = pd.read_csv("./data/processed/03_aum_by_fund_house_clean.csv")
sip = pd.read_csv("./data/processed/04_monthly_sip_inflows_clean.csv")
category = pd.read_csv("./data/processed/05_category_inflows_clean.csv")
folio = pd.read_csv("./data/processed/06_industry_folio_count_clean.csv")
perf = pd.read_csv("./data/processed/07_scheme_performance_clean.csv")
txn = pd.read_csv("./data/processed/08_investor_transactions_clean.csv")
holdings = pd.read_csv("./data/processed/09_portfolio_holdings_clean.csv")
benchmark = pd.read_csv("./data/processed/10_benchmark_indices_clean.csv")

# Load into SQLite

fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

sip.to_sql(
    "monthly_sip_inflows",
    engine,
    if_exists="replace",
    index=False
)

category.to_sql(
    "category_inflows",
    engine,
    if_exists="replace",
    index=False
)

folio.to_sql(
    "industry_folio_count",
    engine,
    if_exists="replace",
    index=False
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

holdings.to_sql(
    "portfolio_holdings",
    engine,
    if_exists="replace",
    index=False
)

benchmark.to_sql(
    "benchmark_indices",
    engine,
    if_exists="replace",
    index=False
)

print("===================================")
print("Database Loaded Successfully!")
print("===================================")

print("Rows Loaded:")
print("dim_fund:", len(fund_master))
print("fact_nav:", len(nav))
print("fact_aum:", len(aum))
print("monthly_sip_inflows:", len(sip))
print("category_inflows:", len(category))
print("industry_folio_count:", len(folio))
print("fact_performance:", len(perf))
print("fact_transactions:", len(txn))
print("portfolio_holdings:", len(holdings))
print("benchmark_indices:", len(benchmark))