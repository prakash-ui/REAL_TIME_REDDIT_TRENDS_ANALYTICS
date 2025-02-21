import pandas as pd

def calculate_trends(data, window_size=5):
    """
    Calculate trends from Reddit post data.

    Args:
        data (list of dict): List of Reddit posts.
        window_size (int): Rolling window size in minutes.

    Returns:
        pd.DataFrame: DataFrame with rolling average scores.
    """
    df = pd.DataFrame(data)
    
    # Ensure 'created_utc' exists
    if 'created_utc' not in df.columns:
        raise ValueError("Input data must contain 'created_utc' field.")
    
    # Convert timestamp and calculate rolling average
    df['timestamp'] = pd.to_datetime(df['created_utc'], unit='s')
    df.set_index('timestamp', inplace=True)
    df['score_rolling'] = df['score'].rolling(window=f'{window_size}T').mean()
    
    return df

# Example usage
if __name__ == "__main__":
    # Simulate input data (replace with actual data from Kafka)
    data = [
        {
            'title': 'This is a Reddit post',
            'url': 'https://www.reddit.com/r/all/comments/xyz123/this_is_a_reddit_post/',
            'score': 1234,
            'num_comments': 56,
            'created_utc': 1697049600
        },
        {
            'title': 'Another Reddit post',
            'url': 'https://www.reddit.com/r/all/comments/abc456/another_reddit_post/',
            'score': 567,
            'num_comments': 12,
            'created_utc': 1697049660
        }
    ]
    
    # Calculate trends
    trends = calculate_trends(data)
    print(trends)
    
    # Save trends to CSV
    trends.to_csv('trends.csv')