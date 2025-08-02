"""
main.py
-------
Streamlit app to interactively check if a message is spam.
"""

import streamlit as st
from prediction import predict_spam

st.set_page_config(page_title="📩 Spam Detector App", page_icon="✉️", layout="centered")

st.title("📩 Spam Detector App")
st.write("""
This app uses a trained neural network to detect spam messages.
Enter your message below to check:
""")

# User input
user_input = st.text_area("✏️ Write your message here:")

if st.button("Check Spam"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message.")
    else:
        result = predict_spam(user_input)
        st.success(f"✅ Prediction: **{result}**")
