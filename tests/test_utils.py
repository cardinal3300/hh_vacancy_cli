import pytest

from src.utils import filter_vacancies, get_top_vacancies, sort_vacancies
from src.vacancy import Vacancy


@pytest.fixture
def sample_vacancies():
    return [
        Vacancy("A", "https://url1", 100000, 200000, "RUB"),
        Vacancy("B", "https://url2", 150000, 250000, "RUB"),
        Vacancy("C", "https://url3", None, None, "RUB"),
    ]


def test_sort_vacancies(sample_vacancies):
    sorted_list = sort_vacancies(sample_vacancies)
    assert sorted_list[0].title == "B"
    assert sorted_list[-1].title == "C"


def test_get_top_vacancies(sample_vacancies):
    top2 = get_top_vacancies(sample_vacancies, 2)
    assert len(top2) == 2
    assert top2[0].salary >= top2[1].salary


def test_filter_vacancies(sample_vacancies):
    filtered = filter_vacancies(sample_vacancies, ["A"])
    assert len(filtered) == 1
    assert filtered[0].title == "A"
