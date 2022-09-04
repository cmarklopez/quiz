from quiz_brain import QuizBrain
from quiz_bank import QuizBank
from quiz_categories import QuizCategories

if __name__ == "__main__"":
    my_quiz_category = QuizCategories()
    my_quiz_category.list_categories()
    my_category = int(input("Enter an ID from the list above.\n"))
    number_of_questions = int(input("Choose a number of questions from 1 to 20.\n"))

    my_quiz_bank = QuizBank(my_category, number_of_questions)

    quiz = QuizBrain(my_quiz_bank.questions)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You have completed the quiz.")
    print(f"your final score is {quiz.score}/{quiz.question_number}")
