from quiz_brain import QuizBrain
from quiz_bank import QuizBank
from quiz_categories import QuizCategories


MAX_NUMBER_QUESTIONS = 20


def enter_category() -> int:
    while True:
        user_input = input("Enter an ID from the list above.\n")
        try:
            user_input = int(user_input)
            break
        except ValueError:
            continue
    return user_input


def enter_number() -> int:
    while True:
        user_input = input("Choose a number of questions from 1 to 20.\n")
        try:
            user_input = int(user_input)
            break
        except ValueError:
            continue
    if user_input < 1:
        return 1
    elif user_input > MAX_NUMBER_QUESTIONS:
        return MAX_NUMBER_QUESTIONS
    else:
        return user_input


def main():
    my_quiz_category = QuizCategories()
    my_quiz_category.list_categories()
    my_category = enter_category()
    number_of_questions = enter_number()

    my_quiz_bank = QuizBank(my_category, number_of_questions)

    quiz = QuizBrain(my_quiz_bank.questions)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You have completed the quiz.")
    print(f"your final score is {quiz.score}/{quiz.question_number}")


if __name__ == "__main__":
    main()
