from src.hh import HH
from src.vacancy import Vacancy
from src.json_saver import JSONSaver
from src.utils import sort_vacancies, get_top_vacancies, filter_vacancies


def user_interaction():
    saver = JSONSaver()
    hh = HH(file_worker=saver)

    query = input("Введите поисковый запрос: ")
    hh.load_vacancies(query)

    # приводим "сырые" вакансии в список объектов Vacancy
    vacancies = Vacancy.cast_to_object_list(hh.vacancies)

    # сохраняем в JSON
    for v in vacancies:
        saver.add_vacancies(v)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    keywords = input("Введите ключевые слова для фильтрации: ").split()

    filtered = filter_vacancies(vacancies, keywords) if keywords else vacancies
    sorted_vac = sort_vacancies(filtered)
    top_vac = get_top_vacancies(sorted_vac, top_n)

    for v in top_vac:
        print(f"{v.title} | {v.salary} | {v.url}")


if __name__ == "__main__":
    user_interaction()