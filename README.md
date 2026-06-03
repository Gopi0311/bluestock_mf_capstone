# Data Dictionary — Bluestock MF Capstone

## 01_fund_master.csv
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | TEXT | Unique AMFI scheme code |
| fund_house | TEXT | AMC name (SBI, HDFC etc.) |
| scheme_name | TEXT | Full official fund name |
| category | TEXT | Equity / Debt / Hybrid |
| sub_category | TEXT | Large Cap / Mid Cap etc. |
| expense_ratio_pct | REAL | Annual fee charged (%) |
| risk_category | TEXT | Low / Moderate / High |
| fund_manager | TEXT | Fund manager name |

## 02_nav_history.csv
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | TEXT | Foreign key to fund_master |
| date | DATE | Business day date |
| nav | REAL | Net Asset Value in Rs. |

## 07_scheme_performance.csv
| Column | Type | Description |
|--------|------|-------------|
| return_1yr_pct | REAL | 1 year return % |
| return_3yr_pct | REAL | 3 year CAGR % |
| sharpe_ratio | REAL | Risk adjusted return |
| alpha | REAL | Return above benchmark |
| beta | REAL | Market sensitivity |
| max_drawdown_pct | REAL | Worst peak to trough fall |

## 08_investor_transactions.csv
| Column | Type | Description |
|--------|------|-------------|
| investor_id | TEXT | Unique investor ID |
| transaction_date | DATE | Date of transaction |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | INT | Amount in Rupees |
| state | TEXT | Investor state |
| age_group | TEXT | 18-25 / 26-35 etc. |
| city_tier | TEXT | T30 or B30 city |