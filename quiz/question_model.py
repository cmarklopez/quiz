class Question:
    """This class defines the basic structure for quiz questions."""

    def __init__(self, text: str, answer: str) -> None:
        self.text = text
        self.answer = answer
