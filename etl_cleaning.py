import pandas as pd

# ---------- Extract ----------
# Load Excel file
input_file = "wellbeing-toronto-housing.xlsx"
xls = pd.ExcelFile(input_file)

# Read both raw sheets
df_2008 = pd.read_excel(xls, sheet_name="RawDataRef-Period2008")
df_2011 = pd.read_excel(xls, sheet_name="RawDataRef_2011")

# Add year column to track data origin
df_2008["dataset_year"] = 2008
df_2011["dataset_year"] = 2011

# ---------- Transform ----------
def clean_columns(df):
    """
    Standardizes column names to snake_case and strips spaces.
    """
    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(" ", "_")
                  .str.replace("-", "_")
    )
    return df

df_2008 = clean_columns(df_2008)
df_2011 = clean_columns(df_2011)

# Ensure numeric columns are numeric
for col in df_2008.columns:
    if col not in ["neighbourhood", "dataset_year"]:
        df_2008[col] = pd.to_numeric(df_2008[col], errors="coerce")

for col in df_2011.columns:
    if col not in ["neighbourhood", "dataset_year"]:
        df_2011[col] = pd.to_numeric(df_2011[col], errors="coerce")

# Combine datasets
combined_df = pd.concat([df_2008, df_2011], ignore_index=True)

# Optional: sort by neighbourhood then year
combined_df = combined_df.sort_values(by=["neighbourhood", "dataset_year"]).reset_index(drop=True)

# ---------- Load ----------
output_file = "cleaned_toronto_housing.csv"
combined_df.to_csv(output_file, index=False)

print(f"Cleaned dataset saved to {output_file}")
