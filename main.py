from scraper.scrape_karkidi import scrape_karkidi_jobs
from clustering.cluster_jobs import preprocess_skills, cluster_jobs

# Step 1: Scrape jobs
df = scrape_karkidi_jobs(keyword="data science", pages=2)

# Step 2: Preprocess
df = preprocess_skills(df)

# Step 3: Cluster
clustered_df = cluster_jobs(df)

# View results
print(clustered_df[['Title', 'Company', 'Skills', 'Cluster']].head())
