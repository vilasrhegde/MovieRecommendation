import streamlit as st 
import pandas as pd
import plotly.express as px

mov_data = pd.read_csv('movies.csv')
df=mov_data.loc[:,['title','budget','popularity','runtime','vote_count','director','vote_average','vote_count']]

popular_mov = df.sort_values(by=['popularity'],ascending=True)

st.title('MOST POPULAR MOVIES')

max = st.slider('How many movies you need?',min_value=1,max_value=100,value=10,step=1)
st.plotly_chart(px.bar(popular_mov[-max:], x="title", y='popularity',color='director',title="Most popular movies",height=500),use_container_width=True)



#----------most voted -----------
avg_vote = df.sort_values(by=['vote_average'],ascending=False)
avg_vote.isnull().sum()
avg_vote.fillna('unknown',inplace=True)

st.plotly_chart(px.bar(avg_vote[:max], x="title", y='vote_average',color='director',title="Highest voted movies"),use_container_width=True)

