from src.vacancy import Vacancy


def test_vacancy_creation():
    """Тест для создания вакансий."""
    vac = Vacancy(
        title="Python Developer",
        url="http://hh.ru/vacancy/123",
        salary_from=100000,
        salary_to=150000,
        currency="RUB",
        description="Test job",
    )
    assert vac.title == "Python Developer"
    assert vac.url == "http://hh.ru/vacancy/123"
    assert vac.salary_from == 100000
    assert vac.salary_to == 150000
    assert vac.currency == "RUB"
    assert vac.salary == 125000  # средняя зарплата
    assert vac.description == "Test job"


def test_vacancy_comparison():
    """тест для сравнения вакансий."""
    vac1 = Vacancy("A", "https://url1", 100000, 200000, "RUB")
    vac2 = Vacancy("B", "https://url2", 150000, 250000, "RUB")
    assert vac1 < vac2
    assert vac2 > vac1
    assert vac1 <= vac2
    assert vac2 >= vac1
    vac3 = Vacancy("C", "https://url3", 150000, 250000, "RUB")
    assert vac2 == vac3


def test_cast_to_object_list():
    """Тест приведения объектов к списку."""
    raw = [
        {
            "name": "Dev",
            "alternate_url": "http://hh.ru/vac/1",
            "salary": {"from": 100000, "to": 150000, "currency": "RUB"},
            "snippet": {"responsibility": "Test"},
        },
        {
            "name": "QA",
            "alternate_url": "http://hh.ru/vac/2",
            "salary": None,
            "snippet": {"responsibility": "Test QA"},
        },
    ]
    vacancies = Vacancy.cast_to_object_list(raw)
    assert len(vacancies) == 2
    assert vacancies[0].title == "Dev"
    assert vacancies[1].salary == 0
