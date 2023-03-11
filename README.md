# Movie Recommendation System - Python
> A website made using difflib library and Streamlit

## Check this website [here](https://movierecmdvilashegde.streamlit.app/)

# How am I giving suggestions?

1. Reading the .csv file
2. Some features are selected for further calculations
    - Genres
    - Keywords
    - Tagline
    - Cast
    - Director

3.  Replacing all the null values with null string
```
for feature  in selected_feature:
mov_data[feature]=mov_data[feature].fillna('')
```
4. Combining all the selected features
5. Converting text data into feature vector ```vectoriser = TfidfVectorizer()```
> A feature vector is an n-dimensional vector of numerical features that represent some object

6. Getting Similarity scores using Cosine similarity ```cosine_similarity(feature_vectorizer)```
7. Getting movie name as input from user
8. Searching similar names based on that movie title to find the closest match
9. Selecting the first obtained movie title and get its index value
10. Getting similarity score by with all the movies in database ```list(enumerate(similarity[index_of_movie]))```
11. Slice and select any length of movies name, i gave 10 suggestions


## How did I do using Streamlit
1. Import pickle library
2. Dumping the loaded model into .pkl file ```pickle.dump(similarity, open(filename,'wb'))```
3. Load the model by using ```pickle.load(open('similarity.pkl','rb'))``` function
4. Do all the remaining operations to get the suggestions

## Choose a movie from dropdown
![image](https://user-images.githubusercontent.com/85540091/171777345-4b9c0d6f-91d1-4836-a345-f7dc683fe164.png)

## Get the result!
![image](https://user-images.githubusercontent.com/85540091/171777225-6d612492-71cc-4016-b986-d2dadce30b52.png)


## Tools needed
1. [Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)
2. Numpy 
3. Pandas
4. Difflib
5. Pickle
6. Streamlit
7. TfidfVectorizer from sklearn
8. Cosine_similarity from sklearn
