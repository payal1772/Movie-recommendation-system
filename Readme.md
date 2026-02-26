# 🎬 Movie Recommendation System

A Content-Based Movie Recommender built with **Python** and **Streamlit**. This project utilizes Natural Language Processing (NLP) to recommend movies based on genre and plot similarity.



[Image of Content-based filtering vs Collaborative filtering]


### 🚀 Overview
This application takes a user's favorite movie and suggests 5 similar movies. It uses **Cosine Similarity** to calculate the mathematical "closeness" between 10,000+ movies in the dataset.

### 🛠️ Tech Stack
* **Language:** Python 3.10+
* **ML Libraries:** Scikit-learn (CountVectorizer), Pandas, NumPy
* **Frontend:** Streamlit
* **Deployment:** Streamlit Cloud

### 📂 How it Works
1. **Data Preprocessing:** Cleaned and merged movie titles, genres, and overviews into "tags."
2. **Vectorization:** Converted text tags into vectors using `CountVectorizer`.
3. **Similarity Calculation:** Applied Cosine Similarity to find the nearest vectors.
4. **UI:** Created an interactive dropdown menu for seamless user experience.

### 🏁 Quick Start
To run locally:
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run app: `streamlit run app.py`