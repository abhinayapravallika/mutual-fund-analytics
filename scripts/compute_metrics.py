"""
compute_metrics.py

Bluestock Mutual Fund Analytics Capstone

Computes:
1. Daily Returns
2. CAGR
3. Sharpe Ratio
4. Sortino Ratio
5. Alpha
6. Beta
7. Max Drawdown
8. Fund Scorecard

"""

import pandas as pd
import numpy as np
from scipy.stats import linregress
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATA = BASE_DIR / "data" / "processed"
REPORTS = BASE_DIR / "reports" / "charts"

REPORTS.mkdir(parents=True, exist_ok=True)

nav = pd.read_csv(DATA / "02_nav_history_clean.csv")

fund = pd.read_csv(DATA / "01_fund_master_clean.csv")

benchmark = pd.read_csv(DATA / "10_benchmark_indices_clean.csv")

nav["date"] = pd.to_datetime(nav["date"])
benchmark["date"] = pd.to_datetime(benchmark["date"])

nav = nav.sort_values(["amfi_code", "date"])

print("Data Loaded Successfully")


nav["daily_return"] = (
    nav.groupby("amfi_code")["nav"]
       .pct_change()
)

nav.to_csv(DATA / "daily_returns.csv", index=False)

print("Daily Returns Created")


cagr_data = []

for code in nav["amfi_code"].unique():

    df = nav[nav["amfi_code"] == code]

    start_nav = df.iloc[0]["nav"]
    end_nav = df.iloc[-1]["nav"]

    years = (
        (df.iloc[-1]["date"] - df.iloc[0]["date"]).days
    ) / 365.25

    cagr = ((end_nav / start_nav) ** (1 / years)) - 1

    cagr_data.append(
        [code, start_nav, end_nav, years, cagr]
    )

cagr_df = pd.DataFrame(
    cagr_data,
    columns=[
        "amfi_code",
        "start_nav",
        "end_nav",
        "years",
        "cagr"
    ]
)

cagr_df["cagr_percent"] = cagr_df["cagr"] * 100

cagr_df = cagr_df.merge(
    fund[["amfi_code", "scheme_name"]],
    on="amfi_code",
    how="left"
)

cagr_df.to_csv(DATA / "cagr_table.csv", index=False)

print("CAGR Completed")


risk_free_rate = 0.065

sharpe = []

for code in nav["amfi_code"].unique():

    df = nav[nav["amfi_code"] == code]

    r = df["daily_return"].dropna()

    annual_return = r.mean() * 252

    annual_std = r.std() * np.sqrt(252)

    ratio = (annual_return - risk_free_rate) / annual_std

    sharpe.append([code, ratio])

sharpe_df = pd.DataFrame(
    sharpe,
    columns=[
        "amfi_code",
        "sharpe_ratio"
    ]
)

sharpe_df = sharpe_df.merge(
    fund[["amfi_code", "scheme_name"]],
    on="amfi_code"
)

sharpe_df.to_csv(DATA / "sharpe_ratio.csv", index=False)

print("Sharpe Ratio Completed")


sortino = []

for code in nav["amfi_code"].unique():

    df = nav[nav["amfi_code"] == code]

    r = df["daily_return"].dropna()

    downside = r[r < 0]

    downside_std = downside.std() * np.sqrt(252)

    annual_return = r.mean() * 252

    ratio = (annual_return - risk_free_rate) / downside_std

    sortino.append([code, ratio])

sortino_df = pd.DataFrame(
    sortino,
    columns=[
        "amfi_code",
        "sortino_ratio"
    ]
)

sortino_df = sortino_df.merge(
    fund[["amfi_code", "scheme_name"]],
    on="amfi_code"
)

sortino_df.to_csv(DATA / "sortino_ratio.csv", index=False)

print("Sortino Ratio Completed")


benchmark100 = benchmark[
    benchmark["index_name"] == "NIFTY100"
].copy()

benchmark100 = benchmark100.sort_values("date")

benchmark100["benchmark_return"] = benchmark100[
    "close_value"
].pct_change()

alpha_beta = []

for code in nav["amfi_code"].unique():

    df = nav[
        nav["amfi_code"] == code
    ][["date", "daily_return"]]

    merged = df.merge(
        benchmark100[
            ["date", "benchmark_return"]
        ],
        on="date"
    ).dropna()

    slope, intercept, r, p, std = linregress(
        merged["benchmark_return"],
        merged["daily_return"]
    )

    alpha = intercept * 252

    beta = slope

    alpha_beta.append(
        [code, alpha, beta, r ** 2]
    )

alpha_beta_df = pd.DataFrame(
    alpha_beta,
    columns=[
        "amfi_code",
        "alpha",
        "beta",
        "r_squared"
    ]
)

alpha_beta_df = alpha_beta_df.merge(
    fund[["amfi_code", "scheme_name"]],
    on="amfi_code"
)

alpha_beta_df.to_csv(DATA / "alpha_beta.csv", index=False)

print("Alpha Beta Completed")


drawdowns = []

for code in nav["amfi_code"].unique():

    df = nav[
        nav["amfi_code"] == code
    ].copy()

    df["running_max"] = df["nav"].cummax()

    df["drawdown"] = (
        df["nav"] / df["running_max"]
    ) - 1

    drawdowns.append(
        [code, df["drawdown"].min()]
    )

drawdown_df = pd.DataFrame(
    drawdowns,
    columns=[
        "amfi_code",
        "max_drawdown"
    ]
)

drawdown_df = drawdown_df.merge(
    fund[["amfi_code", "scheme_name"]],
    on="amfi_code"
)

drawdown_df.to_csv(DATA / "max_drawdown.csv", index=False)

print("Max Drawdown Completed")


score = fund[
    [
        "amfi_code",
        "scheme_name",
        "expense_ratio_pct"
    ]
]

score = score.merge(
    cagr_df[
        ["amfi_code", "cagr_percent"]
    ],
    on="amfi_code"
)

score = score.merge(
    sharpe_df[
        ["amfi_code", "sharpe_ratio"]
    ],
    on="amfi_code"
)

score = score.merge(
    alpha_beta_df[
        ["amfi_code", "alpha"]
    ],
    on="amfi_code"
)

score = score.merge(
    drawdown_df[
        ["amfi_code", "max_drawdown"]
    ],
    on="amfi_code"
)

score["return_rank"] = score["cagr_percent"].rank(ascending=False)

score["sharpe_rank"] = score["sharpe_ratio"].rank(ascending=False)

score["alpha_rank"] = score["alpha"].rank(ascending=False)

score["expense_rank"] = score["expense_ratio_pct"].rank()

score["dd_rank"] = score["max_drawdown"].rank(ascending=False)

score["fund_score"] = (
    0.30 * score["return_rank"] +
    0.25 * score["sharpe_rank"] +
    0.20 * score["alpha_rank"] +
    0.15 * score["expense_rank"] +
    0.10 * score["dd_rank"]
)

score = score.sort_values("fund_score")

score.to_csv(DATA / "fund_scorecard.csv", index=False)

print("Fund Scorecard Completed")

print("\nAll Performance Metrics Computed Successfully.")