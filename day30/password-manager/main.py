import os
import json
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
DATA_FILENAME = "data.json"
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

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open(DATA_FILE, 'r') as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open(DATA_FILE, 'w') as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open(DATA_FILE, 'w') as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
            website_entry.focus()

# ---------------------------- SEARCH PASSWORD ----------------------------- #
def search_password():
    website = website_entry.get()
    try:
        with open(DATA_FILE, 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No password file", message="There is no password file yet.\nPlease create some passwords first.")
    else:
        if website in data:
            website_data = data[website]

            email = website_data["email"]
            email_entry.delete(0, tkinter.END)
            email_entry.insert(tkinter.END, string=email)

            password = website_data["password"]
            password_entry.delete(0, tkinter.END)
            password_entry.insert(tkinter.END, string=password)

            pyperclip.copy(password)

            messagebox.showinfo(title="Website found", message=f"These are the details entered:\nWebsite: {website}\nEmail: {email}\nPassword: {password}\nThis password is now on your clipboard")

        else:
            messagebox.showinfo(title="Website not found", message="I cannot find a password for that website.\nPlease check your spelling.")

# ---------------------------- UI SETUP ------------------------------------ #
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

website_entry = tkinter.Entry(width=23)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = tkinter.Button(text="Search", width=13, command=search_password)
search_button.grid(column=2, row=1)

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
