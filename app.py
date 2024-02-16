from flask import Flask, request, jsonify, render_template, send_from_directory
from transformers import pipeline
from sentiment_analysis_module.sentiment_model import (
    sia,
    polarity_scores_vader,
    polarity_scores_roberta,
)
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)
# Create the sentiment analysis pipeline
sent_pipeline = pipeline("sentiment-analysis")


@app.route("/docs/<path:filename>")
def serve_docs(filename):
    return send_from_directory("docs/documentation", filename)


class HelloWorld(Resource):
    def get(self):
        """Endpoint to get a simple greeting."""
        return jsonify(message="Hello, World!")


api.add_resource(HelloWorld, "/hello")


@app.route("/analyze_sentiment", methods=["POST"])
def analyze_sentiment():
    data = request.get_json()
    text = data["text"]

    # Use the sentiment analysis pipeline
    pipeline_result = sent_pipeline(text)

    # Use VADER sentiment analysis
    vader_result = polarity_scores_vader(text)

    # Use Roberta sentiment analysis
    roberta_result = polarity_scores_roberta(text)

    # Combine results or choose the one you prefer
    result = {
        "pipeline_result": {
            "label": pipeline_result[0]["label"],
            "score": pipeline_result[0]["score"],
        },
        "vader_result": vader_result,
        "roberta_result": roberta_result,
    }

    return jsonify(result)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        text = request.form["text"]

        # Use the sentiment analysis pipeline
        pipeline_result = sent_pipeline(text)

        # Use VADER sentiment analysis
        vader_result = polarity_scores_vader(text)

        # Use Roberta sentiment analysis
        roberta_result = polarity_scores_roberta(text)

        # Combine results or choose the one you prefer
        result = {
            "pipeline_result": {
                "label": pipeline_result[0]["label"],
                "score": pipeline_result[0]["score"],
            },
            "vader_result": vader_result,
            "roberta_result": roberta_result,
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
