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
        category_list = ""
        for id, category in self.categories.items():
            category_list += f"{id}: {category}\n"
        return category_list

    def _get_categories(self) -> dict[int, str]:
        """Get a list of all categories from the API"""
        category_dict_temp: dict[int, str] = {}
        try:
            response = requests.get(self.url_categories, timeout=30)
        except requests.ConnectionError as e:
            print("OOPS!! Connection Error. Make sure you are connected to Internet.\n")
            print(str(e))
        except requests.Timeout as e:
            print("OOPS!! Timeout Error")
            print(str(e))
        except requests.RequestException as e:
            print("OOPS!! General Error")
            print(str(e))
        except KeyboardInterrupt:
            print("Someone closed the program")
        else:
            results_to_json = response.json()
            category_list = html.unescape(results_to_json["trivia_categories"])
            for category_dict in category_list:
                category_id = category_dict["id"]
                category_name = category_dict["name"]
                category_dict_temp[category_id] = category_name
        return category_dict_temp

    def max_questions_category(self, category_id: int) -> int:
        """Get the total number of questions for the chosen category from the API

        :param category_id: int, The category chosen by the player for the game.
        """
        params = {"category": category_id}
        max_questions = 0
        try:
            response = requests.get(self.url_max_questions, params)
        except requests.ConnectionError as e:
            print("OOPS!! Connection Error. Make sure you are connected to Internet.\n")
            print(str(e))
        except requests.Timeout as e:
            print("OOPS!! Timeout Error")
            print(str(e))
        except requests.RequestException as e:
            print("OOPS!! General Error")
            print(str(e))
        except KeyboardInterrupt:
            print("Someone closed the program")
        else:
            max_questions_dict = response.json()
            max_questions = max_questions_dict["category_question_count"][
                "total_question_count"
            ]
        return max_questions
