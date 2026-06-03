"""
load_database.py : Load cleaned data into SQLite database
"""
import pandas as pd
from sqlalchemy import create_engine, text
from pathlib import Path

PROCESSED = Path(__file__).parent.parent / "data" / "processed"
DB_PATH = Path(__file__).parent.parent / "data" / "db" / "bluestock_mf.db"

engine = create_engine(f"sqlite:///{DB_PATH}")

def load_table(filename, table_name):
    fp = PROCESSED / filename
    if not fp.exists():
        print(f"  ⚠️  Not found: {filename}")
        return
    df = pd.read_csv(fp)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"  ✅ {table_name} — {len(df)} rows loaded")

if __name__ == "__main__":
    print("🗄️  Loading database...")
    load_table("clean_01_fund_master.csv", "dim_fund")
    load_table("clean_nav_history.csv", "fact_nav")
    load_table("clean_transactions.csv", "fact_transactions")
    load_table("clean_performance.csv", "fact_performance")
    load_table("clean_03_aum_by_fund_house.csv", "fact_aum")
    load_table("clean_04_monthly_sip_inflows.csv", "fact_sip_industry")
    load_table("clean_09_portfolio_holdings.csv", "fact_portfolio")
    load_table("clean_10_benchmark_indices.csv", "fact_benchmark")
    print("\n✅ Database ready at data/db/bluestock_mf.db")