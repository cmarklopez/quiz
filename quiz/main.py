from question_model import Question
from quiz_brain import QuizBrain
import html
import requests
import json

url = "https://opentdb.com/api.php"

params = {
    "amount": 10,
    "category": 11,
    "type": "boolean",
}

response = requests.get(url, params)
results_to_json = json.loads(response.text)
question_data = results_to_json["results"]

question_bank = []

for question_dict in question_data:
    question_text = html.unescape(question_dict["question"])
    question_answer = question_dict["correct_answer"]
    question = Question(question_text, question_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"your final score is {quiz.score}/{quiz.question_number}")
