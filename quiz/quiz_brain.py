from question_model import Question


class QuizBrain:
    def __init__(self, question_list: list[Question], question_number: int = 0) -> None:
        self.question_number = question_number
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        while True:
            answer = input(f"Q.{self.question_number}: {question.text}. (True/False)? ")
            if answer.lower() in ["true", "false"]:
                break
            else:
                continue
        self.question_number += 1
        self.check_answer(answer, question.answer)

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, answer: str, correct_answer: str):
        if answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.\n")
