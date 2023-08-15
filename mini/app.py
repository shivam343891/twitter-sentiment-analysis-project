from flask import Flask, render_template, request
import pickle
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

def preprocess_tweet(tweet):
    tweet = re.sub(r'#\w+|\W', ' ', tweet)
    tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet)
    tweet = tweet.lower()
    tokens = word_tokenize(tweet)
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in stemmed_tokens]
    preprocessed_tweet = ' '.join(lemmatized_tokens)
    return preprocessed_tweet

# Define the filename of the pickle file
model_filename = 'SVC (TF-IDF).pickle'

# Load the classifier from the pickle file
with open(model_filename, 'rb') as f:
    classifier = pickle.load(f)

# Define the filename of the pickle file
vectorizer_filename = 'SVC (TF-IDF)_tfidf_vectorizer.pickle'

# Load the TF-IDF vectorizer from the pickle file
with open(vectorizer_filename, 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

def predict_sentiment(sentence):
    preprocessed_sentence = preprocess_tweet(sentence)
    sentence_vectorized = tfidf_vectorizer.transform([preprocessed_sentence])
    sentiment = classifier.predict(sentence_vectorized)[0]
    if sentiment ==1:
        return ("Positive")
    elif sentiment ==0:
        return ("Negative")


app = Flask(__name__, template_folder='template')

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for handling the form submission
@app.route('/predict', methods=['POST'])
def predict_sentiment_route():
    sentence = request.form['inp']  # Get the input sentence from the form
    sid = predict_sentiment(sentence)
    return render_template('index.html', message=sid)

@app.route('/results')
def show_results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(port=5500, debug=True) 