from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Optional


class Parser(ABC):
    """
    Абстрактный базовый класс для работы с API сервисов вакансий.

    SRP: класс отвечает только за контракт взаимодействия с API.
    OCP: новые провайдеры (HH, SuperJob и т.д.) добавляются через наследование.
    """

    def __init__(
        self,
        base_url: str,
        headers: Optional[dict[str, str]] = None,
        timeout: float = 10.0,
    ) -> None:
        """
        :param base_url: Базовый URL API.
        :param headers: Заголовки по умолчанию.
        :param timeout: Таймаут запросов в секундах.
        """
        self._base_url: str = base_url
        self._headers: dict[str, str] = headers or {}
        self._timeout: float = timeout

    @abstractmethod
    def _connect(
        self,
        endpoint: str = "",
        params: Optional[dict[str, Any]] = None,
    ) -> Any:
        """
        Подключение к API (без реализации).
        Дочерний класс обязан выполнить запрос к base_url (+ endpoint),
        проверить статус-код и вернуть ответ (обычно requests.Response).
        """
        raise NotImplementedError

    @abstractmethod
    def get_vacancies(self, keyword: str, per_page: int = 50) -> list[dict[str, Any]]:
        """
        Получение вакансий по ключевому слову (без реализации).
        Дочерний класс обязан сформировать параметры (минимум text, per_page),
        обратиться к _connect и вернуть список словарей из ключа 'items'.
        """
        raise NotImplementedError
