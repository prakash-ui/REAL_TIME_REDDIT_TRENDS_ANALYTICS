"""
reddit_api.py

This module fetches real-time Reddit posts using the PRAW library.
"""
import praw

def fetch_reddit_posts():
    
    reddit = praw.Reddit(
        client_id='mB4VD2BTCc3EvTxCPxX9iw',
        client_secret='uGPwQzlvoSi1Z_Co88HnQPZHLbCrTA',
        user_agent="reddit-analytics:reddit_trend_analyzer:v1.0 (by /u/Historical_Ask_3761)"
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