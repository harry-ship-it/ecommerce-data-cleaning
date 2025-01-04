import pandas as pd
import numpy as np

# Load the dataset (replace 'ecommerce_data.csv' with your actual file path)
data = pd.read_csv('ecommerce_data.csv')

# Display the first few rows of the dataset
print("Original Data:")
print(data.head())

# Step 1: Handle Missing Values
numeric_columns = data.select_dtypes(include=[np.number]).columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].median())

categorical_columns = data.select_dtypes(include=['object']).columns
for col in categorical_columns:
    data[col] = data[col].fillna(data[col].mode()[0])

# Step 2: Remove Duplicates
data = data.drop_duplicates()

# Step 3: Standardize Date Format
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d', errors='coerce')

# Step 4: Normalize Text Columns
for col in categorical_columns:
    data[col] = data[col].str.strip().str.lower()

# Step 5: Export Cleaned Data
cleaned_file_path = 'cleaned_ecommerce_data.csv'
data.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")
