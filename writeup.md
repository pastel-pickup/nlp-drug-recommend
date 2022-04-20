# PeopleRX: A Drug Recommendation System For The People by The People
Mai Tran

# Abstract

# Design
1. Clean data - both downloaded train and test data were combined into one dataset together. Together, the final dataset were 215,063 rows with 7 columns. Regular Expressions (RegEx) was used to remove numbers, capital letters, and punctuations in reviews. Rows with NaN values were removed. It was found there were 1194 NaN rows. Long reviews or reviews longer than 250 words were removed. Removal of drug names from reviews was considered but was not implemented due to the large number of drug names. 


2. Explanatory Data Analysis (EDA) - 
4. Document-term matrix using Countvectorizer - 
5. Topic modeling using Latent Semantic Analysis (LSA) via TruncatedSVD - 
6. Topic model matrix created through refinement of previous steps 3 and 4 - 
7. Recommendation system created using Content-Based Filtering - 
8. Web Application of recommendation system using Streamlit - 

# Data
- The dataset of drug reviews from University of California Irvine Machine Learning Repository was created by Surya Kallumadi and Felix Gräßer. 
- Here is the link to the dataset: https://archive.ics.uci.edu/ml/datasets/Drug+Review+Dataset+%28Drugs.com%29
- Each row of the dataset is made of the following features or columns:
1. drugName (categorical): name of drug
2. condition (categorical): name of condition
3. review (text): patient review
4. rating (numerical): 10 star patient rating
5. date (date): date of review entry
6. usefulCount (numerical): number of users who found review useful
- For analysis and modeling, there were 212,850 reviews or data points used after cleaning. The resultant document-matrix from CountVectorizer was 212,850 rows by 304 columns. The same document-matrix was used for LSA modeling. 
- For recommendation, various number of rows of the topic-model matrix were tested for robustness: 100,000 rows; 10,000 rows; 1,000 rows; 100 rows; and 10 rows. 
- For Streamlit integration, since 200MB was the maximum storage allowed on Streamlit, smaller dataframes of the topic-model matrix were tested for efficiency and robustness. 

# Algorithms

# Tools
- Numpy and Pandas for data manipulation
- NLTK for Natural Language Processing (NLP) including stopwords for word/text filtering and cleaning
- Regular Expressions for text cleaning
- CountVectorizer for text feature extraction and document-matrix formation
- TruncatedSVD for Latent Semantic Analysis (LSA) or topic modeling
- cosine_similarity for recommendation system
- Streamlit as web-application of recommendation system

# Communication

