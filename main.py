from flask import Flask, render_template, request, redirect
import datetime
from twilio.twiml.messaging_response import MessagingResponse



app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template('index.html', year=current_year)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming call with text message"""
    # Start TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("Thanks for your interest, Really")
    return str(resp)


@app.route("/hobbies.html")
def hobbies():
    return render_template("hobbies.html")


@app.route("/fishing_conditions.html")
def fishing_conditions():
    return render_template("fishing_conditions.html")


if __name__ == '__main__':

    app.run(debug=True)


