import streamlit as st
import os
import joblib
import numpy as np
import pandas as pd
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)
MODELS = {
    "Heart": os.path.join(BASE_DIR,"../models/heart_model.pkl"),
    "Diabetes": os.path.join(BASE_DIR,"../models/diabetes_model.pkl"),
    "Eyesight": os.path.join(BASE_DIR,"../models/eyesight_model.pkl")
}
DOCTORS = {
    "Heart":["Cardiologist — Dr. Arjun Mehta","Dr. Neha Shah"],
    "Diabetes":["Endocrinologist — Dr. Ramesh Rao","Dr. Kavita Patel"],
    "Eyesight":["Ophthalmologist — Dr. Sneha Gupta","Optometrist — Dr. Rajesh Kumar"]
}
HISTORY_FILE = os.path.join(BASE_DIR,"../data/prediction_history.csv")

def predict_disease(disease,X):
    model_file = MODELS[disease]
    if os.path.exists(model_file):
        model = joblib.load(model_file)
        pred = int(model.predict(X)[0])
        prob = model.predict_proba(X)[0][1] if hasattr(model,"predict_proba") else None

        st.subheader("🔎 Result")
        if pred==1:
            st.error("⚠️ Positive / At risk")
        else:
            st.success("✅ Negative / Low risk")

        if prob:
            st.info(f"Risk probability: {prob*100:.2f}%")
            st.bar_chart({"Risk Probability":[prob]})

        st.write("**Suggested doctors:**")
        for d in DOCTORS[disease]:
            st.write(f"- {d}")

        rec = {"timestamp":datetime.now().isoformat(),"user":st.session_state.get("username",""),"disease":disease,"prediction":pred,"probability":prob if prob else ""}
        df = pd.DataFrame([rec])
        if os.path.exists(HISTORY_FILE):
            df_existing = pd.read_csv(HISTORY_FILE)
            df_all = pd.concat([df_existing,df], ignore_index=True)
            df_all.to_csv(HISTORY_FILE,index=False)
        else:
            df.to_csv(HISTORY_FILE,index=False)
    else:
        st.error(f"{disease} model missing!")

def main():
    st.title("💉 Health Predictions")
    choice = st.selectbox("Choose Disease",["Heart","Diabetes","Eyesight"])
    st.write("Enter your data:")

    if choice=="Heart":
        age = st.number_input("Age",18,100,45)
        chol = st.number_input("Cholesterol",100,400,200)
        trestbps = st.number_input("Resting BP",80,220,120)
        X = np.array([[age,chol,trestbps]])
    elif choice=="Diabetes":
        glucose = st.number_input("Glucose",40,300,120)
        bmi = st.number_input("BMI",10,60,25)
        age = st.number_input("Age",18,100,45)
        X = np.array([[glucose,bmi,age]])
    elif choice=="Eyesight":
        age = st.number_input("Age",5,100,30)
        screen = st.number_input("Screen Time (hrs/day)",0,24,4)
        sleep = st.number_input("Sleep (hrs/day)",0,12,7)
        exercise = st.number_input("Exercise (min/day)",0,180,30)
        X = np.array([[age,screen,sleep,exercise]])

    if st.button("Predict"):
        predict_disease(choice,X)
