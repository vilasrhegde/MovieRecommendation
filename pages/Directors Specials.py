import streamlit as st 
import pandas as pd
import plotly.express as px

mov_data = pd.read_csv('movies.csv')
st.title('Directos Specials')
max = st.slider('How many directors you need?',min_value=1,max_value=100,value=10,step=1)
df=mov_data.loc[:,['title','budget','popularity','runtime','vote_count','director','vote_average','vote_count']]

g = df.groupby(['director'], as_index=False)
count = g.size().reset_index()
grp = g.agg({'popularity':'sum'})
grp.merge(count)
grp['director'].replace(' ','unknown')

sorted_df = grp.sort_values(by=['popularity'],ascending=True)

st.plotly_chart(px.bar(sorted_df[-max:], x="popularity", y='director', title=f"Total Popularity from all movies directed by top {max} directors",orientation='h'),use_container_width=True)

title_runtime=df.sort_values(by=['runtime'],ascending=False).loc[:,['title','runtime','budget','director']]
title_runtime.fillna(0,inplace=True)
st.plotly_chart(px.bar(title_runtime[:max], x="title", y='runtime',color='director',hover_data=['budget',], title="Longest runtime movies & their budgets",width=500))
