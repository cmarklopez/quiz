from question_model import Question


class QuizBrain:
    """This class contains the logic for presenting questions to the player, keeping
    up with the game state, and checking answers
    """

    def __init__(
        self, question_list: list[Question], question_number: int = -1
    ) -> None:
        self.question_number = question_number
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        """Present the player with the next qustion."""
        # question = self.question_list[self.question_number]
        # prompt = f"Q.{self.question_number}: {question.text}. (True/False)? "
        # while (answer := input(prompt)).lower() not in ["true", "false"]:
        #    pass
        self.question_number += 1
        # self.check_answer(answer, question.answer)

    def still_has_questions(self) -> bool:
        """Check to see if there are any more questions for the game."""
        return self.question_number < len(self.question_list)

    def check_answer(self, answer: str, correct_answer: str):
        """Check to see if the player's response is correct.

        :param answer: str, the answer provided by the player
        :param correct_answer: str, the correct answer from the Open Trivia DB
        """
        if answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.\n")
