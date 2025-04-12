
import streamlit as st
import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Too short (min 8 chars)": length_error,
        "Missing a digit": digit_error,
        "Missing an uppercase letter": uppercase_error,
        "Missing a lowercase letter": lowercase_error,
        "Missing a special character": symbol_error
    }

    if not any(errors.values()):
        strength = "Strong 💪"
        color = "green"
    elif sum(errors.values()) <= 2:
        strength = "Moderate 😐"
        color = "orange"
    else:
        strength = "Weak 😞"
        color = "red"

    return strength, color, errors


# Streamlit UI
st.title("🔐 Password Strength Checker")
st.markdown(""" ## welcome to the ultimate password strength checker!🤚
use this simple tool to check your password and get suggestions on how to make it stronger. 
           we will give you helpful tips to create a **Strong Password** 🔒""")
password = st.text_input("Enter your password", type="password")

if password:
    strength, color, errors = check_password_strength(password)
    st.markdown(f"**Strength:** :{color}[{strength}]")

    st.subheader("Issues:")
    for msg, err in errors.items():
        if err:
            st.markdown(f"- ❌ {msg}")
        else:
            st.markdown(f"- ✅ {msg}")
