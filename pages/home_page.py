import streamlit as st

def main():
    st.title("🏠 LifeGuard AI — Home")
    st.write(f"Welcome, **{st.session_state.get('username','User')}**")
    st.write("Use the sidebar to navigate: Predict / Dashboard / Logout")
