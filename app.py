import streamlit as st
import pickle
import pandas as pd

# ---------------- LOAD FILES ----------------
# Use st.cache_data so the app doesn't reload large files every time you click a button
@st.cache_data
def load_data():
    movies = pickle.load(open('movie_list.pkl','rb'))   # movie dataframe
    similarity = pickle.load(open('similarity.pkl','rb'))  # similarity matrix
    return movies, similarity

movies, similarity = load_data()

# ---------------- RECOMMEND FUNCTION ----------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    # Get top 5 similar movies
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# ---------------- UI DESIGN ----------------
st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get similar movie suggestions!")

# 🎥 Dropdown with all movie titles
# Added a unique key just in case, though removing the duplicate code fixes the main issue
selected_movie = st.selectbox(
    "Choose a movie",
    movies['title'].values,
    key="movie_dropdown"
)

# 🔘 Button
if st.button("Recommend Movies", key="recommend_button"):
    recommendations = recommend(selected_movie)
    st.subheader("✨ Recommended for you:")
    
    for movie in recommendations:
        st.write("👉", movie)