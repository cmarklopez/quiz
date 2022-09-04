from unittest import result
from question_model import Question
import html
import requests
import json

class QuizBank:
    url_categories = "https://opentdb.com/api_category.php"
    categories = []

    def __init__(self, category: int, number: int) -> None:
        self.question_category = category
        self.number_of_questions = number
        self.questions = [Question]
        self.categories = self._get_categories()

    def _get_categories(self) -> None:
        response = requests.get(self.url_categories)
        results_to_json = json.loads(response.text)
        self.categories = results_to_json["trivia_categories"]


    def choose_category(self):
        print(self.categories)
