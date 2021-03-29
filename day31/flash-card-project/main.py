import os
import pandas
import random
import tkinter


LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
LANGUAGE_FILE = os.path.join(LOCATION, "data/german_words.csv")
WORDS_TO_LEARN_FILE = os.path.join(LOCATION, "data/words_to_learn.csv")
CARD_BACK_IMAGE = os.path.join(LOCATION, "images/card_back.png")
CARD_FRONT_IMAGE = os.path.join(LOCATION, "images/card_front.png")
RIGHT_IMAGE = os.path.join(LOCATION, "images/right.png")
WRONG_IMAGE = os.path.join(LOCATION, "images/wrong.png")

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")

try:
    data = pandas.read_csv(WORDS_TO_LEARN_FILE)
except FileNotFoundError:
    data = pandas.read_csv(LANGUAGE_FILE)

words_to_learn = data.to_dict(orient="records")
word_to_learn = None
flip_timer = None

def wrong_answer():
    get_random_word()

def right_answer():
    words_to_learn.remove(word_to_learn)
    data = pandas.DataFrame(words_to_learn)
    data.to_csv(WORDS_TO_LEARN_FILE, index=False)

    get_random_word()

def get_random_word():
    global word_to_learn, flip_timer

    if flip_timer:
        window.after_cancel(flip_timer)

    word_to_learn = random.choice(words_to_learn[:50])
    word = word_to_learn['German']

    canvas.itemconfig(card_image, image=cart_front_image)
    
    canvas.itemconfig(title_text, text="Deutsch", fill="black")
    canvas.itemconfig(word_text, text=f"{word}", fill="black")

    flip_timer = window.after(3000, flip_card)

def flip_card():
    word = word_to_learn['English']
    
    canvas.itemconfig(card_image, image=cart_back_image)

    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{word}", fill="white")


window = tkinter.Tk() 
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
cart_front_image = tkinter.PhotoImage(file=CARD_FRONT_IMAGE)
cart_back_image = tkinter.PhotoImage(file=CARD_BACK_IMAGE)
card_image = canvas.create_image(400, 263, image=cart_front_image)
title_text = canvas.create_text(400, 150, text="", fill="black", font=FONT_TITLE)
word_text = canvas.create_text(400, 263, text="", fill="black", font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)

wrong_button_image = tkinter.PhotoImage(file=WRONG_IMAGE)
wrong_button = tkinter.Button(image=wrong_button_image, command=wrong_answer, highlightbackground=BACKGROUND_COLOR, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_button_image = tkinter.PhotoImage(file=RIGHT_IMAGE)
right_button = tkinter.Button(image=right_button_image, command=right_answer, highlightbackground=BACKGROUND_COLOR, highlightthickness=0)
right_button.grid(column=1, row=1)

get_random_word()


window.mainloop()