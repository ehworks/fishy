from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import datetime


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = "BST1686tx"


@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template('index.html', year=current_year)


@app.route("/hobbies.html")
def hobbies():
    return render_template("hobbies.html")


@app.route("/data.txt")
def data():
    return render_template("data.txt")


@app.route("/fishing_conditions.html")
def fishing_conditions():
    return render_template("fishing_conditions.html")


if __name__ == '__main__':

    app.run(debug=True)

