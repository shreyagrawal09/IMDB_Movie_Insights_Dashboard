# 🎬 IMDB Movie Insights Dashboard

This is a simple project that I have made while learning the process of ETL (Extract, Transform and Load) which showcases an **end-to-end ETL pipeline** followed by an **interactive Streamlit dashboard** built using a dataset of top-rated movies from IMDB.

## 🔍 Project Overview

We perform the full **ETL process**:
- **Extract** data from a Kaggle IMDB movies dataset.
- **Transform** the data to clean inconsistencies and prepare it for analysis.
- **Load** the cleaned dataset into a CSV file for dashboard consumption.

An interactive **Streamlit dashboard** is then built to visualize:
- Movie filtering by IMDB rating and genre
- Top 10 movies bar chart
- Year-wise release trend line chart

---

## 📌 Features

✅ ETL pipeline using **Pandas**  
✅ Data visualization with **Seaborn** and **Matplotlib**  
✅ Interactive filters in **Streamlit** sidebar  
✅ Dashboard deployed locally for exploration  

---

## 🛠️ Tech Stack

- Python 3.11
- Pandas
- Seaborn
- Matplotlib
- Streamlit


---

## 🚀 Getting Started

1. **Clone this repository**:
   ```bash
   git clone https://github.com/shreyagrawal09/IMDB_Movie_Insights_Dashboard.git
   cd IMDB_Movie_Insights_Dashboard
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

   ```

3. **Run the dashboard**:
   ```bash
   streamlit run movie_dashboard.py
   ```

---

## 📁 Project Structure

```
IMDB_Movie_Insights_Dashboard/
│
├── etl_cleaning.py              # ETL script to clean raw data
├── movie_dashboard.py           # Streamlit dashboard app
├── cleaned_high_rated_movies.csv
├── README.md                    # You're reading it!
├── requirements.txt             # Python dependencies
└── screenshots/                 # Dashboard preview images (optional)
```

---

## 📂 Dataset Source

- [🎬 IMDB Movies Dataset on Kaggle](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows)


---

## 👨‍💻 Author

**Shrey Agrawal**  
*Final Year B.Tech Student | Data & Backend Enthusiast*

---
