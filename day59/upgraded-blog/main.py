from flask import Flask, render_template
import requests

BLOG_API_URL = "https://api.npoint.io/0067e63917ca7a5034d9"

app = Flask(__name__)


@app.route('/')
def get_home():
    blog_response = requests.get(BLOG_API_URL)
    all_posts = blog_response.json()

    return render_template("index.html", posts=all_posts)


@app.route('/about')
def get_about():
    return render_template("about.html")


@app.route('/contact')
def get_contact():
    return render_template("contact.html")


@app.route('/post/<int:id>')
def get_post(id):
    blog_response = requests.get(BLOG_API_URL)
    posts = blog_response.json()

    blog_post = {}
    for post in posts:
        if post["id"] == int(id):
            blog_post = post
    
    return render_template("post.html", post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
