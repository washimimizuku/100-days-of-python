import tkinter

PADDING_WINDOW = 20
PADDING_LABELS = 10
FONT = ("Arial", 20)

# Create a new window with configurations
window = tkinter.Tk()
window.title("Miles to Kms Converter")
window.minsize(width=300, height=200)
window.config(padx=PADDING_WINDOW, pady=PADDING_WINDOW)

# Label
miles_label = tkinter.Label(text="Miles")
kms_label = tkinter.Label(text="Kms")
equal_to_label = tkinter.Label(text="is equal to")

result_label = tkinter.Label(text="")

miles_label.grid(column=2, row=0)
miles_label.config(padx=PADDING_LABELS, pady=PADDING_LABELS, font=FONT)
kms_label.grid(column=2, row=1)
kms_label.config(padx=PADDING_LABELS, pady=PADDING_LABELS, font=FONT)
equal_to_label.grid(column=0, row=1)
equal_to_label.config(padx=PADDING_LABELS, pady=PADDING_LABELS, font=FONT)
result_label.grid(column=1, row=1)
result_label.config(padx=PADDING_LABELS, pady=PADDING_LABELS, font=FONT)

# Entry
miles_entry = tkinter.Entry(width=9)
miles_entry.grid(column=1, row=0)

# Button
def calculate():
    miles = float(miles_entry.get())
    kms = format(miles * 1.60934, '.2f')
    result_label.config(text=f"{kms}")

button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


# Window main loop
window.mainloop()
