"""
data_ingestion.py - Day 1: Load all 10 CSV datasets
"""
import pandas as pd
from pathlib import Path

RAW = Path(__file__).parent.parent / "data" / "raw"

DATASETS = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv",
]

def load_all():
    for filename in DATASETS:
        fp = RAW / filename
        if not fp.exists():
            print(f"⚠️  Not found: {filename}")
            continue
        df = pd.read_csv(fp)
        print(f"\n✅ {filename}")
        print(f"   Shape: {df.shape}")
        print(df.head(2))

if __name__ == "__main__":
    load_all()