import html
import requests


class QuizCategories:
    url_categories = "https://opentdb.com/api_category.php"

    def __init__(self) -> None:
        self.categories = self._get_categories()

    def __str__(self) -> str:
        category_list = ""
        for id, category in self.categories.items():
            category_list += f"{id}: {category}\n"
        return category_list

    def _get_categories(self) -> dict[int, str]:
        response = requests.get(self.url_categories)
        results_to_json = response.json()
        category_list = html.unescape(results_to_json["trivia_categories"])
        category_dict_temp: dict[int, str] = {}
        for category_dict in category_list:
            category_id = category_dict["id"]
            category_name = category_dict["name"]
            category_dict_temp[category_id] = category_name
        return category_dict_temp
