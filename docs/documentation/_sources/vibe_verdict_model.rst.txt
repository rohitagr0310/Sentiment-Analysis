VibeVerdict Model Notebook
==========================

This document provides an overview of the Jupyter Notebook `vibe_verdict_model.ipynb` which is used for training the sentiment analysis model in the VibeVerdict project.

Introduction
------------

The `vibe_verdict_model.ipynb` Jupyter Notebook contains the code for training the sentiment analysis model using various tools and libraries such as nltk, transformers, and more.

Notebook Overview
-----------------

1. **Data Loading and Exploration:**
   - The notebook starts with loading and exploring the dataset (`part_1.csv` to `part_10.csv`).
   - Visualization of the count of reviews by stars.

2. **Natural Language Processing (NLP) with NLTK:**
   - Tokenization, POS tagging, and Named Entity Recognition (NER) using the Natural Language Toolkit (NLTK).
   - Sentiment analysis using the VADER sentiment intensity analyzer.
   - Visualization of sentiment analysis results.

3. **Sentiment Analysis with Transformers:**
   - Utilizing the Hugging Face Transformers library.
   - Loading the pre-trained sentiment analysis model (`cardiffnlp/twitter-roberta-base-sentiment`).
   - Running the model on an example text and displaying the scores.

4. **Comparing NLTK and Transformers Results:**
   - Iterating through the dataset to perform sentiment analysis with both NLTK and Transformers.
   - Creating a DataFrame with the results.

5. **Visualization and Analysis:**
   - Visualizing compound scores and individual sentiment scores.
   - Pair plot for exploring relationships between different sentiment scores.

6. **Additional Sentiment Analysis:**
   - Using the Transformers pipeline for sentiment analysis.

Usage
-----

To run the Jupyter Notebook and train the VibeVerdict sentiment analysis model, follow these steps:

1. Install the required dependencies mentioned in the `requirements.txt`.
2. Open the Jupyter Notebook using a Jupyter environment.
3. Execute each cell in the notebook sequentially.


.. code-block:: python

    # Install required dependencies
    pip install -r requirements.txt

    # Open the Jupyter Notebook
    jupyter notebook

    # Execute each cell in the notebook
