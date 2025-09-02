import socket

import pytest

from src.hh import HH


def network_available(host="hh.ru", port=80, timeout=2) -> bool:
    """
    Проверяет доступность хоста (по умолчанию hh.ru).
    Возвращает True, если соединение удалось, иначе False.
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except OSError:
        return False


@pytest.mark.skipif(not network_available(), reason="Нет подключения к hh.ru")
def test_get_vacancies():
    """
    Интеграционный тест метода get_vacancies класса HH.
    Тест выполняется только при доступности hh.ru.
    """
    api = HH()
    results = api.get_vacancies("Python", per_page=2)

    # Проверяем, что метод вернул список словарей
    assert isinstance(results, list)
    assert len(results) > 0

    # Проверяем ключевые поля первой вакансии
    first_vacancy = results[0]
    assert "name" in first_vacancy
    assert "alternate_url" in first_vacancy

    # Дополнительно проверяем, что значения не пустые
    assert first_vacancy["name"] != ""
    assert first_vacancy["alternate_url"] != ""
