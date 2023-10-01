from flask import Flask, render_template, request
from recommendation_model import get_recommendations , tfidf_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
import pandas as pd

app = Flask(__name__)
dataset = pd.read_csv("barterdata.csv")

@app.route('/', methods=['GET', 'POST'])
def index():
    input_title = ""
    recommendations = []

    if request.method == 'POST':
        input_title = request.form['input_title']
        recommendations = get_recommendations(input_title, tfidf_matrix, dataset).tolist()

    return render_template('index.html', input_title=input_title, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)