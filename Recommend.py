import streamlit as st 
import pickle 
import pandas as pd
import difflib #value given by user, it might have some different spelling so to find nearest similar movies
from sklearn.feature_extraction.text import TfidfVectorizer #text to numeric values 
from sklearn.metrics.pairwise import cosine_similarity #to find similarity between movies
import numpy as np

movies_dict = pickle.load(open('movies.pkl','rb'))

movies = pd.DataFrame(movies_dict)

mov_data = pd.read_csv('movies.csv')
# st.table(movies.head(1))


selected_feature = ['genres','keywords','tagline','cast','director']
for feature  in selected_feature:
  mov_data[feature]=mov_data[feature].fillna('')
combi_features = mov_data['genres'] + ' '+mov_data['keywords'] + ' '+mov_data['tagline'] + ' '+mov_data['cast'] + ' '+mov_data['director']
vectoriser = TfidfVectorizer()
feature_vectorizer = vectoriser.fit_transform(combi_features)
similarity = cosine_similarity(feature_vectorizer)

# similarity = pickle.load(open('similarity.pkl','rb'))
@st.cache_data
def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True,key=lambda x: x[1])[1:11]

    # st.table(movie_list)

    recommeded_movies =[]
    for i in movie_list:
        movie_id = i[0]
        # st.table(movies.iloc[i[0]])
        recommeded_movies.append([movies.iloc[i[0]].title]+[str(movies.iloc[i[0]].homepage)]+[movies.iloc[i[0]].director] + 
                                 [movies.iloc[i[0]].cast]+[movies.iloc[i[0]].vote_average] )

        # reshape_tb=tb.reshape(9,3)

        
    tb=np.array(recommeded_movies)
    tb=pd.DataFrame(tb, columns=['Title','Homepage','Director','Cast','Votes'])
    # tb=tb.reset_index()
    # blankIndex=[''] * len(tb)
    # tb.index=blankIndex
    tb.index = np.arange(1, len(tb) + 1)

    # st.dataframe(tb)
    selected_mov_genres = movies[movies['title']==movie]['genres'].to_string()
    selected_mov_genres=''.join([i for i in selected_mov_genres if not i.isdigit()])
    st.sidebar.write(f'''
    ## Genre of {movie} are:
    ''')
    st.sidebar.write(selected_mov_genres.split())
    return recommeded_movies    






st.title('Movie Recommender System')

selected_movie= st.selectbox(
    'Enter a movie name',
    movies['title'].values)

# recommendations = recommend(selected_movie)
# j=1
# for i in recommendations:
#     st.write(j,i)
#     j+=1 

result=recommend(selected_movie)
count=0
for i in result:
    count+=1
    with st.expander(f'{count} {i[0]}'):
      st.markdown(f'''
      
      :blue[Director]: {i[2]}
      
      :blue[Cast]: {i[3]}
      
      :blue[Ratings]: {i[4]}/10
      
       {'' if i[1]=='nan' else ':red[Homepage]: '+i[1]}
      
      ''')
    