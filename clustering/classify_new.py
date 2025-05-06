import joblib
import re

def classify_new_job(skill_text):
    model = joblib.load('models/kmeans_model.pkl')
    vectorizer = joblib.load('models/tfidf_vectorizer.pkl')

    cleaned = re.sub(r'[^a-zA-Z0-9, ]', '', skill_text.lower())
    X_new = vectorizer.transform([cleaned])
    cluster = model.predict(X_new)
    return cluster[0]

if __name__ == "__main__":
    skills = "python, pandas, machine learning"
    print("Predicted Cluster:", classify_new_job(skills))
