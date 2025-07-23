import pandas as pd

# Load raw dataset
raw_file = r"C:\Users\abdul\OneDrive\Documents\Wasay Data Projects\Toronto Economics Analysis\toronto_housing_economics_raw.csv"
df = pd.read_csv(raw_file)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Extract Year and Month
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

# Clean numeric fields (just enforce consistent types)
df["Average_Resale_Price"] = df["Average_Resale_Price"].astype(int)
df["Housing_Starts"] = df["Housing_Starts"].astype(int)

# Optional sanity check print
print("✅ Sample cleaned data:")
print(df.head())

# Export cleaned CSV
output_path = (r"C:\Users\abdul\OneDrive\Documents\Wasay Data Projects\Toronto Economics Analysis\cleaned_toronto_housing.csv")
df.to_csv(output_path, index=False)
print(f"✅ Cleaned file saved to: {output_path}")