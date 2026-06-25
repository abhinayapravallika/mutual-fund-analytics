
SELECT *
FROM fact_aum
ORDER BY aum DESC
LIMIT 5;


SELECT
strftime('%Y-%m', full_date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav fn
JOIN dim_date dd
ON fn.date_id = dd.date_id
GROUP BY month;



SELECT
year,
SUM(amount) AS total_sip
FROM fact_transactions ft
JOIN dim_date dd
ON ft.date_id = dd.date_id
WHERE transaction_type='SIP'
GROUP BY year;


SELECT
state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state;



SELECT *
FROM fact_performance
WHERE expense_ratio < 1;



SELECT *
FROM fact_performance
ORDER BY return_1y DESC
LIMIT 10;



SELECT AVG(expense_ratio)
FROM fact_performance;



SELECT
month,
SUM(amount)
FROM fact_transactions ft
JOIN dim_date dd
ON ft.date_id = dd.date_id
GROUP BY month;



SELECT
category,
SUM(aum)
FROM fact_aum fa
JOIN dim_fund df
ON fa.fund_id = df.fund_id
GROUP BY category;



SELECT
fund_id,
SUM(amount)
FROM fact_transactions
WHERE transaction_type='Redemption'
GROUP BY fund_id;