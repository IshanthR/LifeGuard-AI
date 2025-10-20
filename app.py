import streamlit as st
import importlib.util
import sys
import os

st.set_page_config(page_title="LifeGuard AI", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""

def load_page(page_path):
    spec = importlib.util.spec_from_file_location("page", page_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["page"] = module
    spec.loader.exec_module(module)
    module.main()

PAGE_FOLDER = os.path.join(os.getcwd(),"pages")

if not st.session_state["logged_in"]:
    load_page(os.path.join(PAGE_FOLDER,"login_page.py"))
else:
    page = st.sidebar.selectbox("Navigate", ["Home","Predict","Dashboard","Logout"])
    if page=="Home":
        load_page(os.path.join(PAGE_FOLDER,"home_page.py"))
    elif page=="Predict":
        load_page(os.path.join(PAGE_FOLDER,"predict_page.py"))
    elif page=="Dashboard":
        load_page(os.path.join(PAGE_FOLDER,"dashboard_page.py"))
    elif page=="Logout":
        st.session_state.clear()
        st.experimental_rerun()
