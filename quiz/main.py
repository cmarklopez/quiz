from quiz_brain import QuizBrain
from quiz_bank import QuizBank
from quiz_categories import QuizCategories
import requests


MAX_NUMBER_OF_QUESTIONS = 20


def enter_category(quiz_category: QuizCategories) -> int:
    """
    Prompt the player to input the ID of the category of questions to use for the game.

    :param quiz_category: QuizCategory, the object used to pull the categories from
        the Open Trivia DB API and store them.

    :return: The ID of the queestion category chosen by the player.
    """
    while True:
        user_input = input("Enter an ID from the list above.\n")
        try:
            user_input = int(user_input)
        except ValueError:
            continue
        if user_input in quiz_category.categories.keys():
            return user_input


def enter_number(max_questions: int) -> int:
    """
    Prompt the player to input the number of questions to use for the game.

    :param max_questions: int, the total number of questions in the Open Trivia DB
        that match the criteria for the current game

    :return: The number of questions for the game as chosen by the player.
    """
    number_of_questions = min(max_questions, MAX_NUMBER_OF_QUESTIONS)
    while True:
        user_input = input(
            f"Choose a number of questions from 1 to {number_of_questions}.\n"
        )
        try:
            user_input = int(user_input)
        except ValueError:
            continue
        if 1 <= user_input <= number_of_questions:
            return user_input


def main():
    """The entry point for the program. Orchestrates game flow."""
    try:
        my_quiz_category = QuizCategories()
    except requests.RequestException:
        print("Unable to contact server. Please check your internet connection.")
        return

    print(my_quiz_category)
    my_category = enter_category(my_quiz_category)

    try:
        avalable_question_count = my_quiz_category.max_questions_category(my_category)
    except requests.RequestException:
        print("Unable to contact server. Please check your internet connection.")
        return

    number_of_questions = enter_number(avalable_question_count)

    try:
        my_quiz_bank = QuizBank(my_category, number_of_questions)
    except requests.RequestException:
        print("Unable to contact server. Please check your internet connection.")
        return

    quiz = QuizBrain(my_quiz_bank.questions)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You have completed the quiz.")
    print(f"your final score is {quiz.score}/{quiz.question_number}")


if __name__ == "__main__":
    main()
