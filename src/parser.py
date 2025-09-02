from abc import ABC, abstractmethod
from typing import Any


class Parser(ABC):
    """
    Родительский абстрактный класс для работы с API сервисов вакансий.
    Все наследники должны реализовать метод load_vacancies.
    """

    def __init__(self, file_worker: Any):
        self.file_worker = file_worker   # объект для сохранения/загрузки данных

    @abstractmethod
    def load_vacancies(self, keyword: str) -> list[dict]:
        """Загружает вакансии по ключевому слову."""
        pass

    def save(self, vacancies: list[dict]) -> None:
        """Сохраняет вакансии через file_worker (например, в JSON)."""
        if not self.file_worker:
            raise ValueError("File worker не передан в Parser")
        self.file_worker.add_vacancies(vacancies)

    def read(self, criteria: dict | None = None) -> list[dict]:
        """Получает вакансии из хранилища по критериям."""
        if not self.file_worker:
            raise ValueError("File worker не передан в Parser")
        return self.file_worker.get_vacancies(criteria or {})

    def delete(self, vacancy: dict) -> None:
        """Удаляет вакансию из хранилища."""
        if not self.file_worker:
            raise ValueError("File worker не передан в Parser")
        self.file_worker.delete_vacancy(vacancy)
