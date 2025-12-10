
-- Top 5 customers by total revenue
SELECT
    customer_id,
    SUM(revenue) AS total_revenue
FROM orders
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT 5;

-- Revenue by product category and month
WITH monthly AS (
    SELECT
        DATE_TRUNC('month', order_date) AS month,
        category,
        SUM(revenue) AS total_revenue
    FROM orders
    GROUP BY month, category
)
SELECT * FROM monthly
ORDER BY month, category;

-- Conversion rate funnel example
SELECT
    step,
    COUNT(*) AS users,
    100.0 * COUNT(*) / SUM(COUNT(*)) OVER () AS pct_of_total
FROM funnel_events
GROUP BY step
ORDER BY step;
