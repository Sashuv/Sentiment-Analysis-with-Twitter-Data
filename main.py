import streamlit as st
import pickle
import pandas as pd
import numpy as np
import nltk
import tkinter
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string
ps = PorterStemmer()

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


def preprocessing(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation and i.isalnum():
            y.append(ps.stem(i))

    return " ".join(y)


st.title("Sentiment Detection ")
input = st.text_area("Enter the text")
if st.button('Predict'):
    preprocessed_text = preprocessing(input)
    vectorized_text = tfidf.transform([preprocessed_text])
    result = model.predict(vectorized_text)[0]
    if (result == "2"):
        st.header("Positive")
    elif (result == "0" or result == "1"):
        st.header("Negative")
