# 🎬 Movie Recommender System
A simple content-based recommender system that suggests the Top 5 movies based on user input.
Built with Python, NLP techniques (CountVectorizer + Cosine Similarity), and Streamlit for deployment.

# 📌 Features
1. Suggests Top 5 similar movies based on the selected title
2. Uses TMDB dataset (from Kaggle)
3. Implements data preprocessing & feature engineering
4. CountVectorizer for text vectorization
5. Cosine Similarity for recommendation logic
6. Interactive Streamlit frontend

# 📂 Project Structure
├── app.py              # Streamlit frontend
├── model.ipynb         # Jupyter Notebook - training & preprocessing
├── similarity.pkl      # Precomputed similarity matrix (pickle file)
├── movies.pkl          # Preprocessed movies dataframe (pickle file)
├── requirements.txt    # Python dependencies
└── README.md

# ⚙️ Installation & Setup
1. Clone the repository
  git clone https://github.com/your-username/movie-recommender.git
  cd movie-recommender

2. Create a virtual environment (recommended)
  python -m venv venv
  source venv/bin/activate   # On Mac/Linux
  venv\Scripts\activate      # On Windows

3. Install dependencies
  pip install -r requirements.txt

4. Download the dataset
  Get the TMDB 5000 Movie Dataset from Kaggle
  Place the dataset CSV files in a folder named dataset/

# 🚀 Running the Project
1. Run Jupyter Notebook (training & preprocessing)
  jupyter notebook
  Open model.ipynb
  Run all cells to generate movies.pkl and similarity.pkl

2. Run the Streamlit App
  streamlit run app.py
  The app will open in your browser (usually at http://localhost:8501)
