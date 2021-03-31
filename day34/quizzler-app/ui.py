import os
import tkinter
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
FONT_SCORE = ("Arial", 20, "bold")

LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
TRUE_IMAGE = os.path.join(LOCATION, "images/true.png")
FALSE_IMAGE = os.path.join(LOCATION, "images/false.png")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.score = tkinter.Label(text="Score: 0/0", fg="white", bg=THEME_COLOR, font=FONT_SCORE)
        self.score.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR, font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = tkinter.PhotoImage(file=TRUE_IMAGE)
        self.true_button = tkinter.Button(image=true_image, command=self.true_pressed, highlightbackground=THEME_COLOR, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        false_image = tkinter.PhotoImage(file=FALSE_IMAGE)
        self.false_button = tkinter.Button(image=false_image, command=self.false_pressed, highlightbackground=THEME_COLOR, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self): 
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.itemconfig(self.question_text, fill="white")
        self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.window.after(500, self.get_next_question)
