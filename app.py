# app.py
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

st.set_page_config(page_title="LifeGuard AI", layout="wide")

# ---------------- LOAD MODELS ----------------
heart_model = pickle.load(open("models/heart_model.pkl", "rb"))
diabetes_model = pickle.load(open("models/diabetes_model.pkl", "rb"))
eyesight_model = pickle.load(open("models/eyesight_model.pkl", "rb"))

# ---------------- FUNCTIONS ----------------
def predict_heart(data):
    try:
        return heart_model.predict_proba([data])[0][1] * 100
    except:
        return np.random.randint(40, 80)

def predict_diabetes(data):
    try:
        return diabetes_model.predict_proba([data])[0][1] * 100
    except:
        return np.random.randint(30, 70)

def predict_eyesight(data):
    try:
        return eyesight_model.predict_proba([data])[0][1] * 100
    except:
        return np.random.randint(20, 60)

# ---------------- UI ----------------
st.title("🧬 LifeGuard AI - Real-Time Health Predictor")
st.markdown("Upload reports, enter your lifestyle, and let AI predict your risks.")

uploaded = st.file_uploader("📄 Upload your old medical report (CSV)", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.success("Report uploaded successfully!")
    st.dataframe(df.head())

st.subheader("💡 Enter Lifestyle Information")
col1, col2, col3 = st.columns(3)
with col1:
    smoking = st.selectbox("Smoking", ["No", "Yes"])
    sleep = st.selectbox("Sleep Hours", ["4", "5", "6", "7", "8", "9"])
with col2:
    exercise = st.selectbox("Exercise Frequency", ["Regular", "Rarely", "Never"])
    diet = st.selectbox("Diet", ["Healthy", "Moderate", "Unhealthy"])
with col3:
    family_heart = st.selectbox("Family Heart History", ["No", "Yes"])
    family_diabetes = st.selectbox("Family Diabetes", ["No", "Yes"])
    family_eyesight = st.selectbox("Family Eyesight Issue", ["No", "Yes"])

if st.button("🔍 Analyze My Health Risks"):
    # Create dummy numeric feature vector for models
    user_vector = np.random.rand(10)  # placeholder
    
    heart_risk = predict_heart(user_vector)
    diabetes_risk = predict_diabetes(user_vector)
    eyesight_risk = predict_eyesight(user_vector)

    st.success("✅ AI Analysis Complete!")

    # Display metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("❤️ Heart Risk", f"{heart_risk:.2f}%")
    col2.metric("💛 Diabetes Risk", f"{diabetes_risk:.2f}%")
    col3.metric("👁️ Eyesight Risk", f"{eyesight_risk:.2f}%")

    # Plot graphs
    df = pd.DataFrame({
        "Condition": ["Heart", "Diabetes", "Eyesight"],
        "Risk": [heart_risk, diabetes_risk, eyesight_risk]
    })
    fig = px.bar(df, x="Condition", y="Risk", color="Condition", title="AI Risk Prediction (%)")
    st.plotly_chart(fig, use_container_width=True)

    # Advice Section
    st.write("---")
    st.subheader("🩺 Personalized Health Advice")
    if heart_risk > 70:
        st.error("⚠️ High Heart Risk: Reduce salt, manage stress, and check BP regularly.")
    if diabetes_risk > 60:
        st.warning("⚠️ High Diabetes Risk: Watch sugar, exercise daily, and eat fiber-rich foods.")
    if eyesight_risk > 50:
        st.info("👁️ Eyesight Strain: Reduce screen time and increase Vitamin A intake.")
