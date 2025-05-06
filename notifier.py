def alert_users(df, user_skills):
    print("Checking for jobs matching user preferences...")
    matches = df[df['Skills_cleaned'].apply(
        lambda skills: any(skill in skills for skill in user_skills))]
    
    if not matches.empty:
        print(" Alert! Matching jobs found:")
        print(matches[['Title', 'Company', 'Skills']])
    else:
        print("No matching jobs found.")
