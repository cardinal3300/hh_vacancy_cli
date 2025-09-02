from typing import Any


class Vacancy:
    """Класс для представления вакансии."""

    def __init__(self, title: str, url: str, salary: int | str, description: str) -> None:
        self.title = title
        self.url = url
        self.salary = self._validate_salary(salary)
        self.description = description

    def __repr__(self) -> str:
        return f"Vacancy({self.title}, {self.salary}, {self.url})"

    def __str__(self) -> str:
        return f"{self.title} | {self.salary} | {self.url}"

    # Методы сравнения по зарплате
    def __lt__(self, other: "Vacancy") -> bool:
        return self.salary < other.salary

    def __le__(self, other: "Vacancy") -> bool:
        return self.salary <= other.salary

    def __gt__(self, other: "Vacancy") -> bool:
        return self.salary > other.salary

    def __ge__(self, other: "Vacancy") -> bool:
        return self.salary >= other.salary

    @staticmethod
    def _validate_salary(salary: Any) -> int:
        """Проверка корректности зарплаты, возврат int или 0, если нет данных."""
        if isinstance(salary, int):
            return salary
        if isinstance(salary, dict):
            return salary.get("from") or 0
        return 0

    @classmethod
    def cast_to_object_list(cls, raw_vacancies: list[dict[str, Any]]) -> list["Vacancy"]:
        """Преобразование списка словарей (из API) в список объектов Vacancy."""
        objects = []
        for v in raw_vacancies:
            title = v.get("name", "Без названия")
            url = v.get("alternate_url", "")
            salary = v.get("salary")
            description = v.get("snippet", {}).get("requirement", "")
            objects.append(cls(title, url, salary, description))
        return objects
