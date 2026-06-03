"""
live_nav_fetch.py - Day 1: Fetch live NAV from mfapi.in
"""
import requests
import pandas as pd
from pathlib import Path

RAW = Path(__file__).parent.parent / "data" / "raw"

SCHEMES = [
    (125497, "HDFC_Top_100"),
    (119551, "SBI_Bluechip"),
    (120503, "ICICI_Bluechip"),
    (118632, "Nippon_Large_Cap"),
    (119092, "Axis_Bluechip"),
    (120841, "Kotak_Bluechip"),
]

def fetch(code, name):
    url = f"https://api.mfapi.in/mf/{code}"
    print(f"Fetching {name}...")
    r = requests.get(url, timeout=15)
    data = r.json()["data"]
    df = pd.DataFrame(data)
    df.columns = ["date", "nav"]
    df["amfi_code"] = code
    df["scheme_name"] = name
    df.to_csv(RAW / f"live_nav_{name}.csv", index=False)
    print(f"  ✅ {len(df)} rows saved")

if __name__ == "__main__":
    for code, name in SCHEMES:
        try:
            fetch(code, name)
        except Exception as e:
            print(f"  ❌ {name}: {e}")