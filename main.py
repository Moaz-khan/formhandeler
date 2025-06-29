import streamlit as st
import requests

# ✅ Get Webhook from Streamlit Secrets
SLACK_WEBHOOK_URL = st.secrets["general"]["SLACK_WEBHOOK_URL"]

# ✅ Set Page Config
st.set_page_config(page_title="Thank You", page_icon="✅")
st.title("")

# ✅ Read query parameters
query_params = st.query_params

if query_params.get("name"):
    # Get all form fields from query params
    name = query_params.get("name", [""])
    email = query_params.get("email", [""])
    phone = query_params.get("phone", [""])
    location = query_params.get("location", [""])
    interest = query_params.get("interest", [""])
    budget = query_params.get("budget", [""])
    message = query_params.get("message", [""])
    contact_time = query_params.get("contact_time", [""])

    # Format the Slack message
    slack_data = {
        "text": f"*New Form Submission:*\n\n*Name:* {name}\n*Email:* {email}\n*Phone:* {phone}\n*Location:* {location}\n*Interest:* {interest}\n*Budget:* {budget}\n*Message:* {message}\n*Preferred Time:* {contact_time}"
    }

    # 🚀 Send to Slack
    response = requests.post(SLACK_WEBHOOK_URL, json=slack_data)

    # ✅ Show thank you confirmation
    st.markdown("## 🎉 Thanks for contacting us!")
    st.markdown("We’ll get back to you as soon as possible.")

    # 🔙 Back to main site button
    st.markdown(
        "<a href='https://muhammad-maaz-six.vercel.app/' target='_self'>"
        "<button style='padding:10px 20px; background-color:#f97316; color:white; border:none; border-radius:5px;'>Go Back to Home</button>"
        "</a>",
        unsafe_allow_html=True
    )

else:
    st.warning("No form data found in URL. Please try again.")
