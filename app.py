import streamlit as st
import openai

st.title("Idea Validator is Loading...")

# Step 1: API Key
try:
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    st.success("API key loaded successfully")
except Exception as e:
    st.error(f"API key issue: {e}")

# Step 2: UI Ready
st.write("Checkpoint: Reached UI setup")

# Step 3: Main logic
try:
    # Whatever main logic you use — for example:
    idea = st.text_input("Enter your startup idea")
    if idea:
        st.write("Checkpoint: Received user input")

        # Add a dummy response to make sure this part is working
        st.write("Pretend analysis is running...")

        # If you use OpenAI here, also wrap in try/except
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"Evaluate this idea: {idea}"}]
            )
            st.write("Response from OpenAI:")
            st.write(response.choices[0].message["content"])
        except Exception as e:
            st.error(f"OpenAI API call failed: {e}")
except Exception as e:
    st.error(f"Main app logic failed: {e}")
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
