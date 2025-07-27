import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the cleaned CSV
df = pd.read_csv("cleaned_high_rated_movies.csv")


sns.set(style="whitegrid")

# Showing first few rows
print(df.head())


# to get the top 10 movies by rating we should:
top10 = df.sort_values(by='IMDB_Rating', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x='IMDB_Rating', y='Series_Title', data=top10, palette="viridis")
plt.title("🎬 Top 10 Highest Rated Movies", fontsize=16)
plt.xlabel("IMDB Rating")
plt.ylabel("Movie Title")
plt.tight_layout()
plt.show()



plt.figure(figsize=(8, 5))
sns.histplot(df['IMDB_Rating'], bins=10, kde=True, color='skyblue')
plt.title("⭐ Distribution of IMDB Ratings")
plt.xlabel("IMDB Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
 


 # spliting mutliple genres for movies
genre_series = df['Genre'].str.split(',').explode().str.strip()
top_genres = genre_series.value_counts().head(5)

plt.figure(figsize=(6, 6))
top_genres.plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
plt.title("🎭 Top 5 Genres")
plt.ylabel("")
plt.tight_layout()
plt.show()
