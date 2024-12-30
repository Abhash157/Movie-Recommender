import streamlit as st
import pickle
import pandas as pd
import requests
import json
# movies_list = pickle.load(open('movies.pkl','rb'))
# movies_list = movies_list['title'].values

# st.title('Movie Recommender System')

# option = st.selectbox('Movies',
#                       (movies_list))

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2c925cd526756a1afdd541f2d97a00a5'.format(movie_id))
    data = response.json()
    # st.write(data)
    # st.write(data.get("id"))
    # st.write(data.get("poster_path"))
    return "https://image.tmdb.org/t/p/w500"+ (data.get("poster_path"))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key= lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Movies',
                      (movies['title'].values))

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header(names[0])
        st.image(posters[0])
    with col2:
        st.header("move")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    with col3:
        st.header("move")
        st.image("https://static.streamlit.io/examples/cat.jpg")


