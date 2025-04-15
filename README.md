import streamlit as st
import openai

openai.api_key = st.secrets["openai_api_key"]

st.title("🧠 AI Idea Validator")

idea = st.text_input("Enter your project idea:")

if st.button("Validate"):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role":"user","content":f"Is '{idea}' a good business idea?"}]
    )
    st.write(response.choices[0].message.content.strip())
