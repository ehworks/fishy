from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import datetime


import smtplib
import requests


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = "BST1686tx"


G_EMAIL = "day.32.practice@gmail.com"
G_PASSWORD = "zavnWKkvFVmE9d8"
Y_EMAIL = "day_32_practice@yahoo.com"
Y_PASSWORD = "gg36H2Pgz38gjQJ"


@app.route('/')
def home():
    current_year = datatime.datetime.now().year
    return render_template('index.html', year=current_year)


@app.route("/hobbies.html")
def hobbies():
    return render_template("hobbies.html")

@app.route"/data.txt")
def data_txt():
    return render_template("data.txt")

@app.route("/weather_codes.html")
def weather_codes():
    with open('C:/Users/m_els/PycharmProjects/pythonProject1/Fishy/templates/data.txt') as data_file:
        # data_file = open('C:/Users/m_els/PycharmProjects/pythonProject1/Fishy/templates/data.txt')
        # data_file.close()
        for line in data_file:
            print(line)
        return render_template("weather_codes.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


# @app.route("/login.html")
# def login():
#     login_form = LoginForm()
#     return render_template('login.html', form=login_form)


#
# @app.route('/login', methods=["POST"])
# def receive_data():
#     name = request.form["username"]
#     password = request.form["password"]
#     typefish = request.form["typeFish"]
#
#     conditions = request.form["yourDescribe"]
#
#     return f"<h1> Name: {name} </h1> <br> <h1>Type of Fish: {typefish} </h1> " \
#            f"<br> <h1>Conditions are: {conditions} </h1>"


# def send_email():
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         # with smtplib.SMTP("smtp.gmail.com") as connection:
#         # simple mail transfer protocol
#         connection.starttls()
#         connection.login(G_EMAIL, G_PASSWORD)
#         connection.sendmail(
#                 from_addr=Y_EMAIL,
#                 to_addrs="day.32.practice@gmail.com",
#                 msg="Subject:Want to see Space Station \n\n this is the body ")
#

if __name__ == '__main__':

    app.run(debug=True)

# send_email()
