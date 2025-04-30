
import os
import pandas as pd

current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, "FinalData.csv")
file_path = os.path.normpath(file_path)


df = pd.read_csv(file_path)
def getRecc(keywords):
    related_articles = []

    sorted_keywords = sorted(keywords, key=keywords.get, reverse=True)
    for keyword in sorted_keywords:
        found_articles = df[df['title'].str.contains(keyword, case=False)]        
        if not found_articles.empty:
           
            for index, row in found_articles.head(2).iterrows():
                article_dict = row.to_dict()  # Convert the row to a dictionary
                article_dict['row_no'] = index  # Add the row number
                related_articles.append(article_dict) 

    return related_articles  


def myRec(listKey):
   
    rec_art = getRecc(listKey)

    return rec_art