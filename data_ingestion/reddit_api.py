import praw
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def fetch_reddit_posts():
    reddit = praw.Reddit(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        user_agent=os.getenv("USER_AGENT")
    )
    
    subreddit = reddit.subreddit('all')
    for submission in subreddit.stream.submissions():
        yield {
            'title': submission.title,
            'url': submission.url,
            'score': submission.score,
            'num_comments': submission.num_comments,
            'created_utc': submission.created_utc
        }
