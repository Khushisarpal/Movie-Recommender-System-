
import streamlit as st
import pickle



def recommend (movie):
    movie_index = movies[movies['Title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recomended_movies=[]
    rec_movies_posters=[]

    for i in movie_list:

        recomended_movies.append(movies.iloc[i[0]].Title)
        rec_movies_posters.append(movies.iloc[i[0]].Poster)

    return recomended_movies, rec_movies_posters







st.header('Movie Recommender System')

movies= pickle.load(open('movies.pkl','rb'))
similarity =pickle.load(open('similarity.pkl','rb'))

movie_list= movies['Title'].values

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list)

if st.button('Show Recommendation'):
    recomended_movies, rec_movies_posters= recommend(selected_movie)
    cols = st.columns(5)  # Create 5 columns
    for col, movie, poster in zip(cols, recomended_movies, rec_movies_posters):
        with col:
            st.image(poster)
            st.text(movie)  # Display movie title

