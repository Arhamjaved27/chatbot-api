import streamlit as st
import requests
import time

# Flask API endpoints
API_URL_MESSAGES = "https://aibytec-bot-4da4777c8a3f.herokuapp.com/api/messages"
API_URL_NEW_MESSAGES = "https://aibytec-bot-4da4777c8a3f.herokuapp.com/api/has_new_messages"

st.title("Chatbot Message Viewer")
st.write("Messages received via WhatsApp:")

# Function to fetch messages
def fetch_messages():
    try:
        response = requests.get(API_URL_MESSAGES)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error fetching messages: {response.status_code}")
            return []
    except Exception as e:
        st.error(f"Error: {e}")
        return []

# Function to check for new messages
def has_new_messages():
    try:
        response = requests.get(API_URL_NEW_MESSAGES)
        if response.status_code == 200:
            return response.json().get("new_messages", False)
        else:
            return False
    except Exception as e:
        return False

# Placeholder to display messages
messages_placeholder = st.empty()

# Polling loop
st.write("Waiting for new messages...")
while True:
    if has_new_messages():
        messages = fetch_messages()
        with messages_placeholder.container():
            st.write("New messages received:")
            for msg in messages:
                st.write(f"**From:** {msg['from']}")
                st.write(f"**Message:** {msg['body']}")
                st.write(f"**Timestamp:** {msg['timestamp']}")
                st.write("---")
    time.sleep(2)  # Poll every 5 seconds





# import streamlit as st
# import requests

# # Flask API endpoint
# API_URL = "https://aibytec-bot-4da4777c8a3f.herokuapp.com/api/messages"

# st.title("Chatbot Message Viewer")
# st.write("Messages received via WhatsApp:")

# def fetch_messages():
#     """Fetch messages from Flask API."""
#     try:
#         response = requests.get(API_URL)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             st.error(f"Error fetching messages: {response.status_code}")
#             return []
#     except Exception as e:
#         st.error(f"Error: {e}")
#         return []

# # Fetch and display messages
# if st.button("Refresh Messages"):
#     messages = fetch_messages()
#     if messages:
#         for msg in messages:
#             st.write(f"**From:** {msg['from']}")
#             st.write(f"**Message:** {msg['body']}")
#             st.write(f"**Timestamp:** {msg['timestamp']}")
#             st.write("---")
