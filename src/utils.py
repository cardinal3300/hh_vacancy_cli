from src.vacancy import Vacancy

def sort_vacancies(vacancies: list[Vacancy]) -> list[Vacancy]:
    return sorted(vacancies, key=lambda v: v.salary, reverse=True)

def get_top_vacancies(vacancies: list[Vacancy], n: int) -> list[Vacancy]:
    return vacancies[:n]

def filter_vacancies(vacancies: list[Vacancy], keywords: list[str]) -> list[Vacancy]:
    return [v for v in vacancies if any(kw.lower() in v.description.lower() for kw in keywords)]
