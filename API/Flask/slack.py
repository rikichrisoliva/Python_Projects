from flask import Flask, jsonify, request
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

app = Flask(__name__)

# Replace with your Slack API token
SLACK_TOKEN = "xoxb-4595279809761-4665758849255-Ra1QqOUIJyuy915DJNGL0aZV"
# Replace with the channel ID where you want to send the message
SLACK_CHANNEL = "#testing"
client = WebClient(token=SLACK_TOKEN)


@app.route("/send_message", methods=["POST"])
def send_message():
    try:
        # Get the message from the client
        message = request.get_json()["message"]
        # alternative
        # data = request.get_json()
        # message = data.get("message")

        # Send the message to the designated channel
        response = client.chat_postMessage(channel=SLACK_CHANNEL, text=message)

        return jsonify(response)
    except SlackApiError as e:
        return jsonify(error=str(e)), 500


if __name__ == "__main__":
    app.run()
