
import math
import spacy
from spacy.lang.en import STOP_WORDS
from string import punctuation
from heapq import nlargest
import pandas as pd
from flask import jsonify, Response
import os
from collections import Counter

stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')
punctuation = punctuation + '\n'


#--
def compute_tf(doc):
    words = doc.split()
    tf = Counter(words)
    doc_len = len(words)
    for word in tf:
        tf[word] = tf[word] / doc_len
    return tf

# tf_doc1 = compute_tf(doc1_clean)
# tf_doc2 = compute_tf(doc2_clean)


def compute_tf(doc):
    words = doc.split()
    tf = Counter(words)
    doc_len = len(words)
    for word in tf:
        tf[word] = tf[word] / doc_len
    return tf


def compute_idf(documents):
    N = len(documents)
    idf = {}
    all_words = set([word for doc in documents for word in doc.split()])
    for word in all_words:
        doc_containing_word = sum(1 for doc in documents if word in doc.split())
        idf[word] = math.log(N / (1 + doc_containing_word)) 
    return idf


def compute_tfidf(tf, idf):
    tfidf = {}
    for word, tf_value in tf.items():
        tfidf[word] = tf_value * idf.get(word, 0)  
    return tfidf


def cosine_similarity(doc1, doc2):
   
    documents = [doc1, doc2]
    idf = compute_idf(documents)
    
    
    tf_doc1 = compute_tf(doc1)
    tf_doc2 = compute_tf(doc2)
    
    
    tfidf_doc1 = compute_tfidf(tf_doc1, idf)
    tfidf_doc2 = compute_tfidf(tf_doc2, idf)
    
    
    common_words = set(tfidf_doc1.keys()).union(set(tfidf_doc2.keys()))
    
    
    dot_product = sum(tfidf_doc1.get(word, 0) * tfidf_doc2.get(word, 0) for word in common_words)
    magnitude1 = math.sqrt(sum(tfidf_doc1.get(word, 0) ** 2 for word in common_words))
    magnitude2 = math.sqrt(sum(tfidf_doc2.get(word, 0) ** 2 for word in common_words))
    

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    
    
    return dot_product / (magnitude1 * magnitude2)




def getWordFrequenciesFromDoc(word_frequencies, doc):
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1

def getSentenceScoreFromSentenceTokensWordFreq(sentence_scores, sentence_tokens, word_frequencies):
    for sent in sentence_tokens:
        sent_doc = nlp(sent)
        for word in sent_doc:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text]
                else:
                    sentence_scores[sent] += word_frequencies[word.text]

def processSummary(sentence_tokens, sentence_scores, val):
    select_length = int(len(sentence_tokens) * val)
    my_summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    final_summary = [word.text for word in my_summary for word in nlp(word)]
    my_summary = ' '.join(final_summary)
    return my_summary

def getSummary(text):
    doc = nlp(text)
    word_frequencies = {}
    getWordFrequenciesFromDoc(word_frequencies, doc)

    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / max_frequency  
    sentence_tokens = list({sent.text for sent in doc.sents})
    sentence_scores = {}
    getSentenceScoreFromSentenceTokensWordFreq(sentence_scores, sentence_tokens, word_frequencies)

    mySummary = processSummary(sentence_tokens, sentence_scores, 0.1)

    return mySummary
