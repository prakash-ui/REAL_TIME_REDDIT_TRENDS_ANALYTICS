from kafka import KafkaProducer
import json
from reddit_api import fetch_reddit_posts

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for post in fetch_reddit_posts():
    producer.send('reddit-posts', post)