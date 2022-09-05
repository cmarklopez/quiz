from quiz_brain import QuizBrain
from quiz_bank import QuizBank
from quiz_categories import QuizCategories


MAX_NUMBER_QUESTIONS = 20


def enter_category(quiz_category: QuizCategories) -> int:
    while True:
        user_input = input("Enter an ID from the list above.\n")
        try:
            user_input = int(user_input)
        except ValueError:
            continue
        else:
            if user_input in quiz_category.categories.keys():
                break
            else:
                continue
    return user_input


def enter_number(max_questions: int) -> int:
    number_of_questions = min(max_questions, MAX_NUMBER_QUESTIONS)
    while True:
        user_input = input(
            f"Choose a number of questions from 1 to {number_of_questions}.\n"
        )
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
    print(my_quiz_category)
    my_category = enter_category(my_quiz_category)
    avalable_question_count = my_quiz_category.max_questions_category(my_category)
    number_of_questions = enter_number(avalable_question_count)

    my_quiz_bank = QuizBank(my_category, number_of_questions)

    quiz = QuizBrain(my_quiz_bank.questions)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You have completed the quiz.")
    print(f"your final score is {quiz.score}/{quiz.question_number}")


if __name__ == "__main__":
    main()
