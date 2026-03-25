from __future__ import annotations

from typing import Any, Optional

import requests

from src.api_base import Parser


class HH(Parser):
    """
    Класс для работы с API HeadHunter.
    Наследуется от Parser и реализует все его абстрактные методы.
    Атрибуты экземпляра — приватные (__...), метод подключения — приватный (__connect).
    """

    def __init__(self, timeout: float = 10.0) -> None:
        """
        :param timeout: Таймаут запросов в секундах.
        """
        base_url = "https://api.hh.ru/vacancies"
        headers = {"User-Agent": "HH-User-Agent"}
        super().__init__(base_url=base_url, headers=headers, timeout=timeout)

        # приватные атрибуты экземпляра
        self.__base_url: str = base_url
        self.__headers: dict[str, str] = headers
        self.__timeout: float = timeout
        self.__session: requests.Session = requests.Session()

    # --- приватный метод подключения (используется внутри get_vacancies) ---
    def __connect(self, params: Optional[dict[str, Any]] = None) -> requests.Response:
        """
        Выполняет GET-запрос к базовому URL HH и проверяет статус-код.
        :param params: Параметры запроса.
        :return: requests.Response при успешном запросе (status_code == 200).
        :raises requests.HTTPError: если код ответа не 200.
        """
        response = self.__session.get(
            self.__base_url,
            headers=self.__headers,
            params=params,
            timeout=self.__timeout,
        )
        if response.status_code != 200:
            # Явная проверка статус-кода + информативная ошибка
            raise requests.HTTPError(
                f"HeadHunter API error: {response.status_code} {response.text}",
                response=response,
            )
        return response

    # --- реализация абстрактного метода (адаптер к приватному подключению) ---
    def _connect(
        self,
        endpoint: str = "",
        params: Optional[dict[str, Any]] = None,
    ) -> requests.Response:
        # endpoint для HH не используется (базовый URL уже указывает на /vacancies),
        # но оставляем сигнатуру для совместимости контракта Parser.
        return self.__connect(params=params)

    # --- основной публичный метод получения данных ---
    def get_vacancies(self, keyword: str, per_page: int = 50) -> list[dict[str, Any]]:
        """
        Получает вакансии HH по ключевому слову.
        Обязательные параметры запроса: text, per_page.
        В методе перед отправкой запроса вызывается приватный __connect(),
        ответ парсится и возвращается список словарей из ключа 'items'.
        """
        params: dict[str, Any] = {
            "text": keyword,
            "per_page": per_page,
        }
        response = self.__connect(params=params)
        payload: dict[str, Any] = response.json()

        items = payload.get("items", [])
        if not isinstance(items, list):
            return []
        # Гарантируем список словарей
        return [item for item in items if isinstance(item, dict)]
