import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("vader_lexicon")

# Example Tokenization
text = "NLTK is a powerful library for natural language processing."
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Example POS Tagging
tagged = pos_tag(tokens)
print("POS Tags:", tagged)

# Example VADER Sentiment Analysis
sia = SentimentIntensityAnalyzer()
sentiment_scores = sia.polarity_scores(text)
print("Sentiment Scores:", sentiment_scores)
