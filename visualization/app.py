from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    trends = pd.read_csv('../data_analysis/trends.csv')  # Load trends from CSV
    return render_template('index.html', trends=trends.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)