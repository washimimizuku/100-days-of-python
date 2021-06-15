from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()

    return render_template("index.html", posts=all_posts)


@app.route('/post/<id>')
def get_post(id):
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    blog_response = requests.get(blog_url)
    posts = blog_response.json()

    blog_post = {}
    for post in posts:
        if post["id"] == int(id):
            blog_post = post

    return render_template("post.html", post=blog_post)


if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
