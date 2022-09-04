from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html

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
