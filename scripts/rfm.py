import pandas as pd
import datetime as dt

# Load the cleaned data
data_cleaned = pd.read_csv('cleaned_purchase_data.csv')

# Step 1: Create RFM table
reference_date = dt.datetime(2018, 12, 1)  # Example: Set a reference date for recency calculation

# Grouping by Customer ID
rfm_table = data_cleaned.groupby('customer_id').agg({
    'date': lambda x: (reference_date - pd.to_datetime(x).max()).days,  # Recency
    'customer_id': 'count',  # Frequency
    'value [USD]': 'sum'     # Monetary
})

# Rename columns to recency, frequency, monetary
rfm_table.columns = ['recency', 'frequency', 'monetary']

# Assign RFM scores (1 to 5) using quantiles
rfm_table['R_score'] = pd.qcut(rfm_table['recency'], 5, labels=[5, 4, 3, 2, 1])
rfm_table['F_score'] = pd.qcut(rfm_table['frequency'].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
rfm_table['M_score'] = pd.qcut(rfm_table['monetary'], 5, labels=[1, 2, 3, 4, 5])

# Combine RFM scores into one column
rfm_table['RFM_Segment'] = rfm_table['R_score'].astype(str) + rfm_table['F_score'].astype(str) + rfm_table['M_score'].astype(str)
rfm_table['RFM_Score'] = rfm_table[['R_score', 'F_score', 'M_score']].sum(axis=1)

# Display top customers based on RFM score
print(rfm_table.head())

# Save the RFM table to a CSV file
rfm_table.to_csv('rfm_analysis.csv', index=True)
