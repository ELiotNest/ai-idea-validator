import streamlit as st
import openai

openai.api_key = st.secrets["openai_api_key"]

st.title("🧠 AI Idea Validator")

idea = st.text_input("Enter your project idea:")

if st.button("Validate"):from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"Evaluate this idea: {idea}"}
    ]
)

st.write(response.choices[0].message.content)
    st.write(response.choices[0].message.content.strip())
