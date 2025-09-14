import streamlit as st
import openai


openai.api_key = ""

st.title("Simple Chat App")

st.write("This is a very basic chat app. Some features are missing (TODO).")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Ask something:")

if st.button("Send"):
    if user_input.strip():
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a simple assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            answer = response["choices"][0]["message"]["content"]
        except Exception as e:
            answer = f"Error: {e}"

        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Bot", answer))

for role, msg in st.session_state.history[::-1]:
    st.write(f"**{role}:** {msg}")
