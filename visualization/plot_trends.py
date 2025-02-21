import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_trends():
    trends = pd.read_csv('trends.csv')
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='timestamp', y='score_rolling', data=trends)
    plt.title('Reddit Post Score Trends')
    plt.xlabel('Time')
    plt.ylabel('Rolling Average Score')
    plt.show()

if __name__ == "__main__":
    plot_trends()