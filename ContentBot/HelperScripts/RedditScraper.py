import praw
import os

reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                     client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                     user_agent="ROBOT1")

subreddit = reddit.subreddit('relationship_advice')
def get_top_month_submissions(limit):
    list_of_submissions = []
    for submission in subreddit.top(time_filter="month", limit=limit):
        list_of_submissions.append({"Title": submission.title, "Body": submission.selftext})
    return list_of_submissions

def get_hot_submissions(limit):
    list_of_submissions = []
    for submission in subreddit.hot(limit=limit):
        list_of_submissions.append({"Title": submission.title, "Body": submission.selftext, "Score": submission.score, "URL": submission.url})
    return list_of_submissions