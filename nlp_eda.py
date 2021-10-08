import numpy as np
import pandas as pd
import nltk
nltk.download('stopwords')
import string
import re
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def wordcloud_display(df, column_name):
    font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
    All_words = ""
    All_words += " ".join(df[column_name])
    wordcloud = WordCloud(background_color='white').generate(All_words)
    plt.figure(figsize=(15,15))
    plt.title("WordCloud of " +column_name, fontdict=font)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    return plt.show()

def remove_punctuation(text):
    no_punct=[words for words in text if words not in string.punctuation]
    words_wo_punct=''.join(no_punct)
    return words_wo_punct

def tokenize(text):
    split=re.split("\W+",text) 
    return split

stop_words = set(nltk.corpus.stopwords.words('english'))
stop_words.add('subject')
stop_words.add('http')
def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in stop_words])

def lower(text):
    return text.lower()

def remove_numbers(dataframe,column_name):
    return (dataframe[column_name].apply(lambda x: re.sub('W*dw*','',x)))

def remove_extraspace(dataframe,column_name):
    return (dataframe[column_name].apply(lambda x: re.sub(' +', ' ', x)))
             
                      
def remove_url(dataframe,column_name):
    return (dataframe[column_name].apply(lambda x: re.sub(r'https?://(www\.)?(\w+)(\.\w+)',' ',x)))

def remove_specific_word(dataframe,column_name, word):
    return (dataframe[column_name].str.replace(word, ' '))

def remove_email_id(dataframe,column_name):
    return (dataframe[column_name].apply(lambda x: re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',' ',x)))

porter_stemmer = PorterStemmer()
def stem_sentences(sentence):
    tokens = sentence.split()
    stemmed_tokens = [porter_stemmer.stem(token) for token in tokens]
    return ' '.join(stemmed_tokens)




    
                                       
            