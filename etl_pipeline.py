import pandas as pd

# 1. Extracting
df = pd.read_csv("imdb_top_1000.csv")  # or your CSV file name

print("📊 Preview of data:")
print(df.head())

# 2. Transforming
print("\n🔍 Checking for missing values:")
print(df.isnull().sum())

df_clean = df.dropna()

df_high_rated = df_clean[df_clean['IMDB_Rating'] > 8]
df_sorted = df_high_rated.sort_values(by='IMDB_Rating', ascending=False)

# 3. Loading the cleaned data
df_sorted.to_csv("cleaned_high_rated_movies.csv", index=False)

print("\n✅ ETL complete! File saved as 'cleaned_high_rated_movies.csv'")
