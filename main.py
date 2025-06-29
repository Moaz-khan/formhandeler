import streamlit as st
import requests

# Slack webhook URL from environment variable
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"
# Title for dev check
st.title("Streamlit Form Receiver")

# ✅ Updated line: Get query parameters
query_params = st.query_params

if query_params.get("name"):
    # Parse values
    name = query_params.get("name")[0]
    email = query_params.get("email")[0]
    phone = query_params.get("phone", [""])[0]
    location = query_params.get("location", [""])[0]
    interest = query_params.get("interest", [""])[0]
    budget = query_params.get("budget", [""])[0]
    message = query_params.get("message", [""])[0]
    contact_time = query_params.get("contact_time", [""])[0]

    # Format Slack message
    slack_data = {
        "text": f"*New Contact Form Submission:*\n\n*Name:* {name}\n*Email:* {email}\n*Phone:* {phone}\n*Location:* {location}\n*Interest:* {interest}\n*Budget:* {budget}\n*Message:* {message}\n*Preferred Time:* {contact_time}"
    }

    # Send to Slack
    response = requests.post(SLACK_WEBHOOK_URL, json=slack_data)
    
    if response.status_code == 200:
        st.success("✅ Slack notified successfully!")
    else:
        st.error(f"⚠️ Slack Error: {response.status_code}")
