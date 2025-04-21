
import pandas as pd

# Load the dataset
df = pd.read_csv("marketing_campaign.csv", sep="\t")  # Tab-separated

# Drop rows with missing 'Income' values
df_cleaned = df.dropna(subset=["Income"])

# Standardize 'Education' values
df_cleaned["Education"] = df_cleaned["Education"].str.strip().str.title()

# Standardize and clean 'Marital_Status' values
df_cleaned["Marital_Status"] = df_cleaned["Marital_Status"].str.strip().str.title()
df_cleaned["Marital_Status"] = df_cleaned["Marital_Status"].replace({
    "Alone": "Single",
    "Absurd": "Single",
    "Widow": "Widowed",
    "Yolo": "Single",
    "Together": "Living Together"
})

# Convert 'Dt_Customer' to datetime format
df_cleaned["Dt_Customer"] = pd.to_datetime(df_cleaned["Dt_Customer"], format="%d-%m-%Y")

# Clean column names
df_cleaned.columns = df_cleaned.columns.str.strip().str.lower().str.replace(" ", "_")

# Fix data types
df_cleaned["year_birth"] = df_cleaned["year_birth"].astype(int)
df_cleaned["income"] = df_cleaned["income"].astype(float)

# Save cleaned dataset
df_cleaned.to_csv("marketing_campaign_cleaned.csv", index=False)

print("✅ Data cleaned and saved as 'marketing_campaign_cleaned.csv'")
