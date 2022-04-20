import pandas as pd
import numpy as np
import streamlit as st

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("C:/Users/New User/Desktop/Streamlit/st_data_sample.csv")

condition = data.condition

st.title("PeopleRX: A Drug Recommendation System For People By The People")

st.header("This system recommends top 3 most effective medications for a chosen medical condition")

st.subheader("Enter a medical condition:")





def get_drugs():
    cv=CountVectorizer()
    count_matrix=cv.fit_transform(data)
    cosine_sim=cosine_similarity(count_matrix)

    def get_index_from_condition(condition):
        return data[data.condition == condition]['index'].values[0]

    def get_drug_from_index(index):
        return data[data.index == index]['drugName'].values[0]

    condition_index = get_index_from_condition(condition)
    similar_drugs=list(enumerate(cosine_sim[condition_index]))
    sorted_similar_drugs = sorted(similar_drugs, key=lambda x: x[1], reverse=True)
    i=0
    for drug in sorted_similar_drugs:
        print (get_drug_from_index(drug[0]))
        i=i+1
        if i>5:
            break
    return get_drug_from_index(drug[0])

st.selectbox("Condition", condition, index=1)

if st.button("Recommend Me:"):
    get_drugs()


st.text("Disclaimer: \nThis system and its recommendations are not official medical advice. \nPlease use at your own risk.")