#  Job Monitoring & Classification System

A Python-based system that **scrapes job listings**, **extracts skills**, **clusters jobs using unsupervised learning**, and **notifies users** when jobs match their preferred skills.

---

##  Objectives

* Scrape job listings from [Karkidi.com](https://www.karkidi.com)  
* Extract job titles, companies, skills, and other key details  
* Use **unsupervised clustering** (KMeans) on skills to classify jobs  
* Save a trained model to classify new jobs into discovered categories  
* Automatically scrape new jobs **once daily** using a scheduler  
* Alert users when a new job matches their **preferred skills**

---

##  Project Structure

hierarchial_project/
├── clustering/
│ ├── cluster_jobs.py # Preprocess skills, cluster jobs, save model
│ └── classify_new.py # Classify a new job using saved model
│
├── data/
│ └── jobs_data.csv # Scraped job data
│
├── models/
│ ├── kmeans_model.pkl # Saved KMeans clustering model
│ └── tfidf_vectorizer.pkl # Saved TF-IDF vectorizer
│
├── notifier/
│ └── alert_users.py # Alerts users if job matches skill preferences
│
├── scraper/
│ └── scrape_karkidi.py # Scrapes jobs from Karkidi
│
├── scheduler.py # Daily scheduler for scraping + notifications
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

##  How It Works

1. **Scraping**  
   Jobs are scraped using BeautifulSoup from `https://www.karkidi.com`.

2. **Skill Extraction & Clustering**  
   - Skills are vectorized using **TF-IDF**
   - Clustering is done using **KMeans**
   - Model is saved to `models/` for future use

3. **Job Classification**  
   New job inputs can be classified using the saved clustering model.

4. **User Alerts**  
   Alerts are triggered (currently via `print()`) when a job matches user-defined skills.

5. **Daily Automation**  
   The script automatically runs every day at **09:00 AM** using the `schedule` module.

---
