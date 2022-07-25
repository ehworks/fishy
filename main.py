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
    with open('C:/Users/m_els/PycharmProjects/pythonProject1/Fishy/data.txt') as data_file:
        # data_file = open('C:/Users/m_els/PycharmProjects/pythonProject1/Fishy/templates/data.txt')
        # data_file.close()
        for line in data_file:
            print(line)
        return render_template("weather_codes.html")





if __name__ == '__main__':

    app.run(debug=True)

# send_email()
