from abc import ABC, abstractmethod
from typing import Any, Dict, List


class SaverBase(ABC):
    """
    Абстрактный класс для работы с файлами.
    Определяет общий интерфейс для сохранения, получения и удаления данных.
    """
    @abstractmethod
    def add_vacancy(self, vacancy: Dict[str, Any]) -> None:
        """
        Добавляет вакансию в файл.
        :param vacancy: словарь с данными вакансии.
        """
        pass

    @abstractmethod
    def get_vacancies(self) -> List[Dict[str, Any]]:
        """
        Получает список вакансий из файла.
        :return: список словарей с вакансиями.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_url: str) -> None:
        """
        Удаляет вакансию по URL.
        :param vacancy_url: ссылка на вакансию.
        """
        pass
