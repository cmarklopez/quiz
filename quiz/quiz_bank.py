from question_model import Question
import html
import requests


class QuizBank:
    """This class gets and stored the questions for a quiz from the Open Trivia DB"""

    url_questions = "https://opentdb.com/api.php"

    def __init__(self, category: int, number: int) -> None:
        self.question_category = category
        self.number_of_questions = number
        self.questions = self._get_questions()
        self.question_type = "boolean"

    def _get_questions(self) -> list[Question]:
        """Get the questions from the Open Trivia DB and store them in questions
        attribute
        """
        params = {
            "amount": self.number_of_questions,
            "category": self.question_category,
            "type": self.question_type,
        }
        response = requests.get(self.url_questions, params)
        results_to_json = response.json()
        result_code = results_to_json["response_code"]
        if result_code == 0:
            raw_questions = results_to_json["results"]
            question_bank = self._process_questions(raw_questions)
            return question_bank
        else:
            return []

    def _process_questions(
        self, questions_to_parse: list[dict[str, str]]
    ) -> list[Question]:
        """Format the questions returned from the API. Strip the extra dictionary
        and fix the encoding.
        """
        question_bank: list[Question] = []
        for question_dict in questions_to_parse:
            question_text = html.unescape(question_dict["question"])
            question_answer = question_dict["correct_answer"]
            question = Question(question_text, question_answer)
            question_bank.append(question)
        return question_bank
