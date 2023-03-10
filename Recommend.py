import streamlit as st 
import pickle 
import pandas as pd
import difflib #value given by user, it might have some different spelling so to find nearest similar movies
from sklearn.feature_extraction.text import TfidfVectorizer #text to numeric values 
from sklearn.metrics.pairwise import cosine_similarity #to find similarity between movies


movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)

mov_data = pd.read_csv('movies.csv')



selected_feature = ['genres','keywords','tagline','cast','director']
for feature  in selected_feature:
  mov_data[feature]=mov_data[feature].fillna('')
combi_features = mov_data['genres'] + ' '+mov_data['keywords'] + ' '+mov_data['tagline'] + ' '+mov_data['cast'] + ' '+mov_data['director']
vectoriser = TfidfVectorizer()
feature_vectorizer = vectoriser.fit_transform(combi_features)
similarity = cosine_similarity(feature_vectorizer)

# similarity = pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True,key=lambda x: x[1])[1:11]

    recommeded_movies =[]
    for i in movie_list:
        movie_id = i[0]
        recommeded_movies.append(movies.iloc[i[0]].title)
    return recommeded_movies    






st.title('Movie Recommender System')

selected_movie= st.selectbox(
    'Enter a movie name',
    movies['title'].values)
if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    j=1
    for i in recommendations:
        st.write(j,i)
        j+=1 

