import pickle
from sklearn.feature_extraction.text import CountVectorizer

# load model
with open('../../../Trained_models/nb.pkl', 'rb') as f:
    model = pickle.load(f)

# load vectorizer
with open('../../../Trained_models/nb_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# predict a single sentence
sentence = input("Enter a sentence: ")
if model.predict(vectorizer.transform([sentence]).toarray()) == 1:
    print("SQLi")
else:
    print("Normal")