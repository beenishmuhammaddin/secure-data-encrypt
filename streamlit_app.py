# streamlit_app.py
import streamlit as st
from cryptography.fernet import Fernet

st.title("🔐 Secure Data Encryption App")

# Generate and store key
if "key" not in st.session_state:
    st.session_state["key"] = Fernet.generate_key()

key = st.session_state["key"]
cipher = Fernet(key)

# Input
message = st.text_input("Enter a message to encrypt:")

if st.button("Encrypt"):
    if message:
        encrypted = cipher.encrypt(message.encode())
        st.success("Encrypted Message:")
        st.code(encrypted)
    else:
        st.warning("Please enter a message.")

if st.button("Decrypt"):
    try:
        decrypted = cipher.decrypt(encrypted).decode()
        st.success("Decrypted Message:")
        st.code(decrypted)
    except:
        st.error("Decryption failed.")
