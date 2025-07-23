import pandas as pd
import pyodbc

# Load cleaned data
csv_path = r"C:\Users\abdul\OneDrive\Documents\Wasay Data Projects\Toronto Economics Analysis\cleaned_toronto_housing.csv"
df = pd.read_csv(csv_path)

# Connect to local SQL Server
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=TorontoHousingDB;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

# Insert each row into the SQL table
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO toronto_housing (
            Date, Average_Resale_Price, Housing_Starts, 
            Unemployment_Rate, Participation_Rate, Employment_Rate, 
            GDP_Growth, CPI_Toronto, Year, Month
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, 
        row["Date"], row["Average_Resale_Price"], row["Housing_Starts"],
        row["Unemployment_Rate"], row["Participation_Rate"], row["Employment_Rate"],
        row["GDP_Growth"], row["CPI_Toronto"], row["Year"], row["Month"]
    )

conn.commit()
cursor.close()
conn.close()

print("✅ Data inserted successfully into toronto_housing table.")