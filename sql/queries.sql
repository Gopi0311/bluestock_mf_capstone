-- queries.sql : 10 Analytical Queries

-- 1. Top 5 funds by expense ratio
SELECT scheme_name, fund_house, expense_ratio_pct
FROM dim_fund
ORDER BY expense_ratio_pct DESC
LIMIT 5;

-- 2. Average NAV per fund
SELECT amfi_code, ROUND(AVG(nav), 2) as avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC
LIMIT 10;

-- 3. Total SIP inflow by year
SELECT substr(month, 1, 4) as year,
ROUND(SUM(sip_inflow_crore), 2) as total_sip
FROM fact_sip_industry
GROUP BY year
ORDER BY year;

-- 4. Transactions by state
SELECT state, COUNT(*) as total_tx,
ROUND(SUM(amount_inr)/10000000, 2) as total_crore
FROM fact_transactions
GROUP BY state
ORDER BY total_tx DESC;

-- 5. Funds with expense ratio less than 1 percent
SELECT scheme_name, fund_house, expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct;

-- 6. Top 5 funds by 3 year return
SELECT amfi_code, return_3yr_pct, sharpe_ratio
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;

-- 7. AUM by fund house latest
SELECT fund_house, ROUND(SUM(aum_crore), 2) as total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC;

-- 8. SIP vs Lumpsum vs Redemption count
SELECT transaction_type, COUNT(*) as count,
ROUND(SUM(amount_inr)/10000000, 2) as total_crore
FROM fact_transactions
GROUP BY transaction_type;

-- 9. Average SIP amount by age group
SELECT age_group, ROUND(AVG(amount_inr), 2) as avg_amount
FROM fact_transactions
WHERE transaction_type = 'Sip'
GROUP BY age_group
ORDER BY avg_amount DESC;

-- 10. Top performing sectors in portfolio
SELECT sector, ROUND(AVG(weight_pct), 2) as avg_weight
FROM fact_portfolio
GROUP BY sector
ORDER BY avg_weight DESC
LIMIT 10;