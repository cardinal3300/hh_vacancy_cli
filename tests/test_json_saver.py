import pytest
from src.vacancy import Vacancy

def test_vacancy_salary_validation():
    v = Vacancy("Python Dev", "url", -100, "desc")
    assert v.salary == 0

def test_vacancy_comparison():
    v1 = Vacancy("A", "url1", 100, "desc")
    v2 = Vacancy("B", "url2", 200, "desc")
    assert v2 > v1
