from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import email_validator


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[
                             DataRequired(), Length(8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html.jinja')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if (login_form.validate_on_submit()):
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html.jinja")
        else:
            return render_template("denied.html.jinja")
    return render_template('login.html.jinja', form=login_form)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
