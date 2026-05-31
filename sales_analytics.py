import pandas as pd

# Load Dataset
df = pd.read_csv("Dataset.csv")

# ==========================
# Basic Data Information
# ==========================
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

# ==========================
# KPI Calculations
# ==========================
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
profit_margin = (total_profit / total_sales) * 100

print("\n===== BUSINESS KPIs =====")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Profit Margin: {profit_margin:.2f}%")

# ==========================
# Sales by Category
# ==========================
category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== SALES BY CATEGORY =====")
print(category_sales)

# ==========================
# Profit by Region
# ==========================
region_profit = (
    df.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== PROFIT BY REGION =====")
print(region_profit)

# ==========================
# Top 10 Products by Sales
# ==========================
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n===== TOP 10 PRODUCTS =====")
print(top_products)

# ==========================
# Sales by Segment
# ==========================
segment_sales = (
    df.groupby("Segment")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== SALES BY SEGMENT =====")
print(segment_sales)

# ==========================
# Revenue Trend
# ==========================
df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
)

print("\n===== MONTHLY SALES TREND =====")
print(monthly_sales)

# ==========================
# Export Summary Files
# ==========================
category_sales.to_csv("category_sales.csv")
region_profit.to_csv("region_profit.csv")
top_products.to_csv("top_products.csv")
segment_sales.to_csv("segment_sales.csv")

print("\nAnalysis Complete.")
print("Summary files exported successfully.")
