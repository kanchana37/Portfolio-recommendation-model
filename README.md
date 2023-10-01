# Portfolio-recommendation-model

Portfolio Recommendation Model
Project Overview
This project implements a recommendation system for a portfolio dataset using cosine similarity with TF-IDF. The system is designed to recommend similar portfolios to a user based on the title of their portfolio.

## How It Works

### The system operates through the following steps:

1. Data Preprocessing: The portfolio dataset is preprocessed to remove stop words and special characters. This step ensures that the text data is clean and ready for analysis.

2. TF-IDF Vectorization: The text data is converted into TF-IDF (Term Frequency-Inverse Document Frequency) vectors. TF-IDF is a numerical representation of the importance of words in a document relative to a collection of documents (in this case, portfolios).

3. Cosine Similarity Calculation: To recommend similar portfolios to a user, the system calculates the cosine similarity between the user's portfolio vector and all other portfolio vectors in the dataset. Cosine similarity measures the cosine of the angle between two non-zero vectors and provides a measure of similarity between them.

4. Top Recommendations: The system identifies the top 5 most similar portfolios based on cosine similarity and returns them to the user as recommendations.

## Benefits

1. Discover Relevant Portfolios: Easily find portfolios related to your interests and profession.

2. Time and Effort Savings: Save time searching for portfolios, making information discovery efficient.

3. Industry Exploration: Explore various industries and professions through diverse portfolios.

4. Mentorship and Collaboration: Identify potential mentors or collaborators based on portfolio recommendations.

## How to Use?:

1. Setup Environment: Create a Conda environment for the project.

2. Install Dependencies: Install project dependencies listed in requirements.txt.

3. Run Model: Execute recommendation_model.py to build the recommendation model.

4. Launch Web App: Start the web application by running app.py, enabling users to explore portfolio recommendations through the user-friendly interface.

## Result
](https://drive.google.com/file/d/1TwbMDFpV29mfwEfszQW_NGG5_FLbliso/view?usp=sharing)https://drive.google.com/file/d/1TwbMDFpV29mfwEfszQW_NGG5_FLbliso/view?usp=sharing
