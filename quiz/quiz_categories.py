import html
import requests


class QuizCategories:
    """This class obtains a list of all question categories from the Open Trivia DB,
    and stores and manages them
    """

    url_categories = "https://opentdb.com/api_category.php"
    url_max_questions = "https://opentdb.com/api_count.php"

    def __init__(self) -> None:
        self.categories = self._get_categories()

    def __str__(self) -> str:
        if self.categories is not None:
            return "".join(
                f"{id}: {category}\n" for id, category in self.categories.items()
            )
        else:
            return ""

    def _get_categories(self) -> dict[int, str]:
        """Get a list of all categories from the API"""
        try:
            response = requests.get(self.url_categories, timeout=30)
        except requests.ConnectionError:
            raise
        except requests.Timeout:
            raise
        except requests.RequestException:
            raise
        else:
            results_to_json = response.json()
            category_list = html.unescape(results_to_json["trivia_categories"])
            return {
                category_dict["id"]: category_dict["name"]
                for category_dict in category_list
            }

    def max_questions_category(self, category_id: int) -> int:
        """Get the total number of questions for the chosen category from the API

        :param category_id: int, The category chosen by the player for the game.
        """
        params = {"category": category_id}
        try:
            response = requests.get(self.url_max_questions, params)
        except requests.ConnectionError:
            raise
        except requests.Timeout:
            raise
        except requests.RequestException:
            raise
        else:
            max_questions_dict = response.json()
            return max_questions_dict["category_question_count"]["total_question_count"]
