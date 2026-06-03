import pandas as pd

# Load dataset
df = pd.read_csv("Diabetes Missing Data.csv")

# Data Cleaning

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
for col in df.select_dtypes(include='number').columns:
    df[col] = df[col].fillna(df[col].mean())

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(df[col].mode()[0])
    df[col] = df[col].str.strip().str.title()

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

# Generate summary report
report = {
    "Total Rows": len(df),
    "Total Columns": len(df.columns),
    "Missing Values": df.isnull().sum().sum(),
    "Duplicate Rows Removed": "Completed"
}

# Save report
with open("report.txt", "w") as f:
    f.write("DATA CLEANING REPORT\n")
    f.write("====================\n")
    for key, value in report.items():
        f.write(f"{key}: {value}\n")

    f.write("\nSTATISTICAL SUMMARY\n")
    f.write("====================\n")
    f.write(str(df.describe(include="all")))

print("Data cleaning completed!")
print("Cleaned file saved as: cleaned_data.csv")
print("Report saved as: report.txt")