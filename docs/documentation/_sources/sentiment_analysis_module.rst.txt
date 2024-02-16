Sentiment Analysis Module
=========================

This module contains functionalities for sentiment analysis, including a trained model for sentiment prediction.

Trained Models
--------------

The module includes the following trained models:

- **sentiment_model.py**: Python file containing the sentiment analysis model.
- **vibe_verdict_model.ipynb**: Jupyter Notebook used for training the VibeVerdict sentiment analysis model.

Model Files
------------

The model files are located in the `sentiment_analysis_module` directory:

- **sentiment_model.py**: Contains the sentiment analysis model code.
- **vibe_verdict_model.ipynb**: Jupyter Notebook with the training code for the VibeVerdict sentiment analysis model.

Data
----

The module uses the following datasets for training the sentiment analysis model:

- **part_1.csv**
- **part_2.csv**
- **part_3.csv**
- **part_4.csv**
- **part_5.csv**
- **part_6.csv**
- **part_7.csv**
- **part_8.csv**
- **part_9.csv**
- **part_10.csv**

Usage
-----

To use the sentiment analysis module in your project:

1. Import the `sentiment_model.py` module.
2. Load the trained model using the provided functions.
3. Perform sentiment analysis on the desired text.


.. code-block:: python

    # Import the sentiment analysis module
    from sentiment_analysis_module.sentiment_model import load_model, predict_sentiment

    # Load the trained model
    model = load_model()

    # Perform sentiment analysis
    text = "This is a positive example."
    result = predict_sentiment(model, text)
    print(result)


.. raw:: html

   <div style="text-align: center;">
       <a class="btn" href="index.html">Go back to home page</a>
   </div>

.. raw:: html

   <div style="text-align: center;">
       <a class="btn" href="http://127.0.0.1:5000/">Go back to base URL</a>
   </div>

