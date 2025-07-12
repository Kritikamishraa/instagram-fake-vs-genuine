
# 📘 Instagram Fake vs Genuine Account - EDA Project

# 1. Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.float_format', lambda x: '%.2f' % x)
sns.set(style="whitegrid")

# 2. Load the Dataset
df = pd.read_csv("instagram_accounts.csv")
print("🔍 First 5 rows:")
print(df.head())

# 3. Data Information
print("\n📊 Dataset Info:")
print(df.info())

# 4. Data Cleaning
binary_cols = ['Private', 'Verified', 'Profile_Pic']
df[binary_cols] = df[binary_cols].astype(int)

print("\n🧼 Missing values:")
print(df.isnull().sum())

# 5. Distribution of Fake vs Genuine
sns.countplot(x='Fake_Account', data=df)
plt.title('Distribution: Fake vs Genuine Accounts')
plt.xlabel('Fake Account (1 = Fake, 0 = Genuine)')
plt.ylabel('Count')
plt.show()

# 6. Followers Boxplot
sns.boxplot(x='Fake_Account', y='Followers', data=df)
plt.title('Followers Count Comparison')
plt.yscale('log')
plt.xlabel('Fake Account')
plt.ylabel('Followers (log scale)')
plt.show()

# 7. Following Boxplot
sns.boxplot(x='Fake_Account', y='Following', data=df)
plt.title('Following Count Comparison')
plt.yscale('log')
plt.xlabel('Fake Account')
plt.ylabel('Following (log scale)')
plt.show()

# 8. Posts Boxplot
sns.boxplot(x='Fake_Account', y='Posts', data=df)
plt.title('Posts Count Comparison')
plt.xlabel('Fake Account')
plt.ylabel('Number of Posts')
plt.show()

# 9. Correlation Matrix
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation between Features")
plt.show()

# 10. Export Cleaned Dataset
df.to_csv("cleaned_instagram_data.csv", index=False)
print("✅ Cleaned data exported to 'cleaned_instagram_data.csv'")
