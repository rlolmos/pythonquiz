from tkinter import *
import html
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
GREEN = "#00FF00"
RED = "#FF0000"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.user_answer = None
        self.color = "white"
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canva = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canva.create_text(
            150,
            125,
            width=280,
            text="HOLI",
            font=("Arial", 15, "italic"),
            fill=THEME_COLOR)
        self.canva.grid(pady=50, column=0, row=1, columnspan=2)
        self.get_next_question()
        true_btn = PhotoImage(file='./images/true.png')
        false_btn = PhotoImage(file='./images/false.png')
        self.buttonTrue = Button(image=true_btn, highlightthickness=0, command=self.true_button_action)
        self.buttonTrue.grid(column=0, row=2)
        self.buttonFalse = Button(image=false_btn, highlightthickness=0, command=self.false_button_action)
        self.buttonFalse.grid(column=1, row=2)
        self.window.mainloop()

    def get_next_question(self):
        self.canva.config(bg="white")
        q_text = self.quiz.next_question()
        self.canva.itemconfig(self.question_text, text=q_text)

    def true_button_action(self):
        self.user_answer = "True"
        self.check_the_answer()

    def false_button_action(self):
        self.user_answer = "False"
        self.check_the_answer()

    def check_the_answer(self):
        is_right = self.quiz.check_answer(self.user_answer)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.color = GREEN
        else:
            self.color = RED
        self.canva.config(bg=self.color)
        self.window.after(700, self.get_next_question)