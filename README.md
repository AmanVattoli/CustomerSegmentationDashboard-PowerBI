# Customer Segmentation Dashboard

## Overview

This **Customer Segmentation Dashboard** offers a detailed analysis of customer purchasing behavior using **Recency, Frequency, and Monetary (RFM)** segmentation. The original purchase dataset, which includes transaction-level data such as purchase amounts and dates, was analyzed to derive the RFM dataset. This transformation involved scoring customers based on how recently they made a purchase (Recency), how frequently they made purchases (Frequency), and their total spending (Monetary). The dashboard uses these RFM scores to segment customers into categories that drive strategic decision-making for personalized marketing and retention initiatives.

### Key Features

- **Total Customers**: Displays the total number of customers.
- **Average Purchases**: The average number of purchases made by customers.
- **Average Order Value**: Displays the average amount spent by customers.
- **Customer Distribution by RFM Score**: A histogram showcasing the spread of customers based on their RFM scores.
- **Customer Segmentation TreeMap**: Visualizes several customer segments
- **Top Customers by Spending and RFM Score**: Highlights top customers based on total purchase value and RFM scores.

### Data Exploration and Cleaning

The data was cleaned and prepared for analysis through the following steps:
1. **Exploratory Data Analysis (EDA)**: Identified missing values, outliers, and overall distribution of data.
2. **RFM Segmentation**: Customers were segmented based on recency, frequency, and monetary metrics to identify key customer groups.
3. **Data Cleaning**: Handled missing values, corrected data types, and removed inconsistencies.

### Key Customer Segments and Insights

![Customer Segmentation Dashboard](https://github.com/user-attachments/assets/4beacc70-3f8b-4557-8d6b-e63b0290af05)

- **Potential Loyalists (4.13K customers):** These customers have shown potential to become loyal, with the right strategies in place to engage them.
  
- **Champions (2.04K customers):** High-value customers who frequently purchase. Target them with exclusive offers and loyalty programs.
  
- **At Risk (1.42K customers):** These customers have recently stopped engaging. Re-engagement strategies are vital to prevent churn.
  
- **Lost Customers (0.88K customers):** Customers who haven't purchased in a long time and are likely to churn. Win-back campaigns should target them.

- **Cannot Lose Them (0.63K customers):** These are significant but infrequent spenders. Focus on personalized attention to retain them.

- **Promising (2.42K customers):** Customers showing promise but still in the lower spending range. They may become loyal customers with the right offers.

- **New Customers (1.39K customers):** Recent customers that need nurturing to foster loyalty through engagement and special offers.

- **Loyal Customers (2.25K customers):** Customers with consistent purchases who are likely to remain loyal but still benefit from engagement.

- **Hibernating Customers (1.62K customers):** Previously active customers that are now inactive but could be reactivated with targeted campaigns.

- **Need Attention (1.61K customers):** These customers are on the verge of disengagement, and immediate intervention is necessary to keep them active.

- **About To Sleep (1.38K customers):** These customers haven’t been active in a while, and it’s crucial to engage them soon to prevent churn.
