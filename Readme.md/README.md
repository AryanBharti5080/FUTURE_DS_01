# Retail Sales Analytics Project

This project analyzes retail sales performance using the Superstore sales dataset and presents the results in a Power BI dashboard. The dashboard is designed to help users understand sales, profit, quantity sold, customer behavior, and performance across regions, categories, segments, and time periods.

## Project Overview

The goal of this project is to turn raw retail transaction data into clear business insights. It focuses on identifying sales trends, profitable and loss-making areas, regional performance, product category performance, and customer segment behavior.

Key analysis areas include:

- Total sales, profit, and quantity sold
- Sales and profit trends over time
- Regional and state-level performance
- Category and sub-category performance
- Customer segment analysis
- Discount impact on profit
- Top-performing products and customers

## Repository Structure

```text
Retail_Sales_Analytics_Project/
+-- Dashboard/
|   +-- Retail_Sales_Dashboard.pbix
+-- Dataset/
|   +-- superstore_sales.csv
+-- Readme.md/
|   +-- README.md
+-- Report/
+-- Screenshots/
```

## Dataset

The dataset used in this project is `superstore_sales.csv`, located in the `Dataset` folder.

Dataset summary:

| Metric | Value |
| --- | ---: |
| Rows | 9,994 |
| Orders | 5,009 |
| Customers | 793 |
| Products | 1,862 |
| Total Sales | 2,297,200.86 |
| Total Profit | 286,397.02 |
| Total Quantity | 37,873 |
| Order Date Range | 2014-01-03 to 2017-12-30 |

Main columns:

- `Order ID`
- `Order Date`
- `Ship Date`
- `Ship Mode`
- `Customer ID`
- `Customer Name`
- `Segment`
- `Country`
- `City`
- `State`
- `Postal Code`
- `Region`
- `Product ID`
- `Category`
- `Sub-Category`
- `Product Name`
- `Sales`
- `Quantity`
- `Discount`
- `Profit`

## Dashboard

The Power BI dashboard file is available at:

```text
Dashboard/Retail_Sales_Dashboard.pbix
```

The dashboard can be used to explore:

- Overall business performance through KPI cards
- Monthly and yearly sales trends
- Profitability by category and sub-category
- Sales contribution by region and segment
- State-wise and city-wise performance
- Products or categories causing losses
- Impact of discounts on profitability

## Tools Used

- Power BI Desktop
- CSV dataset
- Data cleaning and modeling in Power BI
- DAX measures for dashboard metrics

## How to Use

1. Open Power BI Desktop.
2. Open `Dashboard/Retail_Sales_Dashboard.pbix`.
3. If Power BI asks for the dataset path, reconnect it to `Dataset/superstore_sales.csv`.
4. Refresh the report.
5. Use filters and visuals to explore sales, profit, region, category, and customer segment insights.

## Possible Insights

This project can help answer questions such as:

- Which region generates the highest sales?
- Which category contributes the most profit?
- Which sub-categories are loss-making?
- How do discounts affect profit?
- Which customer segment performs best?
- What are the sales and profit trends over time?

## Future Improvements

- Add dashboard screenshots to the `Screenshots` folder.
- Add a detailed analysis report to the `Report` folder.
- Include DAX measure documentation.
- Add recommendations based on dashboard findings.
- Publish the dashboard to Power BI Service for sharing.

## Author

Aryan Bharti
