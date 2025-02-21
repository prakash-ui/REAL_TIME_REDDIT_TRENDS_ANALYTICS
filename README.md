# Reddit Real-Time Analytics Pipeline

## Overview
This project is a real-time analytics pipeline for Reddit data, including trend analysis and visualization.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Kafka producer:
   ```bash
   python data_ingestion/kafka_producer.py
   ```
3. Run the Flask app:
   ```bash
   python visualization/app.py
   ```

## Deployment
- Build the Docker image:
  ```bash
  docker build -t reddit-analytics .
  ```
- Run the Docker container:
  ```bash
  docker run -p 5000:5000 reddit-analytics
  ```