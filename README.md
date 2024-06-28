# Email/SMS Spam Classifier using Streamlit
* Overview
This project is a Streamlit-based application that classifies email/SMS messages as spam or not spam using a pre-trained machine learning model. The model is trained on a dataset of labeled messages and uses TF-IDF vectorization and a Porter Stemmer for text preprocessing.

* Features
User-friendly interface: Enter an email/SMS message in the text area and click the "Predict" button to classify the message as spam or not spam.
Pre-trained model: The model is trained on a dataset of labeled messages, ensuring accurate classification results.
Text preprocessing: The application uses TF-IDF vectorization and a Porter Stemmer to preprocess the input text, improving the model's performance.

* How to Use
Run the script and open the Streamlit app in a web browser.
Enter an email/SMS message in the text area.
Click the "Predict" button to classify the message as spam or not spam.

* Technical Details
Model: The pre-trained model is stored in model.pkl and is loaded using pickle.
TF-IDF Vectorizer: The TF-IDF vectorizer is stored in tfidf.pkl and is loaded using pickle.
Text Preprocessing: The transform_text function is used to preprocess the input text, which includes:
Converting the text to lowercase
Tokenizing the text
Removing non-alphanumeric characters
Removing stopwords and punctuation
Stemming the words using the Porter Stemmer

* Requirements
Streamlit: The application is built using Streamlit, a Python library for building web applications.
NLTK: The application uses NLTK for text preprocessing, including tokenization and stemming.
Pickle: The application uses Pickle to load the pre-trained model and TF-IDF vectorizer.

* Acknowledgments
The pre-trained model and TF-IDF vectorizer are stored in artifacts directory. You can update these files with your own trained model and vectorizer.
I hope this helps