import streamlit as st
import requests

# Set the page configuration for better layout
st.set_page_config(page_title="Email Analysis", layout="wide")

# Function to send POST request to your API
def send_email_for_analysis(email_body):
    response = requests.post(
        'https://ruchai-ansjhewkia-el.a.run.app/predict',  # Replace with your API endpoint
        json={"email_body": email_body}
    )
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error from API: " + response.text)
        return None

# Streamlit UI
st.title("RuchAI - Your Email Mom")

# Email body text area
email_body = st.text_area("Enter the body of the email:", height=300)

# Button to submit email
if st.button('Get Priority'):
    if email_body:
        result = send_email_for_analysis(email_body)
        if result:
            # Display summary
            st.subheader("Summary:")
            st.write(result.get("summary"))

            # Display label with color based on predicted class
            predicted_class = result.get("predicted_class")
            if predicted_class == 0:
                st.markdown("<h2 style='color: red;'>Urgent</h2>", unsafe_allow_html=True)
            elif predicted_class == 1:
                st.markdown("<h2 style='color: yellow;'>Moderate</h2>", unsafe_allow_html=True)
            elif predicted_class == 2:
                st.markdown("<h2 style='color: green;'>Low</h2>", unsafe_allow_html=True)
    else:
        st.warning("Please enter the email body to analyze.")

# Add spacing at the bottom
st.write("")
st.write("")
