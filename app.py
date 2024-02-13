from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

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
