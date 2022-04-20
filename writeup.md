# PeopleRX: A Drug Recommendation System For The People by The People
Mai Tran

# Abstract

# Design
1. Clean data - both downloaded train and test data were combined into one dataset together. Together, the final dataset were 215,063 rows with 7 columns. Regular Expressions (RegEx) was used to remove numbers, capital letters, and punctuations in reviews. Rows with NaN values were removed. It was found there were 1194 NaN rows. Long reviews or reviews longer than 250 words were removed. Removal of drug names from reviews was considered but was not implemented due to the large number of drug names. 

2. Explanatory Data Analysis (EDA) - For the original dataset of 215,063 rows, there were 3,671 unique drugs; 916 unique conditions; 131,932 reviews; 3,579 unique entry dates; and 397 unique usefulCount entries. As for most common medical conditions, the top 6 most common conditions are as follows: 


   1. Birth Control
   2. Depression
   3. Pain
   4. Anxiety
   5. Acne
   6. Bipolar Disorder

- These top 6 conditions and their related side effects are strongly correlated to the top 6 common topics discovered by the model using Latent Semantic Analysis (LSA) as later shown in Step 5. This comparison step is an excellent validation step in measuring performance of this CountVectorizer-LSA model. 

3. Document-term matrix using Countvectorizer - The best document-term matrix was created using CountVectorizer with custom stopwords, max_df = .75, min_df = .02, and ngram_range=(1,3). The resultant document-term matrix was 212,850 rows and 304 columns. The following are custom stopwords added to NLTK default stopwords list to help in topic modeling refinement process:

   - like, just, ive, im, got, day, days, time, times, years, weeks, took, taking, taken, side effects, get, month, went, ago, feel, felt, one, hours, using, started, back, dont, since, life, never, really, medicine, dose, much, still, doctor, dr, meds. 


4. Topic modeling using Latent Semantic Analysis (LSA) via TruncatedSVD - Six topics were modeled from the document-term matrix using Latent Semantic Analysis (LSA) via TruncatedSVD. 


  - In the first iteration:
    - first topic: "im, day, taking, ive, mg"
    - second topic: "mg, pain, day, anxiety, sleep"
    - third topic: "pain, period, days, got, birth"
    - fourth topic: "im, ive, pain, years, and feel"
    - fifth topic: "day, im, days, period, like"
    - sixth topic: "mg, day, ive, control, and birth"

  - After 20 iterations, the final iteration yielded the following: 
    - first topic: "pain, period, weight, control, bad"
    - second topic: "pain, sleep, severe, night, relief"
    - third topic: "pain, period, birth, control, birth control"
    - fourth topic: "weight, gain, lbs, weight gain, lost"
    - fifth topic: "control, birth, birth control, anxiety, depression"
    - sixth topic: "acne, skin, face, use, clear"


5. Topic model matrix created through refinement of previous steps 3 and 4 - As shown above, after 20 iterations, LSA yielded the following top 6 common topics in the drug reviews:

    1. Period
    2. Pain
    3. Birth control
    4. Weight
    5. Mood (Anxiety/Depression)
    6. Acne
  
  Note: upon closer assessment, #1 should be Pain and #2 should be Sleep. This note is for future refinement of the model. 

6. Recommendation system created using Content-Based Filtering - A content-based filtering recommendation program was successfully built and tested on a smaller topic-model dataframe made of 100,000 rows. There was a recommendation step that utilized a smaller topic-model dataframe made of only 3 PCA features and pairwise_distances, this recommendation step was the most accurate step yielding very accurate top 3 recommendations for "Birth Control" condition (Ortho Tri-Cyclen Lo, Seasonique, and Depo-Provera). Another program written using the original topic-model dataframe of 100,000 rows and 9 features/columns with cosine_similarity, this program was not as accurate and buggy. Also, this program only yielded the recommended drug names whereas the PCA program yielded drug name as well as the topics/experiences (period, pain, birth control, weight, mood, acne) related with the drug name. In summary, the first program with a smaller topic-model dataframe with 3 PCA features and pairwise distances was the most accurate program. 

7. Web Application of recommendation system using Streamlit - Graphical User Interface (GUI) was successfully built for the recommendation system, but the recommendation Python code needs closer examination and further debugging. In communication, a GUI of the web application is shown. 

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
1. Regular Expressions for text cleaning
2. CountVectorizer - for document-matrix modeling
3. TruncatedSVD - for Latent Semantic Analysis (LSA) topic modeling and generating a topic-model matrix
4. pairwise_distances - recommendation method with pairwise_distances comparison for PCA-based features was found to be the fastest and most accurate
5. cosine_similarity - recommendation method with cosine_similarty comparison with topic-model matrix features was found to be not as fast nor as accurate as the previous recommendation method

For future work on recommendation performance comparison:
1. SpaCy
2. VADER
3. CorEX
4. TFIDF
5. LDA
6. NMF

# Tools
- Numpy and Pandas for data manipulation
- NLTK for Natural Language Processing (NLP) including stopwords for word/text filtering and cleaning
- Regular Expressions for text cleaning
- CountVectorizer for text feature extraction and document-matrix formation
- TruncatedSVD for Latent Semantic Analysis (LSA) or topic modeling
- cosine_similarity for recommendation system
- Streamlit as web-application of recommendation system

# Communication
LSA Topic Modeling First Iteration:

<img width="250" alt="topic_model_first_iter" src="https://user-images.githubusercontent.com/67651332/164134765-4c5ba764-a83a-41a1-b9fe-3c129e70569c.PNG">

LSA Topic Modeling After 20 Iterations:

<img width="400" alt="topic_model_last_iter" src="https://user-images.githubusercontent.com/67651332/164134813-e45c265c-c6c8-41fd-bd87-0383dc04d5cd.PNG">


This is a GUI of a web-based application of the PeopleRX Recommendation System built in Streamlit:

<img width="550" alt="streamlit_gui" src="https://user-images.githubusercontent.com/67651332/164134500-55fb1f2b-605c-4090-8af6-3844a5d51e06.PNG">
