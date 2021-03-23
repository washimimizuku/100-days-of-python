import tkinter

# Create a new window with configurations
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Label
label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
label["text"] = "New Text"
label.config(text="Really New Text")
label.grid(column=0, row=0)
label.config(padx=50, pady=50)

# Entry
input = tkinter.Entry(width=10)
input.grid(column=1, row=1)

# Button
def button_clicked():
    print("I got clicked")
    text = input.get()
    label["text"] = text

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)


# Window main loop
window.mainloop()
