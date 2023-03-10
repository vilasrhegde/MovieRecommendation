

import streamlit as st 
import pandas as pd
import plotly.express as px

mov_data = pd.read_csv('movies.csv')
st.title('Genre Specific')
max = st.slider('How many movies you need?',min_value=1,max_value=100,value=10,step=1)


data_on_genre = mov_data.loc[:,['title','genres','director','budget','vote_average','popularity']]
data_on_genre= data_on_genre.fillna('unknown')


# Genre list is obtained from MovRecommend.ipynb
select_one_genre=st.sidebar.multiselect(
    'Which genre/s are you interested?',
    ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Fiction', 'Foreign', 'History', 'Horror', 'Movie', 'Music', 'Mystery', 'Romance', 'Science', 'TV', 'Thriller', 'War', 'Western'],
    default=['Action','Thriller']
)
# select_one_genre=select_one_genre.capitalize()
# st.write(select_one_genre)

    


movies_of_same_genre = data_on_genre[data_on_genre['genres'].isin(select_one_genre)]
# movies_of_same_genre['Genre_opted']=select_one_genre

movies_of_same_genre=movies_of_same_genre.sort_values(by=['popularity'],ascending=True)

st.plotly_chart(px.bar(movies_of_same_genre[-max:], x="title", y='popularity', color='director', title=f"Top movies from {', '.join(select_one_genre)}"),use_container_width=True)
