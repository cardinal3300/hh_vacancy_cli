import requests
from src.parser import Parser


class HH(Parser):
    """
    Класс для работы с API HeadHunter.
    Наследуется от Parser.
    """

    def __init__(self, file_worker):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies: list[dict] = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword: str) -> list[dict]:
        """
        Загружает вакансии с hh.ru по ключевому слову.
        По умолчанию максимум 20 страниц × 100 вакансий = 2000.
        """
        self.params["text"] = keyword
        self.params["page"] = 0
        self.vacancies = []

        while self.params.get("page") < 20:  # ограничение hh.ru
            response = requests.get(self.url, headers=self.headers, params=self.params)
            response.raise_for_status()
            vacancies = response.json().get("items", [])
            if not vacancies:
                break
            self.vacancies.extend(vacancies)
            self.params["page"] += 1

        return self.vacancies
