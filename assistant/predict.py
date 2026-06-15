import joblib

model = joblib.load("model/intent_model.pkl")

def predict_intent(text):
    return model.predict([text])[0]