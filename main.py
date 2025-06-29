import streamlit as st
import requests
from dotenv import load_dotenv

# 🟢 Load .env file
load_dotenv()

# 🟠 Get Webhook from env
SLACK_WEBHOOK_URL = st.secrets["general"]["SLACK_WEBHOOK_URL"]

st.title("Streamlit Form Receiver")

query_params = st.query_params  # ✅ new method
if query_params.get("name"):
    name = query_params.get("name")
    email = query_params.get("email")
    phone = query_params.get("phone", [""])
    location = query_params.get("location", [""])
    interest = query_params.get("interest", [""])
    budget = query_params.get("budget", [""])
    message = query_params.get("message", [""])
    contact_time = query_params.get("contact_time", [""])

    slack_data = {
        "text": f"*New Form Submission:*\n\n*Name:* {name}\n*Email:* {email}\n*Phone:* {phone}\n*Location:* {location}\n*Interest:* {interest}\n*Budget:* {budget}\n*Message:* {message}\n*Preferred Time:* {contact_time}"
    }

    response = requests.post(SLACK_WEBHOOK_URL, json=slack_data)
    
    if response.status_code == 200:
        st.success("✅ Slack notified successfully!")
    else:
        st.error(f"⚠️ Slack Error: {response.status_code}")
