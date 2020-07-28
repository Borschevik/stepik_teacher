import os
from pathlib import Path

ROOT_DIR: Path = Path(__file__).parent.parent
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI: str = "postgresql+psycopg2://postgres:admin@127.0.0.1:5432/test"
MIGRATION_DIR = os.path.join(ROOT_DIR, "database", "migrations")


DAY_MAP: dict = {
    "mon": "Понедельник",
    "tue": "Вторник",
    "wed": "Среда",
    "thu": "Четверг",
    "fri": "Пятница",
    "sat": "Суббота",
    "sun": "Воскресенье",
}


TIME_MAP: dict = {
    8: "8:00",
    10: "10:00",
    12: "12:00",
    14: "14:00",
    16: "16:00",
    18: "18:00",
    20: "20:00",
    22: "22:00",
}


TIME_INT: dict = {
    "1-2": "1-2 часа в неделю",
    "3-5": "3-5 часа в неделю",
    "5-7": "5-7 часа в неделю",
    "7-10": "7-10 часа в неделю",
}
