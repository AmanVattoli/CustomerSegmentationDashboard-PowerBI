import pandas as pd

# Load the cleaned dataset
data_cleaned = pd.read_csv('cleaned_purchase_data.csv')

# Basic statistics
print(data_cleaned.describe())

# Analyze distribution of purchase values
data_cleaned['value [USD]'].hist()

# Group by product category to see sales per category
product_sales = data_cleaned.groupby('product_category')['value [USD]'].sum()
print(product_sales)

# Findings:

# 1. Product category 505 generated the highest revenue at $443,451.26.

# 2. There is a relatively balanced spread of revenue among the categories, with most categories generating between $300,000 to $350,000.

# 3. Product categories 509 ($313,093.63) and 511 ($313,385.53) have lower total sales compared to others.