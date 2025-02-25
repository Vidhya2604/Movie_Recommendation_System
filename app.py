import streamlit as st
import pandas as pd
import requests
import pickle

# Load the pickle file
with open('movie_data.pkl', 'rb') as file:
    Movies, cosine_sim = pickle.load(file)

# Function to get recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = Movies[Movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Get top 10 similar movies
    movies_indices = [i[0] for i in sim_scores]
    return Movies['title'].iloc[movies_indices]  # Returns a Series of movie titles

# Function to fetch movie poster
def fetch_poster(movie_id):
    api_key = '5a7a751ed5e97e464ba0c2320b403a1e'  # TMDB API key
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()  # Parse the JSON response
        
        # Debugging: Print the data to see its structure
        print("Response data:", data)
        
        # Use .get() to safely access 'poster_path'
        poster_path = data.get('poster_path', None)  # Default to None if not found
        if poster_path:  # Check if poster_path is not None
            return f'https://image.tmdb.org/t/p/w500{poster_path}'
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    
    return "https://via.placeholder.com/130"  # Return placeholder if no poster found

# Streamlit UI
st.title("Movie Recommendation System")

selected_movie = st.selectbox('Select a movie:', Movies['title'].values)

if st.button('Recommend'):
    recommendations = get_recommendations(selected_movie)
    st.write("Top 10 Recommended Movies:")

    for i in range(0, 10, 5):  # Loop in batches of 5
        cols = st.columns(5)  # Create 5 columns for each row
        for col, j in zip(cols, range(i, i + 5)):
            if j < len(recommendations):
                movie_title = recommendations.iloc[j]  # Get movie title correctly
                movie_ids = Movies.loc[Movies['title'] == movie_title, 'movie_id']  # Properly access movie_id
                
                if not movie_ids.empty:
                    movie_id = movie_ids.values[0]  # Access the first movie_id
                    poster_url = fetch_poster(movie_id)
                    with col:
                        st.image(poster_url, width=130)
                        st.write(movie_title)
                else:
                    st.write(f"No ID found for {movie_title}")  # Handle case where no movie_id is found
