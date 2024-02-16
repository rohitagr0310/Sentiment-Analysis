Setting Up NLTK Environment Documentation
=========================================

This documentation provides step-by-step instructions for setting up a Python environment, installing NLTK (Natural Language Toolkit), and running a sample program that involves NLTK for tokenization, POS tagging, and sentiment analysis.

Creating a Virtual Environment
-------------------------------

1. Open a terminal or command prompt.

2. Navigate to the project directory (if not already there).

3. Create a virtual environment using the following command:

   ::

      python -m venv venv

4. Activate the virtual environment:

   - On Windows:

     ::

       venv\Scripts\activate

   - On macOS/Linux:

     ::

       source venv/bin/activate

Installing NLTK and Dependencies
---------------------------------

5. With the virtual environment activated, install NLTK and its components:

   ::

      pip install nltk

6. Download NLTK data for tokenization, POS tagging, and sentiment analysis. In a Python script or interactive environment, run the following:

   ::

      import nltk

      nltk.download('punkt')
      nltk.download('averaged_perceptron_tagger')
      nltk.download('vader_lexicon')

   Expected Output:

   ::

      [nltk_data] Downloading package punkt to
      [nltk_data]     C:\Users\rohit\AppData\Roaming\nltk_data...
      [nltk_data]   Package punkt is already up-to-date!
      [nltk_data] Downloading package averaged_perceptron_tagger to
      [nltk_data]     C:\Users\rohit\AppData\Roaming\nltk_data...
      [nltk_data]   Package averaged_perceptron_tagger is already up-to-
      [nltk_data]       date!
      [nltk_data] Downloading package vader_lexicon to
      [nltk_data]     C:\Users\rohit\AppData\Roaming\nltk_data...
      [nltk_data]   Package vader_lexicon is already up-to-date!

Running the Existing Test Script
--------------------------------

7. There is already a test script available for NLTK in the `test` folder. The file name is `nltk_test.py`. To run the test script, execute the following command in the terminal:

   ::

      python test/nltk_test.py

   Expected Output:

   ::

      [nltk_data] Downloading package punkt to
      [nltk_data]     C:\Users\rohit\AppData\Roaming\nltk_data...
      [nltk_data]   Package punkt is already up-to-date!
      [nltk_data] Downloading package averaged_perceptron_tagger to
      [nltk_data]     C:\Users\rohit\AppData\Roaming\nltk_data...
      [nltk_data]   Package averaged_perceptron_tagger is already up-to-
      [nltk_data]       date!
      [nltk_data] Downloading package vader_lexicon to
      [nltk_data]     C:\Users\rohit\AppData\Roaming\nltk_data...
      [nltk_data]   Package vader_lexicon is already up-to-date!
      Tokens: ['NLTK', 'is', 'a', 'powerful', 'library', 'for', 'natural', 'language', 'processing', '.']
      POS Tags: [('NLTK', 'NNP'), ('is', 'VBZ'), ('a', 'DT'), ('powerful', 'JJ'), ('library', 'NN'), ('for', 'IN'), ('natural', 'JJ'), ('language', 'NN'), ('processing', 'NN'), ('.', '.')]
      Sentiment Scores: {'neg': 0.0, 'neu': 0.531, 'pos': 0.469, 'compound': 0.6486}



.. raw:: html

   <div style="text-align: center;">
       <a class="btn" href="index.html">Go back to home page</a>
   </div>

.. raw:: html

   <div style="text-align: center;">
       <a class="btn" href="http://127.0.0.1:5000/">Go back to base URL</a>
   </div>

