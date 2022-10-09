import tkinter as tk

THEME_COLOR = "375362"


class QuizInterface:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("Quiz Game")

        self.window.mainloop()
