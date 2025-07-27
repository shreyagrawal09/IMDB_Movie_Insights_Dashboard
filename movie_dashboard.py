import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Set up page
st.set_page_config(page_title="🎬 Movie Insights Dashboard", layout="wide")

# Load the cleaned data
df = pd.read_csv("cleaned_high_rated_movies.csv")

st.title("🎬 IMDB Movie Explorer")
st.markdown("Explore top-rated movies using filters and visuals.")

# Sidebar Filters
st.sidebar.header("📊 Filters")

min_rating = st.sidebar.slider("Minimum IMDB Rating", 8.0, 10.0, 8.5, 0.1)
selected_genre = st.sidebar.selectbox(
    "Select Genre",
    options=["All"] + sorted(set(df['Genre'].str.split(',').explode().str.strip())),
)

# Filter Logic
filtered_df = df[df["IMDB_Rating"] >= min_rating]

if selected_genre != "All":
    filtered_df = filtered_df[filtered_df["Genre"].str.contains(selected_genre)]

st.subheader(f"🎯 {len(filtered_df)} Movies Found")

st.dataframe(filtered_df[['Series_Title', 'Released_Year', 'Genre', 'IMDB_Rating', 'Director']], use_container_width=True)

# Top 10 Bar Chart
st.subheader("⭐ Top 10 Movies by IMDB Rating")
top10 = filtered_df.sort_values(by='IMDB_Rating', ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='IMDB_Rating', y='Series_Title', data=top10, ax=ax, palette="viridis")
ax.set_title("Top 10 Rated Movies")
st.pyplot(fig)

# Yearly Trend Chart
st.subheader("📅 Number of Movies by Release Year")

year_counts = filtered_df['Released_Year'].value_counts().sort_index()

fig2, ax2 = plt.subplots(figsize=(12, 4))
sns.lineplot(x=year_counts.index, y=year_counts.values, marker="o", ax=ax2)
ax2.set_title("Movies Released by Year")
ax2.set_xlabel("Year")
ax2.set_ylabel("Count")
st.pyplot(fig2)
