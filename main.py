from flask import Flask, render_template, request, redirect
import datetime
from twilio.twiml.messaging_response import MessagingResponse



app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template('index.html', year=current_year)


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'hello':
        resp.message("Hi!")
    elif body == 'bye':
        resp.message("Goodbye")

    return str(resp)


@app.route("/hobbies.html")
def hobbies():
    return render_template("hobbies.html")


@app.route("/fishing_conditions.html")
def fishing_conditions():
    return render_template("fishing_conditions.html")


if __name__ == '__main__':

    app.run(debug=True)


