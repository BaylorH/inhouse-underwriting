import pandas as pd

# Load data
df = pd.read_csv('data/raw_data.csv')

# Drop identifiers
df.drop(columns=['uuid', 'tracking_number'], inplace=True)

# Drop timestamp for now
df.drop(columns=['created_at'], inplace=True)

# Convert decision to binary
df['decision'] = df['decision'].map({'Deny': 0, 'Accept': 1}).astype('int8')

# Encode ccr_worst_pmt_rating as categorical codes
df['ccr_worst_pmt_rating'] = df['ccr_worst_pmt_rating'].astype('category').cat.codes

# Print shape and confirm dtypes
print(f"✅ Cleaned dataset shape: {df.shape}")
print("\n📊 Data types summary:")
print(df.dtypes.value_counts())

# Optional: peek at head
print("\n🔍 Sample rows:")
print(df.head())
