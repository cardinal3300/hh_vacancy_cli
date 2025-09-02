import json
from pathlib import Path
from typing import Any


class JSONSaver:
    """
    Класс для сохранения, чтения и удаления вакансий в JSON-файле.
    Используется в связке с Parser.
    """

    def __init__(self, filename: str = "data/vacancies.json"):
        self.file = Path(filename)
        self.file.parent.mkdir(parents=True, exist_ok=True)  # создаём папку, если её нет

    def _load(self) -> list[dict]:
        """Загружает список вакансий из JSON."""
        if self.file.exists():
            with open(self.file, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def _save(self, data: list[dict]) -> None:
        """Сохраняет список вакансий в JSON."""
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add_vacancies(self, vacancies: list[dict]) -> None:
        """Добавляет вакансии в файл."""
        data = self._load()
        data.extend(vacancies)
        self._save(data)

    def get_vacancies(self, criteria: dict[str, Any]) -> list[dict]:
        """Фильтрует вакансии по критериям (ключ=значение)."""
        data = self._load()
        if not criteria:
            return data

        result = []
        for v in data:
            if all(str(v.get(k, "")).lower().find(str(val).lower()) != -1 for k, val in criteria.items()):
                result.append(v)
        return result

    def delete_vacancy(self, vacancy: dict) -> None:
        """Удаляет вакансию по URL."""
        data = self._load()
        data = [v for v in data if v.get("url") != vacancy.get("url")]
        self._save(data)
