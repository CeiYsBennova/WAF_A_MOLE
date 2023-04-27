import pickle

#load model
#with open('../../../Trained_models/GSVM/gsvm.pkl', 'rb') as f:
#    model = pickle.load(f)

with open('../../../../WafaMole_dataset/gsvm.pkl', 'rb') as f:
    model = pickle.load(f)

#load vectorizer
with open('../../../Trained_models/GSVM/gsvm_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# predict a single sentence
sentence = ["Union Select 1,2,3,4,id(),--+-"]
if model.predict(vectorizer.transform(sentence).toarray()) == 1:
    print("SQLi")
else:
    print("Normal")