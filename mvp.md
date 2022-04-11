# PeopleSay: Drug Recommendation System

# Minimum Viable Product (MVP)

# Solution Path

To do this, I am using a sample of 100,000 text drug reviews from the UCI dataset, which usually include what previous drug the patient was taking, how the previous drug was making the patient feel better or worse, how the new drug is making the patient feel better or worse or neutral/uncertain, whether the patient is having side effects due to new drug, whether the new drug is making a difference, whether the drug is a miracle, whether the pain associated with the drug has subsided or increased, general bodily feelings and complaints, etc. 

Each review varies from 5 words to over 100 words. The original data were consisted of 161,297 reviews, but 100,000 sample was used instead for faster pre-processing and modeling. More samples might be added down the line for refinement. In the original data of 161,297 reviews, there are 3,436 drugs, 884 conditions, 112,329 reviews, rating scale of 10, 3579 dates with oldest review entry dating back 4/1/2008 and newest entries dating back 9/9/2017, and 389 number of users found reviews helpful. 

# Work Completed

In pre-processing the data, I removed numbers, capital letters, punctuations, and white spaces. 
