import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure outputs directory exists
os.makedirs("outputs", exist_ok=True)

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

# ====== Exploratory Analysis ======

# Decision Distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='decision')
plt.title("Distribution of Loan Decisions")
plt.xticks([0, 1], ['Deny', 'Accept'])
plt.ylabel('Count')
plt.xlabel('Decision')
plt.tight_layout()
plt.savefig("outputs/decision_distribution.png")
plt.close()

# Histogram of Score (if present)
if 'score' in df.columns:
    plt.figure(figsize=(6, 4))
    sns.histplot(df['score'], bins=50, kde=True)
    plt.title("Distribution of Score")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("outputs/score_distribution.png")
    plt.close()

# Correlation heatmap with top variables related to decision
correlation = df.corr(numeric_only=True)
top_corr = correlation['decision'].abs().sort_values(ascending=False).head(11)
plt.figure(figsize=(8, 6))
sns.heatmap(df[top_corr.index].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Top Correlated Features with Decision")
plt.tight_layout()
plt.savefig("outputs/correlation_heatmap.png")
plt.close()

# Estimate cutoff score for Accepts
if 'score' in df.columns:
    cutoff_score = df[df['decision'] == 1]['score'].min()
    print(f"\n🔍 Estimated score cutoff for acceptance: {cutoff_score:.4f}")

    # Score distribution by decision
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x='score', hue='decision', kde=True, bins=50, palette='Set2', stat="density", common_norm=False)
    plt.title("Score Distribution by Decision")
    plt.xlabel("Score")
    plt.ylabel("Density")
    plt.legend(title="Decision", labels=["Deny (0)", "Accept (1)"])
    plt.tight_layout()
    plt.savefig("outputs/score_cutoff_visual.png")
    plt.close()

    # Output cutoff to text
    with open("outputs/score_cutoff.txt", "w") as f:
        f.write(f"Estimated score cutoff for acceptance: {cutoff_score:.4f}")
