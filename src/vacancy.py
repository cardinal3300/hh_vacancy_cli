from __future__ import annotations

from typing import Any, Dict, List


class Vacancy:
    """
    Класс для представления вакансии.
    Использует __slots__ для экономии памяти.
    Атрибуты:
        __title (str): Название вакансии.
        __url (str): Ссылка на вакансию.
        __salary_from (int | None): Минимальная зарплата.
        __salary_to (int | None): Максимальная зарплата.
        __currency (str): Валюта зарплаты.
        __description (str): Описание вакансии.
    """
    __slots__ = (
        "__title",
        "__url",
        "__salary_from",
        "__salary_to",
        "__currency",
        "__description",
    )

    def __init__(
        self,
        title: str,
        url: str,
        salary_from: Any = None,
        salary_to: Any = None,
        currency: str = "RUB",
        description: str = "",
    ) -> None:
        self.__title = self.__validate_title(title)
        self.__url = self.__validate_url(url)
        self.__salary_from = self.__validate_salary(salary_from)
        self.__salary_to = self.__validate_salary(salary_to)
        self.__currency = self.__validate_currency(currency)
        self.__description = description or "Описание отсутствует"

    # ------------------ методы для работы ------------------

    def average_salary(self) -> float:
        """
        Возвращает среднюю зарплату.
        Если указана только одна граница, берётся она.
        Если обе None → 0.0.
        """
        if self.__salary_from and self.__salary_to:
            return (self.__salary_from + self.__salary_to) / 2
        if self.__salary_from:
            return self.__salary_from
        if self.__salary_to:
            return self.__salary_to
        return 0.0

    # ------------------ приватные методы валидации ------------------

    def __validate_title(self, title: Any) -> str:
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Некорректное название вакансии")
        return title.strip()

    def __validate_url(self, url: Any) -> str:
        if not isinstance(url, str) or not url.startswith("http"):
            raise ValueError("Некорректная ссылка на вакансию")
        return url

    def __validate_salary(self, salary: Any) -> int | None:
        if salary is None:
            return None
        if not isinstance(salary, (int, float)) or salary < 0:
            raise ValueError("Некорректное значение зарплаты")
        return int(salary)

    def __validate_currency(self, currency: Any) -> str:
        if not isinstance(currency, str) or len(currency) > 5:
            raise ValueError("Некорректная валюта")
        return currency.upper()

    # ------------------ свойства ------------------

    @property
    def title(self) -> str:
        return self.__title

    @property
    def url(self) -> str:
        return self.__url

    @property
    def salary_from(self) -> int | None:
        return self.__salary_from

    @property
    def salary_to(self) -> int | None:
        return self.__salary_to

    @property
    def currency(self) -> str:
        return self.__currency

    @property
    def description(self) -> str:
        return self.__description

    @property
    def salary(self) -> int:
        """Средняя зарплата (если нет данных, возвращает 0)."""
        if self.__salary_from and self.__salary_to:
            return (self.__salary_from + self.__salary_to) // 2
        return self.__salary_from or self.__salary_to or 0

    # ------------------ магические методы сравнения ------------------

    def __str__(self) -> str:
        return f"{self.__title} | {self.salary} {self.__currency} | {self.__url}"

    def __repr__(self) -> str:
        return f"Vacancy({self.__title!r}, {self.salary!r}, {self.__currency!r})"

    def __eq__(self, other: Vacancy) -> bool:
        return self.salary == other.salary

    def __lt__(self, other: Vacancy) -> bool:
        return self.salary < other.salary

    def __le__(self, other: Vacancy) -> bool:
        return self.salary <= other.salary

    def __gt__(self, other: Vacancy) -> bool:
        return self.salary > other.salary

    def __ge__(self, other: Vacancy) -> bool:
        return self.salary >= other.salary

    # ------------------ представление ------------------

    def __repr__(self) -> str:
        return (
            f"Vacancy(title='{self.__title}', salary={self.average_salary()} {self.__currency})"
        )

    def __str__(self) -> str:
        return f"{self.__title} — {self.average_salary()} {self.__currency} ({self.__url})"

    # ------------------ класс методы ------------------

    @classmethod
    def cast_to_object_list(cls, vacancies: List[Dict[str, Any]]) -> List["Vacancy"]:
        """
        Преобразует список словарей в список объектов Vacancy.
        """
        result: List[Vacancy] = []
        for v in vacancies:
            salary_from = None
            salary_to = None
            currency = "RUB"

            # Если зарплата приходит в формате словаря
            if isinstance(v.get("salary"), dict):
                salary_from = v["salary"].get("from")
                salary_to = v["salary"].get("to")
                currency = v["salary"].get("currency") or "RUB"

            result.append(
                cls(
                    title=v.get("name", "Без названия"),
                    url=v.get("alternate_url", ""),
                    salary_from=salary_from,
                    salary_to=salary_to,
                    currency=currency,
                    description=v.get("snippet", {}).get("responsibility", ""),
                )
            )
        return result

    def to_dict(self) -> Dict[str, Any]:
        """
        Преобразует объект Vacancy в словарь для сохранения в JSON.
        """
        return {
            "title": self.__title,
            "url": self.__url,
            "salary_from": self.__salary_from,
            "salary_to": self.__salary_to,
            "currency": self.__currency,
            "description": self.__description,
        }
