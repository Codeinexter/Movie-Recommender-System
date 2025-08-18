import streamlit as st
import pickle
import pandas as pd

# Load data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommend function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# --- FRONTEND STARTS HERE ---
st.set_page_config(page_title="🎬 Movie Recommender", page_icon="🍿", layout="wide")

st.markdown(
    """
    <style>
    .main-title {
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        color: #FF4B4B;
        margin-bottom: 10px;
    }
    .sub-title {
        text-align: center;
        font-size: 20px;
        color: #666;
        margin-bottom: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">🎬 Movie Recommender System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Get personalized movie suggestions instantly 🍿</div>', unsafe_allow_html=True)

# Dropdown in center
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    selected_movie_name = st.selectbox("Pick a movie to get recommendations:", movies['title'].values)

# Recommend button
center = st.columns([2, 1, 2])
with center[1]:
    recommend_button = st.button("✨ Recommend Movies")

# Show recommendations
if recommend_button:
    names = recommend(selected_movie_name)

    st.subheader("Here are your top picks 👇")
    st.write("---")

    # Display movies in nice cards
    cols = st.columns(3)
    for idx, name in enumerate(names):
        with cols[idx % 3]:
            st.markdown(
                f"""
                <div style="
                    background: #f9f9f9;
                    padding: 20px;
                    border-radius: 15px;
                    text-align: center;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                    margin-bottom: 20px;">
                    <h4 style="color:#333;">{name}</h4>
                    <p style="color:#888;">Recommended for you 🍿</p>
                </div>
                """,
                unsafe_allow_html=True
            )