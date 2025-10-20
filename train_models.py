import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Make sure model folder exists
os.makedirs("models", exist_ok=True)

# -----------------------------
# HEART DISEASE MODEL
# -----------------------------
try:
    heart = pd.read_csv("datasets/heart.csv")
    X_heart = heart.drop("target", axis=1)
    y_heart = heart["target"]

    X_train, X_test, y_train, y_test = train_test_split(X_heart, y_heart, test_size=0.2, random_state=42)
    heart_model = RandomForestClassifier()
    heart_model.fit(X_train, y_train)
    acc = heart_model.score(X_test, y_test)
    print(f"❤️ Heart Model Trained | Accuracy: {acc:.2f}")

    pickle.dump(heart_model, open("models/heart_model.pkl", "wb"))
except Exception as e:
    print("⚠️ Error training Heart model:", e)

# -----------------------------
# DIABETES MODEL
# -----------------------------
try:
    diabetes = pd.read_csv("datasets/diabetes.csv")
    X_diabetes = diabetes.drop("Outcome", axis=1)
    y_diabetes = diabetes["Outcome"]

    X_train, X_test, y_train, y_test = train_test_split(X_diabetes, y_diabetes, test_size=0.2, random_state=42)
    diabetes_model = RandomForestClassifier()
    diabetes_model.fit(X_train, y_train)
    acc = diabetes_model.score(X_test, y_test)
    print(f"💧 Diabetes Model Trained | Accuracy: {acc:.2f}")

    pickle.dump(diabetes_model, open("models/diabetes_model.pkl", "wb"))
except Exception as e:
    print("⚠️ Error training Diabetes model:", e)

# -----------------------------
# EYESIGHT MODEL (synthetic dataset)
# -----------------------------
import numpy as np
np.random.seed(42)
eyesight = pd.DataFrame({
    "age": np.random.randint(18, 70, 200),
    "screen_time": np.random.randint(1, 10, 200),
    "sleep_hours": np.random.randint(4, 9, 200),
    "reading_habit": np.random.randint(0, 2, 200),
})
eyesight["risk"] = (0.03 * eyesight["age"] + 
                    0.5 * eyesight["screen_time"] - 
                    0.4 * eyesight["sleep_hours"] + 
                    2 * eyesight["reading_habit"] + 
                    np.random.randn(200) * 2 > 5).astype(int)

X_eye = eyesight.drop("risk", axis=1)
y_eye = eyesight["risk"]

X_train, X_test, y_train, y_test = train_test_split(X_eye, y_eye, test_size=0.2, random_state=42)
eye_model = RandomForestClassifier()
eye_model.fit(X_train, y_train)
acc = eye_model.score(X_test, y_test)
print(f"👁️ Eyesight Model Trained | Accuracy: {acc:.2f}")

pickle.dump(eye_model, open("models/eyesight_model.pkl", "wb"))

print("\n✅ All Models Saved Successfully in /models folder!")
