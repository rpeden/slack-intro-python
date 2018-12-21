import requests
import json

url = "https://slack.com/api/chat.postMessage"
token = "your-token-goes-here"

headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer {0}".format(token)
}

def send_message(message_text):
  message = {
    "channel": "#general",
    "text": message_text
  }

  requests.post(url, headers=headers, data=json.dumps(message))

send_message("Hello from Python!")