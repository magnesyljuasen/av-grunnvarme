import streamlit as st
from scripts._utils import electricity_database

def elprice():
    st.title("Dagens strømpris")
    electricity_database()
    st.markdown("---")