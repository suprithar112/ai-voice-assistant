import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("dataset/intents.csv")

X = df["text"]
y = df["intent"]

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

model.fit(X, y)

joblib.dump(
    model,
    "model/intent_model.pkl"
)

print("Model trained successfully")