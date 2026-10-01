import pandas as pd

# Load raw data
df = pd.read_excel("Task1_Data_Cleaning_and_Preprocessing.xlsx", sheet_name="Raw_Data")

# 1. Clean column names
df.columns = (
    df.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)
)

# 2. Remove extra spaces and standardize text
for col in ["customer_name", "gender", "city", "active"]:
    df[col] = df[col].astype("string").str.strip()

df["gender"] = df["gender"].replace({
    "M": "Male", "m": "Male", "F": "Female", "f": "Female",
    "male": "Male", "female": "Female", "FEMALE": "Female"
})

df["city"] = df["city"].replace({
    "hyderabad": "Hyderabad", "HYDERABAD": "Hyderabad",
    "Bangalore": "Bengaluru"
})

df["active"] = df["active"].replace({"Y": "Yes", "N": "No"})

# 3. Convert data types
df["join_date"] = pd.to_datetime(df["join_date"], dayfirst=True, errors="coerce")
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["annual_income"] = pd.to_numeric(df["annual_income"], errors="coerce")

# 4. Handle missing values
df["age"] = df["age"].fillna(df["age"].median())
df["annual_income"] = df["annual_income"].fillna(df["annual_income"].median())
df["gender"] = df["gender"].fillna(df["gender"].mode()[0])

# 5. Remove exact duplicate rows
df = df.drop_duplicates()

# 6. Check possible duplicate customer IDs
df["duplicate_customer_id_flag"] = df.duplicated("customer_id", keep=False)

# Save cleaned data
df.to_excel("Cleaned_Customer_Data.xlsx", index=False)

print("Data cleaning completed successfully.")
print(df.isna().sum())
