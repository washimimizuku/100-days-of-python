from flask import Flask, render_template, request
import os
import requests
import smtplib
from dotenv import load_dotenv


BLOG_API_URL = "https://api.npoint.io/0067e63917ca7a5034d9"

EMAIL_SERVER = os.environ.get('EMAIL_SERVER')
EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

MY_EMAIL = os.environ.get('MY_EMAIL')


app = Flask(__name__)


@app.route('/')
def get_home():
    blog_response = requests.get(BLOG_API_URL)
    all_posts = blog_response.json()

    return render_template("index.html.jinja", posts=all_posts)


@app.route('/about')
def get_about():
    return render_template("about.html.jinja")


@app.route('/contact', methods=['GET', 'POST'])
def get_contact():
    if request.method == 'POST':
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html.jinja", msg_sent=True)
    return render_template("contact.html.jinja", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP(EMAIL_SERVER) as connection:
        connection.starttls()
        connection.login(EMAIL_USER, EMAIL_PASSWORD)
        connection.sendmail(EMAIL_USER, MY_EMAIL, email_message)


@app.route('/post/<int:id>')
def get_post(id):
    blog_response = requests.get(BLOG_API_URL)
    posts = blog_response.json()

    blog_post = {}
    for post in posts:
        if post["id"] == int(id):
            blog_post = post

    return render_template("post.html.jinja", post=blog_post)


if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
