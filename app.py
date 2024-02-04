from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Create the sentiment analysis pipeline
sent_pipeline = pipeline("sentiment-analysis")

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data['text']

    # Use the sentiment analysis pipeline
    result = sent_pipeline(text)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
