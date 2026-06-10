"""
recommender.py -  Fund recommendation system
"""
import pandas as pd
from pathlib import Path

PROCESSED = Path(__file__).parent.parent / "data" / "processed"

def recommend_funds(risk_appetite):
    fm = pd.read_csv(PROCESSED / "clean_01_fund_master.csv")
    perf = pd.read_csv(PROCESSED / "clean_performance.csv")
    merged = fm.merge(perf, on='amfi_code')
    
    filtered = merged[merged['risk_category'] == risk_appetite]
    top3 = filtered.nlargest(3, 'sharpe_ratio')[
        ['scheme_name_x','fund_house_x',
         'risk_category','sharpe_ratio','return_3yr_pct']
    ]
    top3.columns = ['scheme_name','fund_house',
                    'risk_category','sharpe_ratio','return_3yr_pct']
    return top3

if __name__ == "__main__":
    for risk in ['Low', 'Moderate', 'High']:
        print(f"\n{'='*40}")
        print(f"🎯 {risk} Risk Funds:")
        print(recommend_funds(risk).to_string())