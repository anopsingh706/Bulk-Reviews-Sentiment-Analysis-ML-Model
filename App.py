import streamlit as st
import pandas as pd
import joblib

# Load saved model + vectorizer
model = joblib.load("sentiment_model.joblib")
vectorizer = joblib.load("tfidf_vectorizer.joblib")

st.title("📊 Bulk Reviews Sentiment Analysis")
st.write("Upload a CSV file containing reviews and get sentiment predictions!")

# File uploader
uploaded_file = st.file_uploader("Upload CSV with a column named 'review'", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if "review" not in df.columns:
        st.error("CSV must have a column called 'review'")
    else:
        # Predict sentiments
        X = vectorizer.transform(df["review"].astype(str))
        predictions = model.predict(X)
        df["Sentiment"] = ["Positive" if p == 1 else "Negative" for p in predictions]

        # Show results
        st.success("✅ Analysis complete!")
        st.dataframe(df)

        # Allow download
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Results", csv, "results.csv", "text/csv")
