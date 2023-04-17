import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
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

# Create a LinearSVC Classifier
model = LinearSVC()

# Train the model using the training sets
model.fit(x.toarray(), train_labels)

# save model
with open('../../../Trained_models/LSVM/lsvm.pkl', 'wb') as f:
    pickle.dump(model, f)

# save vectorizer
with open('../../../Trained_models/LSVM/lsvm_vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

# Predict the response for test dataset
y_pred = model.predict(vectorizer.transform(test_sentences.ravel()).toarray())

# Model Accuracy, how often is the classifier correct?
print("Accuracy:", accuracy_score(test_labels, y_pred))

