import json
import os
from typing import Any, Dict, List

from src.saver_base import SaverBase


class JSONSaver(SaverBase):
    """
    Класс для работы с JSON-файлами.
    Реализует добавление, получение и удаление вакансий.
    """
    def __init__(self, filename: str = "vacancies.json") -> None:
        """
        Инициализация экземпляра.
        :param filename: имя файла для сохранения вакансий.
        """
        self.__filename = filename
        # создаём файл, если его нет
        if not os.path.exists(self.__filename):
            with open(self.__filename, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: Dict[str, Any]) -> None:
        """
        Добавляет вакансию в JSON-файл.
        Исключает дублирование по URL.
        """
        vacancies = self.get_vacancies()
        if any(v["url"] == vacancy["url"] for v in vacancies):
            return
        vacancies.append(vacancy)
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def get_vacancies(self) -> List[Dict[str, Any]]:
        """
        Загружает список вакансий из JSON-файла.
        """
        with open(self.__filename, "r", encoding="utf-8") as f:
            return json.load(f)

    def delete_vacancy(self, vacancy_url: str) -> None:
        """
        Удаляет вакансию по URL из файла.
        """
        vacancies = self.get_vacancies()
        vacancies = [v for v in vacancies if v["url"] != vacancy_url]
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)
