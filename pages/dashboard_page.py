import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

HEALTH_FILE = "data/health_data.csv"
DOCTOR_FILE = "data/doctor_list.csv"

def save_health_report(user_id, heart, diabetes, eyesight):
    try:
        df = pd.read_csv(HEALTH_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["user_id","heart","diabetes","eyesight"])
    
    new_row = pd.DataFrame([[user_id, heart, diabetes, eyesight]], 
                           columns=["user_id","heart","diabetes","eyesight"])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(HEALTH_FILE, index=False)

def show_health_trends(user_id):
    try:
        df = pd.read_csv(HEALTH_FILE)
    except FileNotFoundError:
        st.warning("No health data available")
        return
    user_data = df[df['user_id']==user_id]
    if user_data.empty:
        st.info("No health reports yet")
        return
    fig, ax = plt.subplots()
    sns.lineplot(data=user_data[['heart','diabetes','eyesight']], ax=ax)
    ax.set_ylabel("Risk Level (0=Low,1=High)")
    st.pyplot(fig)

def suggest_doctors():
    try:
        doctors = pd.read_csv(DOCTOR_FILE)
    except FileNotFoundError:
        doctors = pd.DataFrame([["Dr. A","Cardiologist"],["Dr. B","Endocrinologist"],["Dr. C","Ophthalmologist"]],
                               columns=["Name","Speciality"])
        doctors.to_csv(DOCTOR_FILE,index=False)
    st.subheader("Recommended Doctors")
    st.table(doctors)
