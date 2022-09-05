from question_model import Question
import html
import requests


class QuizBank:
    url_questions = "https://opentdb.com/api.php"
    question_type = "boolean"

    def __init__(self, category: int, number: int) -> None:
        self.question_category = category
        self.number_of_questions = number
        self.questions = self._get_questions()
        self.question_type = "boolean"

    def _get_questions(self) -> list[Question]:
        params = {}
        params["amount"] = self.number_of_questions
        params["category"] = self.question_category
        params["type"] = self.question_type
        response = requests.get(self.url_questions, params)
        results_to_json = response.json()
        raw_questions = results_to_json["results"]
        question_bank = self._process_questions(raw_questions)
        return question_bank

    def _process_questions(
        self, questions_to_parse: list[dict[str, str]]
    ) -> list[Question]:
        question_bank: list[Question] = []
        for question_dict in questions_to_parse:
            question_text = html.unescape(question_dict["question"])
            question_answer = question_dict["correct_answer"]
            question = Question(question_text, question_answer)
            question_bank.append(question)
        return question_bank
