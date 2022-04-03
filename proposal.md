# PeopleSay: A Drug Recommendation System For The People By The People

# Question/Need:
# What is the question behind your analysis or model and what practical impact will your work have?
- What drugs do people react positively to, give positive reviews for, and want to recommend for a particular medical condition? 
- This drug recommendation system serves as a clinical decision support (CDS) system to help both healthcare providers and patients to be more informed in choosing the most appropriate drugs for the patient's medical conditions. This PeopleSay drug recommendation system will serve as a backup reference to supplement the medical knowledge of the healthcare providers, and to help them make better decisions for their patients, allow them to spend more quality care time together, and to improve the overall care experience of the patient. 

# Who is your client and how will that client benefits from exploring this question or building this model/system?
- My client is CVS, which is looking to provide more online healthcare services for its customers. Both of the healthcare provider and the customer of CVS could benefit from this PeopleSay recommendation system to help them pick out drugs that are most suitable for them. 

# Data Description:
# What dataset(s) do you plan to use, and how will you obtain the data? Please include a link! (The link can be to the dataset you’re downloading, the site you’re scraping, etc.)
- I am using a dataset of drug reviews from University of California Irvine Machine Learning Repository created by Surya Kallumadi and Felix Gräßer. 
- https://archive.ics.uci.edu/ml/datasets/Drug+Review+Dataset+%28Drugs.com%29

# What is an individual sample/unit of analysis in this project? In other words, what does one row or observation of the data represent?
- An individual sample of analysis is as follows:
1. drugName (categorical): name of drug
2. condition (categorical): name of condition
3. review (text): patient review
4. rating (numerical): 10 star patient rating
5. date (date): date of review entry
6. usefulCount (numerical): number of users who found review useful

# What characteristics/features do you expect to work with? In other words, what are your columns of interest?
- My columns of interest are: 1) drugName, 2) condition, 3) review, 4) rating, and 6) usefulCount

# If modeling, what will you predict as your target?
- If modeling, positive drug reviews are my target. 

# Tools:
# How do you intend to meet the tools requirement of the project?
# Are you planning in advance to need or use additional tools beyond those required?

# MVP Goal:
# What would a minimum viable product (MVP) look like for this project?
