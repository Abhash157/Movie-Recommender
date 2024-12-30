import streamlit as st
import pickle
import pandas as pd
import requests



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list= sorted(list(enumerate(distances)), reverse= True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = i[0]
    st.write(movie_index)
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        print(movie_id)

    return recommended_movies, recommended_movies_posters

def fetch_poster(movie_id):
    # response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2c925cd526756a1afdd541f2d97a00a5&language=en-US'.format(movie_id))
    response = requests.get('https://api.themoviedb.org/3/movie/256?api_key=2c925cd526756a1afdd541f2d97a00a5&language=en-US')
    data = response.json()
    return "http://image.tmdb.org/t/p/w500{}".format(data['poster_path'])

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.header('A cat')
        st.image(fetch_poster(posters[2]))
    with col2:
        st.header('A cat')
        st.image('https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg')
    with col3:
        st.header('A cat')
        st.image('https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg')
    with col4:
        st.header('A cat')
        st.image('https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg')
    with col5:
        st.header('A cat')
        st.image('https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg')
    