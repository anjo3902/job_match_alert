import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import joblib
import os

def comma_tokenizer(text):
    return text.split(',')

def preprocess_skills(df):
    df['Skills_cleaned'] = df['Skills'].apply(
        lambda x: re.sub(r'[^a-zA-Z0-9, ]', '', x.lower()) if pd.notnull(x) else "")
    return df

def cluster_jobs(df, k=5):
    vectorizer = TfidfVectorizer(tokenizer=comma_tokenizer, stop_words='english')
    X = vectorizer.fit_transform(df['Skills_cleaned'])

    kmeans = KMeans(n_clusters=k, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X)

    os.makedirs("models", exist_ok=True)
    joblib.dump(kmeans, 'models/kmeans_model.pkl')
    joblib.dump(vectorizer, 'models/tfidf_vectorizer.pkl')

    df.to_csv("data/clustered_jobs.csv", index=False)
    print("Model and vectorizer saved. Clustered data saved to data/clustered_jobs.csv")
    return df


