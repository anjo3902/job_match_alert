import schedule
import time
from scraper.scrape_karkidi import scrape_karkidi_jobs as scrape_jobs


from clustering.cluster_jobs import preprocess_skills, cluster_jobs

from notifier import alert_users

user_skills = ['python', 'data analysis', 'machine learning']

def daily_job_monitor():
    df = scrape_jobs()
    df = preprocess_skills(df)
    clustered_df = cluster_jobs(df)
    alert_users(clustered_df, user_skills)

def start_scheduler():
    schedule.every().day.at("09:00").do(daily_job_monitor)
    while True:
        schedule.run_pending()
        time.sleep(60)

# Call this if you want the scheduler to start when the script runs
if __name__ == "__main__":
    start_scheduler()

