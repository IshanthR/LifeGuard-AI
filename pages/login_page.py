import streamlit as st
import pandas as pd
import os

USER_FILE = os.path.join(os.path.dirname(__file__), "../data/users.csv")

def ensure_users_file():
    if not os.path.exists(USER_FILE):
        os.makedirs(os.path.dirname(USER_FILE), exist_ok=True)
        pd.DataFrame(columns=["username","password"]).to_csv(USER_FILE,index=False)

def load_users():
    ensure_users_file()
    return pd.read_csv(USER_FILE)

def save_user(username,password):
    df = load_users()
    if username in df["username"].values:
        return False
    df.loc[len(df)] = [username,password]
    df.to_csv(USER_FILE,index=False)
    return True

def validate_user(username,password):
    df = load_users()
    return ((df["username"]==username) & (df["password"]==password)).any()

def main():
    st.title("🔐 LifeGuard AI — Login / Sign Up")
    choice = st.radio("Action", ["Login","Sign Up"], horizontal=True)

    if choice=="Login":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if validate_user(username,password):
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.success(f"Welcome {username}!")
                st.experimental_rerun()
            else:
                st.error("Invalid username or password.")
    else:
        username = st.text_input("New Username")
        password = st.text_input("New Password", type="password")
        if st.button("Sign Up"):
            if save_user(username,password):
                st.success("Account created successfully! Login now.")
            else:
                st.error("Username already exists.")
