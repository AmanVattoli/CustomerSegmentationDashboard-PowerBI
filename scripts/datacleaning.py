import pandas as pd

# Load the dataset
data = pd.read_csv('purchase_data_exe.csv')

# Remove unnecessary column
data_cleaned = data.drop(columns=['Unnamed: 7'])

# Convert date column to datetime format
data_cleaned['date'] = pd.to_datetime(data_cleaned['date'], format='%d/%m/%Y')

# Check for missing values
print(data_cleaned.isnull().sum())

# Handle missing values
data_cleaned = data_cleaned.dropna()

# Save the cleaned dataset to a new CSV file
data_cleaned.to_csv('cleaned_purchase_data.csv', index=False)

print("Cleaned data saved to 'cleaned_purchase_data.csv'")
