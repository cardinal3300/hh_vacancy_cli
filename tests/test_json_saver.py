import os

import pytest

from src.json_saver import JSONSaver
from src.vacancy import Vacancy

TEST_FILE = "tests/test_vacancies.json"


@pytest.fixture
def saver():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    return JSONSaver(filename=TEST_FILE)


def test_add_and_get_vacancy(saver):
    vac = Vacancy("Dev", "https://url", 100000, 150000, "RUB", "Test")
    saver.add_vacancy(vac.to_dict())
    data = saver.get_vacancies()
    assert len(data) == 1
    assert data[0]["title"] == "Dev"
