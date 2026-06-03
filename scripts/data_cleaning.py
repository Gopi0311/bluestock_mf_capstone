"""
data_cleaning : Clean all 10 datasets
"""
import pandas as pd
import numpy as np
from pathlib import Path

RAW = Path(__file__).parent.parent / "data" / "raw"
PROCESSED = Path(__file__).parent.parent / "data" / "processed"

def clean_nav_history():
    print("\n📄 Cleaning nav_history...")
    df = pd.read_csv(RAW / "02_nav_history.csv")
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(['amfi_code', 'date'])
    df = df.drop_duplicates()
    df = df[df['nav'] > 0]
    df = df.dropna()
    df.to_csv(PROCESSED / "clean_nav_history.csv", index=False)
    print(f"  ✅ {len(df)} rows saved")

def clean_transactions():
    print("\n📄 Cleaning investor_transactions...")
    df = pd.read_csv(RAW / "08_investor_transactions.csv")
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    df = df[df['amount_inr'] > 0]
    df['transaction_type'] = df['transaction_type'].str.strip().str.title()
    df = df.drop_duplicates()
    df = df.dropna(subset=['investor_id', 'amfi_code', 'amount_inr'])
    df.to_csv(PROCESSED / "clean_transactions.csv", index=False)
    print(f"  ✅ {len(df)} rows saved")

def clean_performance():
    print("\n📄 Cleaning scheme_performance...")
    df = pd.read_csv(RAW / "07_scheme_performance.csv")
    df = pd.to_numeric(df['sharpe_ratio'], errors='coerce')
    df = pd.read_csv(RAW / "07_scheme_performance.csv")
    for col in ['return_1yr_pct','return_3yr_pct','return_5yr_pct','sharpe_ratio']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    df = df.dropna()
    df.to_csv(PROCESSED / "clean_performance.csv", index=False)
    print(f"  ✅ {len(df)} rows saved")

def clean_remaining():
    files = [
        "01_fund_master.csv",
        "03_aum_by_fund_house.csv",
        "04_monthly_sip_inflows.csv",
        "05_category_inflows.csv",
        "06_industry_folio_count.csv",
        "09_portfolio_holdings.csv",
        "10_benchmark_indices.csv",
    ]
    for f in files:
        df = pd.read_csv(RAW / f)
        df = df.drop_duplicates()
        df = df.dropna(how='all')
        out = f.replace(".csv", "").replace("0","clean_",1)
        df.to_csv(PROCESSED / f"clean_{f}", index=False)
        print(f"  ✅ clean_{f} — {len(df)} rows")

if __name__ == "__main__":
    print("🧹 Starting data cleaning...")
    clean_nav_history()
    clean_transactions()
    clean_performance()
    print("\n📄 Cleaning remaining files...")
    clean_remaining()
    print("\n✅ All files cleaned and saved to data/processed/")