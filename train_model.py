import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

os.makedirs("models", exist_ok=True)

for model_name in ["heart_model.pkl","diabetes_model.pkl","eyesight_model.pkl"]:
    X = np.random.rand(100,3)
    y = np.random.randint(0,2,100)
    clf = RandomForestClassifier()
    clf.fit(X,y)
    joblib.dump(clf, f"models/{model_name}")

print("Models trained and saved in /models folder.")
