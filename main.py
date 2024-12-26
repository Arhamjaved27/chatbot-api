import streamlit as st
import requests
import time

# Flask API endpoints
API_URL_MESSAGES = "https://aibytec-bot-4da4777c8a3f.herokuapp.com/api/messages"
API_URL_NEW_MESSAGES = "https://aibytec-bot-4da4777c8a3f.herokuapp.com/api/has_new_messages"

st.title("Chatbot Latest Message Viewer")
st.write("Displaying the most recent message received via WhatsApp:")

# Function to fetch the latest message
def fetch_latest_message():
    try:
        response = requests.get(API_URL_MESSAGES)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error fetching the latest message: {response.status_code}")
            return {}
    except Exception as e:
        st.error(f"Error: {e}")
        return {}

# Function to check if there is a new message
def has_new_message():
    try:
        response = requests.get(API_URL_NEW_MESSAGES)
        if response.status_code == 200:
            return response.json().get("new_message", False)
        else:
            return False
    except Exception as e:
        return False

# Placeholder to display the latest message
latest_message_placeholder = st.empty()

# Polling loop to check for new messages
st.write("Waiting for new messages...")
while True:
    if has_new_message():
        latest_message = fetch_latest_message()
        with latest_message_placeholder.container():
            st.write("**New message received:**")
            if latest_message:
                st.write(f"**From:** {latest_message.get('from')}")
                st.write(f"**Message:** {latest_message.get('body')}")
                st.write(f"**Timestamp:** {latest_message.get('timestamp')}")
    time.sleep(5)  # Poll every 5 seconds







# import streamlit as st
# import requests
# import time

# # Flask API endpoints
# API_URL_MESSAGES = "https://aibytec-bot-4da4777c8a3f.herokuapp.com/api/messages"
# API_URL_NEW_MESSAGES = "https://aibytec-bot-4da4777c8a3f.herokuapp.com/api/has_new_messages"

# st.title("Chatbot Message Viewer")
# st.write("Messages received via WhatsApp:")

# last_message_placeholder = st.empty()

# # Function to fetch the last message
# def fetch_last_message():
#     try:
#         response = requests.get(API_URL_MESSAGES)
#         if response.status_code == 200:
#             return response.json()
#         elif response.status_code == 404:
#             return {"from": "System", "body": "No messages available", "timestamp": ""}
#         else:
#             # st.error(f"Error fetching last message: {response.status_code}")
#             return None
#     except Exception as e:
#         st.error(f"Error: {e}")
#         return None

# # Function to check for new messages
# def has_new_messages():
#     try:
#         response = requests.get(API_URL_NEW_MESSAGES)
#         if response.status_code == 200:
#             return response.json().get("new_messages", False)
#         else:
#             return False
#     except Exception as e:
#         return False

# # Placeholder to display messages
# messages_placeholder = st.empty()

# # Polling loop
# st.write("Waiting for the latest message...")
# last_displayed_message = None
# while True:
#     last_message = fetch_last_message()
#     if last_message and last_message != last_displayed_message:
#         last_displayed_message = last_message
#         with last_message_placeholder.container():
#             st.write(f"**From:** {last_message['from']}")
#             st.write(f"**Message:** {last_message['body']}")
#             st.write(f"**Timestamp:** {last_message['timestamp']}")
#             st.write("---")
#     time.sleep(5)  # Poll every 5 seconds





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
