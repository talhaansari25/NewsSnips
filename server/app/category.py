import os
import pandas as pd
from flask import jsonify, Response

current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, "FinalData.csv")
file_path = os.path.normpath(file_path)
data = pd.read_csv(file_path)

def get_cat(keywords):
   
    keywords_lower = [kw.lower() for kw in keywords]

    relevant_articles = data[data["category"].str.contains('|'.join(keywords_lower), case=False, na=False)]

    relevant_articles_list = relevant_articles.to_dict(orient='records')

    return relevant_articles_list


def myCategory(query):
     
    my_cat_art = get_cat(query)
    return my_cat_art


# import os
# import pandas as pd
# import spacy

# nlp = spacy.load("en_core_web_md")

# current_directory = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(current_directory, "FinalData.csv")
# file_path = os.path.normpath(file_path)
# data = pd.read_csv(file_path)

# def get_cat_nlp(keywords):
#     keywords_doc = [nlp(kw.lower()) for kw in keywords]
#     relevant_articles = []

#     for _, row in data.iterrows():
#         category_doc = nlp(row["category"].lower())
#         similarity_scores = [category_doc.similarity(kw_doc) for kw_doc in keywords_doc]

#         if max(similarity_scores) > 0.7:
#             relevant_articles.append(row.to_dict())

#     return relevant_articles

# def myCategory(query):
#     return get_cat_nlp(query)

