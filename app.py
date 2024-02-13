import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

account_sid = os.environ['AC2e35e932c8d2cce0674ff1ff75eb79ce']
auth_token = os.environ['9e9cf21f77653bb40fde54a1a61f4b18']
client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/ ", methods=["get", "post"])
def reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    resp.message("You said: {}".format(msg))
 
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
