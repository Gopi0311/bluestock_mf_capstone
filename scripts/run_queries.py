"""
run_queries.py : Run all 10 SQL queries
"""
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

DB = Path(__file__).parent.parent / "data" / "db" / "bluestock_mf.db"
engine = create_engine(f"sqlite:///{DB}")

queries = {
    "Top 5 funds by expense ratio": "SELECT scheme_name, fund_house, expense_ratio_pct FROM dim_fund ORDER BY expense_ratio_pct DESC LIMIT 5",
    "Avg NAV per fund": "SELECT amfi_code, ROUND(AVG(nav),2) as avg_nav FROM fact_nav GROUP BY amfi_code ORDER BY avg_nav DESC LIMIT 5",
    "SIP inflow by year": "SELECT substr(month,1,4) as year, ROUND(SUM(sip_inflow_crore),2) as total FROM fact_sip_industry GROUP BY year",
    "Transactions by state": "SELECT state, COUNT(*) as total FROM fact_transactions GROUP BY state ORDER BY total DESC LIMIT 5",
    "Funds expense < 1%": "SELECT scheme_name, expense_ratio_pct FROM dim_fund WHERE expense_ratio_pct < 1.0",
    "Top 5 by 3yr return": "SELECT amfi_code, return_3yr_pct FROM fact_performance ORDER BY return_3yr_pct DESC LIMIT 5",
    "AUM by fund house": "SELECT fund_house, ROUND(SUM(aum_crore),2) as aum FROM fact_aum GROUP BY fund_house ORDER BY aum DESC LIMIT 5",
    "Tx type split": "SELECT transaction_type, COUNT(*) as count FROM fact_transactions GROUP BY transaction_type",
    "Avg SIP by age": "SELECT age_group, ROUND(AVG(amount_inr),2) as avg FROM fact_transactions WHERE transaction_type='Sip' GROUP BY age_group",
    "Top sectors": "SELECT sector, ROUND(AVG(weight_pct),2) as avg_wt FROM fact_portfolio GROUP BY sector ORDER BY avg_wt DESC LIMIT 5",
}

for title, sql in queries.items():
    print(f"\n{'='*40}")
    print(f"📊 {title}")
    print(pd.read_sql(sql, engine).to_string(index=False))