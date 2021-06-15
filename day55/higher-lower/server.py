from flask import Flask
import random


app = Flask(__name__)

random_number = random.randint(0, 10)


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:number>')
def guess(number):
    text = ''
    if number < random_number:
        text = '<h1>Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif number > random_number:
        text = '<h1>Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        text = '<h1>You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    return text


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
