# 📊 Bulk Reviews Sentiment Analysis (ML Model + Streamlit App)

A machine learning project to analyze the sentiment of bulk product reviews (Positive/Negative).  
This app allows users to **upload a CSV file of reviews** and get sentiment predictions instantly, powered by a trained ML model.

🌐 **Live Demo**: [Run the App Here](https://bulk-reviews-sentiment-analysis-ml-model-mywbbcadqeveb4gc4xvxv.streamlit.app/)

---

## 🚀 Features
- Upload a **CSV file** containing product reviews.
- Predict sentiment (**Positive / Negative**) for each review.
- Download the results with predicted sentiments.
- Built using **Streamlit**, **scikit-learn**, **TF-IDF Vectorizer**, and **Logistic Regression**.
- Simple UI to make it recruiter- and user-friendly.

---

## 🛠️ Tech Stack
- **Python 3**
- **Streamlit** (frontend for interactive UI)
- **scikit-learn** (machine learning)
- **pandas & numpy** (data processing)
- **joblib** (model persistence)

---

## 📂 Project Structure
Bulk-Reviews-Sentiment-Analysis-ML-Model/
├── App.py # Streamlit app entry point
├── sentiment_model.joblib # Trained ML model
├── tfidf_vectorizer.joblib # Saved TF-IDF vectorizer
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── .gitignore

---

## ⚙️ Installation (Run Locally)

1. Clone the repository:
   ```bash
   git clone https://github.com/anopsingh706/Bulk-Reviews-Sentiment-Analysis-ML-Model.git
   cd Bulk-Reviews-Sentiment-Analysis-ML-Model
   
2. Create a virtual environment and install requirements:

python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt


3. Run the Streamlit app:

streamlit run App.py


Open in browser at http://localhost:8501/

📊 How to Use

1. Open the live app:
👉 https://bulk-reviews-sentiment-analysis-ml-model-mywbbcadqeveb4gc4xvxv.streamlit.app/

2. Upload a CSV file with a column named review.

3. Get instant predictions:

Positive

Negative

4. Download results as a CSV file.

 📷 Demo Screenshot
 <img width="1920" height="1080" alt="Screenshot (69)" src="https://github.com/user-attachments/assets/b305cd6b-463e-4154-bf38-442afd3a4ac3" />
