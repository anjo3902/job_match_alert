import streamlit as st
import pandas as pd
from scraper.scrape_karkidi import scrape_karkidi_jobs
from clustering.cluster_jobs import preprocess_skills, cluster_jobs
from notifier import alert_users

st.set_page_config(page_title="Job Match Alert", layout="wide")

st.title("💼 Job Match Alert App")
st.write("This app scrapes jobs from Karkidi, clusters them, and alerts you based on your skills.")

# Sidebar
st.sidebar.header("Settings")
keyword = st.sidebar.text_input("Job Keyword", value="data science")
pages = st.sidebar.slider("Number of Pages to Scrape", 1, 5, 2)
user_skills_input = st.sidebar.text_input("Your Skills (comma-separated)", value="python, data analysis, machine learning")

user_skills = [skill.strip().lower() for skill in user_skills_input.split(",") if skill.strip()]

if st.button("🔍 Scrape and Find Jobs"):
    with st.spinner("Scraping job postings..."):
        df = scrape_karkidi_jobs(keyword=keyword, pages=pages)
    st.success(f"Scraped {len(df)} jobs.")

    with st.spinner("Preprocessing and clustering..."):
        df = preprocess_skills(df)
        clustered_df = cluster_jobs(df)

    st.subheader("Clustered Job Listings")
    st.dataframe(clustered_df[['Title', 'Company', 'Skills', 'Cluster']])

    st.subheader("🎯 Matching Jobs Based on Your Skills")
    matches = clustered_df[clustered_df['Skills_cleaned'].apply(
        lambda skills: any(skill in skills for skill in user_skills))]

    if not matches.empty:
        st.success(f"Found {len(matches)} matching jobs!")
        st.dataframe(matches[['Title', 'Company', 'Skills']])
    else:
        st.warning("No matching jobs found based on your skills.")
