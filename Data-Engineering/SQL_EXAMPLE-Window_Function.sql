
-- Running total of revenue
SELECT
    customer_id,
    order_date,
    revenue,
    SUM(revenue) OVER (PARTITION BY customer_id ORDER BY order_date) AS running_revenue
FROM orders;

-- Previous month's revenue using LAG
SELECT
    month,
    revenue,
    LAG(revenue, 1) OVER (ORDER BY month) AS prev_month_revenue
FROM monthly_revenue;

-- 3-month moving average
SELECT
    month,
    revenue,
    AVG(revenue) OVER (
        ORDER BY month
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS revenue_3mo_ma
FROM monthly_revenue;
