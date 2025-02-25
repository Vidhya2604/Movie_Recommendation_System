# Movie Recommendation System

## Overview
This project is a **Movie Recommendation System** built using **Python and Streamlit**. It suggests movies based on user preferences using machine learning algorithms. The system utilizes content-based filtering and collaborative filtering techniques to provide personalized recommendations.

## Features
- Recommend movies based on user input
- Interactive and user-friendly interface using **Streamlit**
- Uses machine learning techniques for recommendations
- Real-time movie suggestions
- Deployed using **Pickle** for model persistence

## Technologies Used
- **Python** (Programming Language)
- **Pandas & NumPy** (Data Handling)
- **Streamlit** (Web Application Framework)
- **Pickle** (Model Deployment)

## Installation
To run this project locally, follow these steps:

```bash
# Clone the Repository
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system

# Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # On MacOS/Linux
venv\Scripts\activate  # On Windows

# Install Required Dependencies
pip install -r requirements.txt

# Run the Streamlit App
streamlit run app.py
```

## Usage
- Open the Streamlit web app in your browser.
- Enter a movie name in the search box.
- The system will suggest similar movies based on content filtering.

## Model Training
The recommendation system is trained using:
- **TF-IDF Vectorization** for content-based filtering
- **Cosine Similarity** to find similar movies
- **Collaborative Filtering** for user-based recommendations (if applicable)

## File Structure
```bash
movie-recommendation-system/
│── app.py                  # Streamlit Web App
│── model.pkl               # Pickle file of the trained model
│── movies.csv              # Dataset containing movie details
│── requirements.txt        # Dependencies
│── README.md               # Project Documentation
└── utils.py                # Helper functions
```


- **GitHub**:(https://github.com/Vidhya2604)
- **Email**: Vidhyabca2021@gmail.com.com
