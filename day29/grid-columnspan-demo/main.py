import tkinter

window = tkinter.Tk()

r = tkinter.Label(bg="red", width=20, height=5)
r.grid(row=0, column=0)

r = tkinter.Label(bg="green", width=20, height=5)
r.grid(row=1, column=1)

r = tkinter.Label(bg="blue", width=40, height=5)
r.grid(row=2, column=0, columnspan=2)

window.mainloop()
