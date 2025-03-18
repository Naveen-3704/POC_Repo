import streamlit as st

st.title("Multi-Input Form with Mandatory & Optional Fields")

# Create a form
with st.form("user_form"):
    st.subheader("Enter Details:")

    # Mandatory Fields
    name = st.text_input("Name (Required)", placeholder="Enter your name")
    age = st.number_input("Age (Required)", min_value=1, max_value=100, step=1)

    # Optional Fields
    email = st.text_input("Email (Optional)", placeholder="Enter email (if available)")
    phone = st.text_input("Phone (Optional)", placeholder="Enter phone number")

    # Submit Button
    submitted = st.form_submit_button("Submit")

# Validate Mandatory Fields
if submitted:
    st.write("Hurrey")