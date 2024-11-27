import pandas as pd
from scipy.stats import zscore

# Load the dataset
file_path = input(str("Enter th file path (without double quote):  "))
df = pd.read_csv(file_path)

# Inspect the data
print("Initial Dataset Info:")
print(df.info())
print("\nPreview of Data:")
print(df.head())

# Remove duplicate rows
df = df.drop_duplicates()
print("\nDuplicates removed.")

#Handle missing values
# For numerical columns fill missing values with median
for column in df.select_dtypes(include='number').columns:
    df[column] = df[column].fillna(df[column].median())

# For categorical columns fill missing values with the mode
for column in df.select_dtypes(include='object').columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].mode()[0])

print("\nMissing values handled.")

#Removoving outliers (using Z-score method)

z_scores = df.select_dtypes(include='number').apply(zscore)
df = df[(z_scores < 3).all(axis=1)]  
print("\nOutliers removed.")

#Standardize column names by lowercase and replace spaces with underscores
df.columns = df.columns.str.lower().str.replace(' ', '_')
print("\nColumn names standardized.")

#Drop irrelevant or unimportant columns (interactive input)
print("\nColumns in the dataset:")
print(list(df.columns))
columns_to_drop = input(
    "Enter the column names to drop (comma-separated) , or press Enter to skip:"
).split(',')

columns_to_drop = [col.strip() for col in columns_to_drop if col.strip()]
if columns_to_drop:
    df = df.drop(columns=columns_to_drop, errors='ignore')
    print(f"\nDropped columns: {columns_to_drop}")
else:
    print("\nNo columns were dropped.")

#Convert data types if necessary
for column in df.select_dtypes(include='object').columns:
    if 'date' in column or 'time' in column:  
        df[column] = pd.to_datetime(df[column], errors='coerce')

print("\nData types adjusted.")

#Save the cleaned dataset
output_path = "cleaned_data.csv"  # output file path
df.to_csv(output_path, index=False)
print(f"\nCleaned data saved to {output_path}")

# Summary
print("Final Dataset Info:")
print(df.info())
print("Preview of Cleaned Data:")
print(df.head())
