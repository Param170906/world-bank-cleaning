import zipfile
import os

zip_path = r'C:\Users\Daljit\Downloads\archive.zip'
extract_to = r'C:\Users\Daljit\Downloads\extracted_data'

# Extract the ZIP file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print("✅ Extracted Successfully.")
import pandas as pd

csv_path = r'C:\Users\Daljit\Downloads\extracted_data\world_bank_data_2025.csv'
df = pd.read_csv(csv_path)

df.head()
# Remove duplicates
df = df.drop_duplicates()

# Fix column names (strip spaces, lower case)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

# Check for nulls
print(df.isnull().sum())

# Fill or drop nulls
# Example: fill numeric columns with mean
df = df.fillna(df.mean(numeric_only=True))

# Final preview
df.head()
clean_path = r'C:\Users\Daljit\Downloads\cleaned_world_bank_data.csv'
df.to_csv(clean_path, index=False)
print("✅ Cleaned data saved.")
