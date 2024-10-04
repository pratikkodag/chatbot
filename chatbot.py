import streamlit as st
import os
import google.generativeai as genai
# Function to set up a simple chatbot
def simple_chatbot(message):
    api_key = "AIzaSyA34MZ0M6Pb6LVJnXN8adv1DBIOCu_HFcE"  # Hardcoded API key
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        },
    )

    chat_session = model.start_chat(history=[])

    response = chat_session.send_message(message)
    return response.text

# Streamlit app
def main():
    st.title(" AI Chatbot")

    # Input for the message only
    message = st.text_area("Enter your message:")

    if st.button("Send"):
        if not message:
            st.error("Message cannot be empty!")
        else:
            with st.spinner("Generating response..."):
                try:
                    chatbot_response = simple_chatbot(message)
                    st.success("Response:")
                    st.write(chatbot_response)
                except Exception as e:
                    st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
