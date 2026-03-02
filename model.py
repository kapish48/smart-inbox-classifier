import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
import pickle

df = pd.read_csv("support_tickets.csv")
X = df["text"]
y = df["category"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
 
#training the nlp model
print("Training the NLP Model")
model.fit(X_train, y_train)

#evaluating 
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"model accuracy is {accuracy:.2%}")
sample = ["my internet is slow today"]
prediction = model.predict(sample)
print(f"Test Prediction for '{sample[0]}': {prediction[0]}")

with open("nlp_model.pkl", "wb") as f:
    pickle.dump(model, f)