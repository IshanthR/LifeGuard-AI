import streamlit as st
import pandas as pd
import os

HISTORY_FILE = os.path.join(os.path.dirname(__file__),"../data/prediction_history.csv")

def main():
    st.title("📊 Dashboard — Prediction History")
    if os.path.exists(HISTORY_FILE):
        df = pd.read_csv(HISTORY_FILE)
        user_df = df[df["user"]==st.session_state.get("username","")]
        if not user_df.empty:
            st.dataframe(user_df)
        else:
            st.info("No prediction history yet.")
    else:
        st.info("No prediction history file yet.")
