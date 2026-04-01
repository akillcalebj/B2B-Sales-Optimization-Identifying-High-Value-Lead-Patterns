-- Query to identify high-performing lead segments
SELECT 
    industry,
    outreach_channel,
    ROUND(AVG(conversion_rate), 2) as avg_conversion,
    SUM(opportunity_value) as total_revenue
FROM mock_leads_data
GROUP BY industry, outreach_channel
ORDER BY total_revenue DESC;
