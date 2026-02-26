import streamlit as st
import pickle
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get similar movie suggestions!")

# ---------------- LOAD FILES ----------------
@st.cache_data
def load_data():
    movies = pickle.load(open('movie_list.pkl','rb'))
    similarity = pickle.load(open('similarity.pkl','rb'))
    return movies, similarity

movies, similarity = load_data()

# ---------------- RECOMMEND FUNCTION ----------------
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index

    # Safety check
    if len(movie_index) == 0:
        return ["Movie not found"]

    movie_index = movie_index[0]

    distances = similarity[movie_index]

    # Top 5 similar movies
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# ---------------- UI ----------------

selected_movie = st.selectbox(
    "Choose a movie",
    movies['title'].values
)

if st.button("Recommend Movies"):

    recommendations = recommend(selected_movie)

    st.subheader("✨ Recommended for you:")

    for movie in recommendations:
        st.write("👉", movie)