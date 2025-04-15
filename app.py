import streamlit as st

st.title("Idea Validator is Loading...")

try:
    import openai
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    st.success("API key loaded successfully")
except Exception as e:
    st.error(f"API key issue: {e}")
import streamlit as st
import openai
