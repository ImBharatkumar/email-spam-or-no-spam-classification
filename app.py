"""
Email/SMS Spam Classifier using Streamlit

This script uses a pre-trained machine learning model to classify email/SMS messages as spam or not spam.
The model is trained on a dataset of labeled messages and uses TF-IDF vectorization and a Porter Stemmer for text preprocessing.

Example usage:

1. Run the script and open the Streamlit app in a web browser.
2. Enter an email/SMS message in the text area.
3. Click the "Predict" button to classify the message as spam or not spam.
"""
import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)
tfidf = pickle.load(open('D:\\Projects\\spam or ham\\artifacts\\tfidf.pkl','rb'))
model = pickle.load(open('D:\\Projects\\spam or ham\\artifacts\\model.pkl','rb'))
st.title("Email/SMS Spam Classifier")
input_sms = st.text_area("Enter the message")
if st.button('Predict'):
    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")