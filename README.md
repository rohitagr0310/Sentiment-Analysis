# VibeVerdict
A Sentimental Analysis AI Webapp to recognize and tell you your mood 

## Description
This is a web application that uses Natural Language Processing (NLP) to analyze the sentiment of user input. The app will take in text, perform an analysis using machine learning algorithms.

## Installation
To run VibeVerdict locally, you can follow these steps:

### 1. Clone the Repository
```shell
git clone https://github.com/your-username/VibeVerdict.git
cd VibeVerdict
```

### 2. Create a Virtual Environment
It's recommended to use a virtual environment to isolate the project dependencies. Run the following commands to create and activate a virtual environment:

```shell
python -m venv venv
# On Windows: .\venv\Scripts\activate
# On macOS/Linux: source venv/bin/activate
```

### 3. Install Dependencies
Install the required dependencies from the `requirements.txt` file:

```shell
pip install -r requirements.txt
```

### 4. Build Documentation
For documentation updates, run the following command in the root directory:

```shell
sphinx-build -b html docs docs/documentation
```

### 5. Run the Web Application
Now you can run the VibeVerdict web application:

```shell
python app.py
```

The app will be accessible in your web browser at http://localhost:5000.

## Usage
Once the app is running, you can use the sentiment analysis feature by entering text in the provided text box, clicking the "Analyze Sentiment" button, and viewing the results.

## Configuration
Configure your app by editing the `config.py` file.

## Contact
For any inquiries or feedback, please feel free to contact us:

- Email: rohitagr2610@gmail.com
