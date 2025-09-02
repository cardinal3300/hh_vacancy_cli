from typing import List, Dict, Any
from src.hh import HH
from src.vacancy import Vacancy
from src.json_saver import JSONSaver
from src.utils import sort_vacancies, get_top_vacancies, filter_vacancies


def user_interaction() -> None:
    """
    Функция взаимодействия с пользователем.
    Позволяет искать вакансии, фильтровать, выводить топ-N и сохранять в JSON.
    """
    # Создаём экземпляры классов
    hh_api = HH()
    saver = JSONSaver()

    # --- Получаем ключевое слово для поиска ---
    query: str = input("Введите поисковый запрос для вакансий: ").strip()
    per_page: int = int(input("Сколько вакансий загружать за один запрос (например, 50): ").strip())

    # --- Получаем вакансии из HH ---
    raw_vacancies: List[Dict[str, Any]] = hh_api.get_vacancies(query, per_page=per_page)
    vacancies: List[Vacancy] = Vacancy.cast_to_object_list(raw_vacancies)

    # --- Сохраняем все вакансии в JSON ---
    for vac in vacancies:
        saver.add_vacancy(vac.to_dict())

    # --- Фильтрация ---
    keyword_input: str = input("Введите ключевые слова для фильтрации вакансий через пробел (Enter — без фильтра): ").strip()
    keywords: List[str] = keyword_input.split() if keyword_input else []
    filtered_vacancies: List[Vacancy] = filter_vacancies(vacancies, keywords) if keywords else vacancies

    # --- Сортировка и топ-N ---
    top_n: int = int(input("Введите количество вакансий для вывода в топ-N: ").strip())
    sorted_vacancies: List[Vacancy] = sort_vacancies(filtered_vacancies)
    top_vacancies: List[Vacancy] = get_top_vacancies(sorted_vacancies, top_n)

    # --- Вывод для пользователя ---
    print("\n=== ТОП вакансий ===")
    for idx, vac in enumerate(top_vacancies, start=1):
        print(f"{idx}. {vac}")


if __name__ == "__main__":
    user_interaction()