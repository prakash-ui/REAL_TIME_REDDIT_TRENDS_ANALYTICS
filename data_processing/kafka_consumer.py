from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'reddit-posts',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    print(message.value)