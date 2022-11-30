from tkinter import *
import html
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.user_answer = None
        self.user_answer: bool
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score:", bg=THEME_COLOR, fg="white")
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
        q_text = self.quiz.next_question()
        self.canva.itemconfig(self.question_text, text=q_text)

    def true_button_action(self):
        self.user_answer = True
        self.check_the_answer()

    def false_button_action(self):
        self.user_answer = False
        self.check_the_answer()

    def check_the_answer(self):
        self.quiz.check_answer(self.user_answer)
