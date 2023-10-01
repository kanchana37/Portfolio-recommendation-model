#  importing the libraries
import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset using Pandas
dataset = pd.read_csv('barterdata.csv')  # Replace 'your_dataset.csv' with the actual dataset file path

# Data Cleaning and Preprocessing
def clean_text(text):
    # Remove special characters, HTML tags, punctuation, and irrelevant symbols
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters and punctuation
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace and strip
    return text
# Apply text cleaning to the 'Title' column
dataset['Title Name'] = dataset['Title Name'].apply(clean_text)

# Tokenize the text into individual words
dataset['Tokenized_Title'] = dataset['Title Name'].apply(word_tokenize)

# Remove stopwords
stop_words = set(stopwords.words('english'))
dataset['Filtered_Title'] = dataset['Tokenized_Title'].apply(lambda tokens: [word.lower() for word in tokens if word.lower() not in stop_words])

# Convert all text to lowercase
dataset['Cleaned_Title'] = dataset['Filtered_Title'].apply(lambda tokens: ' '.join(tokens))

# Print the cleaned dataset
print(dataset[['Title Name', 'Cleaned_Title']].head())
# Transform text data into TF-IDF vectors
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(dataset['Cleaned_Title'])

#Calculate cosine similarity
def get_recommendations(input_title, tfidf_matrix, dataset, top_n=5):
    input_vector = tfidf_vectorizer.transform([input_title])
    cosine_similarities = cosine_similarity(input_vector, tfidf_matrix)
    sim_scores = list(enumerate(cosine_similarities[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in sim_scores[1:top_n + 1]]
    top_recommendations = dataset.iloc[top_indices]['Title Name']
    return top_recommendations

# Example: Get recommendations for a given input title

input_title = input("Enter Your input title here")
recommendations= get_recommendations(input_title, tfidf_matrix, dataset)
print(recommendations)