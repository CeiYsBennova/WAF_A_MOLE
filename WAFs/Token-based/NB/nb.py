import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer

# Load dataset
df = pd.read_csv('../../../Dataset/SQLi.csv')

# Split dataset into training set and test set
train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

# split train sentences and test sentence , and labels
train_sentences = train_data['Sentence'].values.reshape(-1, 1)
train_labels = train_data['Label'].values

test_sentences = test_data['Sentence'].values.reshape(-1, 1)
test_labels = test_data['Label'].values

# vectorize sentences
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(train_sentences.ravel())

# Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets
model.fit(x.toarray(), train_labels)

# save model
with open('../../../Trained_models/nb.pkl', 'wb') as f:
    pickle.dump(model, f)

# save vectorizer
with open('../../../Trained_models/nb_vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)


# Predict the response for test dataset
y_pred = model.predict(vectorizer.transform(test_sentences.ravel()).toarray())

# Model Accuracy, how often is the classifier correct?
print("Accuracy:", accuracy_score(test_labels, y_pred))

# predict a single sentence
sentence = ["Union Select 1,2,3,4,id(),--+-"]
if model.predict(vectorizer.transform(sentence).toarray()) == 1:
    print("SQLi")
else:
    print("Normal")
