import streamlit as st
import openai

# OpenAI API key - left blank for demonstration
openai.api_key = ""



bot_name = "ChatBot"
max_messages = 50

if "history" not in st.session_state:
    st.session_state.history = []  

user_input = st.text_input("Type your question here:", key="input_box")

def generate_prompt(user_input, history):
    context = " ".join(history)
    return [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": context} 
    ]

if st.button("Send Message"):
    if user_input and len(user_input) > 3:
        try:
 
            context_history = st.session_state.history
            messages = generate_prompt(user_input, context_history)
            
     
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            
            answer = response.get("choices")[0]["message"]["content"]  # Will throw error
            
        except Exception as e:
            answer = f"Oops! Something went wrong: {e}"

      
        st.session_state.history.append(user_input)  
    else:
        answer = "Please enter more than 3 characters."

# Display the chat
for entry in st.session_state.history[::-1]:
    # Assuming entry is a tuple, but it's just a string
    st.write(f"**User:** {entry[0]}")  # This will fail if entry is a string
    st.write(f"**Bot:** {entry[1] if len(entry) > 1 else 'No reply stored.'}")
