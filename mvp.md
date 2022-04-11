# PeopleSay: Drug Recommendation System

# Minimum Viable Product (MVP)

# Solution Path

To do this, I am using a sample of 100,000 text drug reviews from the UCI dataset, which usually include what previous drug the patient was taking, how the previous drug was making the patient feel better or worse, how the new drug is making the patient feel better or worse or neutral/uncertain, whether the patient is having side effects due to new drug, whether the new drug is making a difference, whether the drug is a miracle, whether the pain associated with the drug has subsided or increased, general bodily feelings and complaints, etc. 

Each review varies from 5 words to over 100 words. The original data were consisted of 161,297 reviews, but 100,000 sample was used instead for faster pre-processing and modeling. More samples might be added down the line for refinement. In the original data of 161,297 reviews, there are 3,436 drugs, 884 conditions, 112,329 reviews, rating scale of 10, 3579 dates with oldest review entry dating back 4/1/2008 and newest entries dating back 9/9/2017, and 389 number of users found reviews helpful. 

# Work Completed

In pre-processing the data, I removed numbers, capital letters, punctuations, white spaces, and common English stopwords in each review.

In choosing between CountVectorizer and TfidfVectorizer, I compared them both in a supervised environment using Logistic Regression and Naive Bayes, but this was not an appropriate way to compare the two vectors, because I was using the "positive" and "negative" rating data to train the models, and not let the models learn the text on their own and classify the topics from there. To correct this step, in my next iteration, I will compare both CountVectorizer and TfidVectorizer in an unsupervised setting with only textual review data. 

For my base NLP Unsupervised model, I implemented CountVectorizer with min_df = 3 (rare words appearing in 3 or fewer documents will be ignored), and used Latent Semantic Analysis (LSA) to model my topics. As a result, the produced LSA topics were as follows:

<img width="300" alt="base_lsa" src="https://user-images.githubusercontent.com/67651332/162654061-a71dcfde-c9eb-4c07-a5c4-4db22bed0f76.PNG">

As for NMF topics, they were as follows:

<img width="300" alt="base_nmf" src="https://user-images.githubusercontent.com/67651332/162654089-09a25d86-eac1-4ae3-a5e8-b73b41d2815c.PNG">

As a rough base model using both LSA and NMF as topic modeling techniques, the topic words do not give much information. Therefore, it is important to revisit the pre-processing step to only extract relevant words such as adjectives (good, bad), comparatives (better, worse), superlatives (best, worst), related feeling and medical words such as (pain, love, like, vomiting, convulsing, relaxed, etc), and common feeling idioms and phrases such as (this works for me, I can relax now, I would recommend this, etc). Therefore, for the next step, CountVectorizer and TFIDF will be compared with SpaCy Part-Of-Speech as text pre-processing tool for relevant word and phrase extraction. 

SpaCy was downloaded and tested on 3 sample reviews. Will only use 3 reviews as a sample with SpaCy moving forward. 

# Moving Forward

I will refine the text pre-processing step with SpaCy as well as other techniques in NLTK. 
I will look into CorEx to anchor "negative" and "positive" feeling words. 
I will look for the best web-based recommendation system that can be built with Streamlit and design its schematic. 
