from typing import List

from src.vacancy import Vacancy


def sort_vacancies(vacancies: List[Vacancy], reverse: bool = True) -> List[Vacancy]:
    """
    Сортирует вакансии по зарплате.
    :param vacancies: список объектов Vacancy
    :param reverse: сортировка по убыванию (по умолчанию True)
    :return: отсортированный список вакансий
    """
    return sorted(vacancies, reverse=reverse)


def get_top_vacancies(vacancies: List[Vacancy], top_n: int) -> List[Vacancy]:
    """
    Возвращает топ-N вакансий по зарплате.
    :param vacancies: список объектов Vacancy
    :param top_n: количество вакансий
    :return: список топ-N вакансий
    """
    sorted_list = sort_vacancies(vacancies)
    return sorted_list[:top_n]


def filter_vacancies(vacancies: List[Vacancy], keywords: List[str]) -> List[Vacancy]:
    """
    Фильтрует вакансии по ключевым словам в названии или описании.
    :param vacancies: список объектов Vacancy
    :param keywords: список ключевых слов
    :return: список вакансий, содержащих хотя бы одно ключевое слово
    """
    filtered = []
    for vac in vacancies:
        text = f"{vac.title} {vac.description}".lower()
        if any(kw.lower() in text for kw in keywords):
            filtered.append(vac)
    return filtered
