from question_model import Question
import html
import requests
import json


class QuizBank:
    url_questions = "https://opentdb.com/api.php"
    question_type = "boolean"

    def __init__(self, category: int, number: int) -> None:
        self.question_category = category
        self.number_of_questions = number
        self.questions = self._get_questions()
        self.question_type = "boolean"

    def _get_questions(self) -> None:
        params = {}
        params["amount"] = self.number_of_questions
        params["category"] = self.question_category
        params["type"] = self.question_type
        response = requests.get(self.url_questions, params)
        results_to_json = json.loads(response.text)
        raw_questions = results_to_json["results"]
        question_bank = self._process_questions(raw_questions)
        return question_bank

    def _process_questions(self, questions_to_parse) -> None:
        question_bank = []
        for question_dict in questions_to_parse:
            question_text: str = html.unescape(question_dict["question"])
            question_answer: str = question_dict["correct_answer"]
            question = Question(question_text, question_answer)
            question_bank.append(question)
        return question_bank
