from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center;">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/yFQ0ywscgobJK/giphy.gif">'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return 'Bye!'


@app.route('/<name>')
def greet(name):
    return f'Hello there {name}!'


@app.route('/file/<path:file>')
def file_path(file):
    return f'This is yout path {file}!'


@app.route('/username/<name>/<int:number>')
def name_and_age(name, number):
    return f'Hello there {name}, you are {number} years old!'


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
