import requests

# View our quick start guide to get your API key and version ID:
# https://www.voiceflow.com/api/dialog-manager#section/Quick-Start
api_key = "VF.61921124535215001b8219eb.JFpACUbuW4Sx1hTBPbxtxBEpUFf9pmsvSd8J4YD3l2"
version_id = "6184905f2ada060006319ce7"

user_id = "user_123"  # Unique ID used to track conversation state
user_input = "Hello world!"  # User's message to your Voiceflow project

body = {"request": {"type": "text", "payload": "Hello world!"}}

# Start a conversation
response = requests.post(
    f"https://general-runtime.voiceflow.com/state/{version_id}/user/{user_id}/interact",
    json=body,
    headers={"Authorization": api_key},
)

# Log the response
print(response.json())