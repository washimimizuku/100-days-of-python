import os
import pyperclip
import random
import tkinter
from tkinter import messagebox
from dotenv import load_dotenv

load_dotenv()

# ---------------------------- CONSTANTS ------------------------------- #
LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
LOGO_FILENAME = "logo.png"
LOGO_FILE = os.path.join(LOCATION, LOGO_FILENAME)
DATA_FILENAME = "data.txt"
DATA_FILE = os.path.join(LOCATION, DATA_FILENAME)
MY_EMAIL = os.environ.get('MY_EMAIL')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password = []
    password.extend([random.choice(letters) for _ in range(nr_letters)])
    password.extend([random.choice(symbols) for _ in range(nr_symbols)])
    password.extend([random.choice(numbers) for _ in range(nr_numbers)])
    random.shuffle(password)
    password = "".join(password)

    password_entry.delete(0, tkinter.END)
    password_entry.insert(tkinter.END, string=password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nWebsite: {website}\nEmail: {email}\nPassword: {password}\nIs it ok to save?")

        if is_ok: 
            with open(DATA_FILE, 'a') as f:
                f.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk() 
window.title("Password Manager")
window.config(padx=50, pady=50)

# Row 0
canvas = tkinter.Canvas(width=200, height=200)
lock_image = tkinter.PhotoImage(file=LOGO_FILE)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Row 1
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = tkinter.Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Row 2
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = tkinter.Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, MY_EMAIL)

# Row 3
password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = tkinter.Entry(width=23)
password_entry.grid(column=1, row=3)

generate_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

# Row 4
generate_button = tkinter.Button(text="Add", width=38, command=save_password)
generate_button.grid(column=1, row=4, columnspan=2)


# --------------------------- WINDOW LOOP ----------------------------- #
window.mainloop()
