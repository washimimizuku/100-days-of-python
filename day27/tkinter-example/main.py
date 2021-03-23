import tkinter

# Create a new window with configurations
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="Really New Text")

# Button
def button_clicked():
    print("I got clicked")
    text = input.get()
    my_label["text"] = text

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = tkinter.Entry(width=10)
input.pack()

# Text



# Spinbox



# Scale



# Checkbox



# Radiobutton



# Listbox



# "While" loop
window.mainloop()
