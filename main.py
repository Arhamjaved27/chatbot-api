import streamlit as st
import requests

# Flask API endpoint
API_URL = "https://aibytec-bot-4da4777c8a3f.herokuapp.com/api/messages"

st.title("Chatbot Message Viewer")
st.write("Messages received via WhatsApp:")

def fetch_messages():
    """Fetch messages from Flask API."""
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error fetching messages: {response.status_code}")
            return []
    except Exception as e:
        st.error(f"Error: {e}")
        return []

# Fetch and display messages
if st.button("Refresh Messages"):
    messages = fetch_messages()
    if messages:
        for msg in messages:
            st.write(f"**From:** {msg['from']}")
            st.write(f"**Message:** {msg['body']}")
            st.write(f"**Timestamp:** {msg['timestamp']}")
            st.write("---")
