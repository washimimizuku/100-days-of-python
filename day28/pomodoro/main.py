import math
import os
import tkinter


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = "#000000"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
FILENAME = "tomato.png"
FULL_PATH = os.path.join(LOCATION, FILENAME)

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    reps += 1
    if reps % 8 == 0:
        count_down(long_break_seconds)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        title.config(text="Break", fg=PINK)
    else:
        count_down(work_seconds)
        title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"

        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk() 
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
title.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file=FULL_PATH)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text="Start", command=start_timer, fg=BLACK, highlightbackground=YELLOW, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", command=reset_timer, fg=BLACK, highlightbackground=YELLOW, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = tkinter.Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


# --------------------------- WINDOW LOOP ----------------------------- #
window.mainloop()
