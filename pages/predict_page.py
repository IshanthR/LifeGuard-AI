import joblib
import numpy as np

heart_model = joblib.load("models/heart_model.pkl")
diabetes_model = joblib.load("models/diabetes_model.pkl")
eyesight_model = joblib.load("models/eyesight_model.pkl")

def predict_heart(age, bp, chol):
    return heart_model.predict(np.array([[age,bp,chol]]))[0]

def predict_diabetes(age, glucose, bmi):
    return diabetes_model.predict(np.array([[age,glucose,bmi]]))[0]

def predict_eyesight(left, right):
    return eyesight_model.predict(np.array([[left,right]]))[0]
