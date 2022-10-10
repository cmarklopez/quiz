import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
IMG_BUTTON_TRUE = r"quiz/images/true.png"
IMG_BUTTON_FALSE = r"quiz/images/false.png"
FONT_QUESTION = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz: QuizBrain) -> None:
        self.quiz = quiz
        self.window = tk.Tk()
        self.window.title("Quiz Game")
        self.window.config(bg=THEME_COLOR)
        self.score_label = tk.Label(
            text=f"Score: {quiz.score}", background=THEME_COLOR, highlightthickness=0
        )
        self.score_label.grid(row=0, column=1, pady=20)
        self.question_canvas = tk.Canvas(
            self.window, width=300, height=250, bg="white", highlightthickness=0
        )
        self.question_canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.canvas_text = self.question_canvas.create_text(
            150, 125, anchor=tk.CENTER, fill="black", justify=tk.CENTER
        )
        self.question_canvas.itemconfig(
            self.canvas_text,
            font=FONT_QUESTION,
            fill=THEME_COLOR,
            width=280,
        )
        self.image_true = tk.PhotoImage(file=IMG_BUTTON_TRUE)
        self.image_false = tk.PhotoImage(file=IMG_BUTTON_FALSE)
        self.btn_true = tk.Button(
            self.window,
            image=self.image_true,
            highlightthickness=0,
            command=self.next_question,
        )
        self.btn_false = tk.Button(
            self.window,
            image=self.image_false,
            highlightthickness=0,
            command=self.next_question,
        )
        self.btn_true.grid(row=2, column=0, padx=20, pady=20)
        self.btn_false.grid(row=2, column=1, padx=20, pady=20)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.quiz.next_question()
        msg_txt = (
            f"Q{self.quiz.question_number + 1}: "
            f"{self.quiz.question_list[self.quiz.question_number].text}"
        )
        self.question_canvas.itemconfig(
            self.canvas_text,
            text=msg_txt,
        )
