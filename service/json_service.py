import json
import os
from typing import Any, Union

from config.config import ROOT_DIR


class JsonService:
    """
    Service for getting and performing operations with JSON
    """

    def __init__(self, db_name: str):
        """
        Db to save
        :param db_name: str
        """
        self.db_name = db_name
        self.db_path: str = os.path.join(ROOT_DIR, "database", f"{self.db_name}.json")
        self.data = self.read()

    def add(self, entry: Any) -> dict:
        """
        Save data from Flask Form

        :return: dict
        """
        self.save_to_file(entry)

        return entry

    def read(self):
        """
       Read from json
       """
        if os.path.exists(self.db_path):
            with open(self.db_path, encoding="utf8") as f:
                data: list = json.loads(f.read())
        else:
            data = []
        return data

    def sort(self, value: Any, *, desc: bool = False):
        """
        Sort data
        """
        self.data = sorted(self.data, key=lambda i: i[value], reverse=desc)
        return self

    def filter(self, field: Any, value: Any):
        """
        Filter data
        """
        if isinstance(value, int):
            self.data = list(filter(lambda d: d[field] == value, self.data))
        else:
            self.data = list(filter(lambda d: value in d[field], self.data))

        return self

    def all(self):
        """
        Get all data
        """
        return self.data

    def first(self, *, n: int = 1) -> Union[list, dict]:
        """
        Get first entries
        """
        if isinstance(self.data, dict):
            return {
                k: v
                for k, v in zip(
                    list(self.data.keys())[:n], list(self.data.values())[:n]
                )
            }
        return self.data[:n]

    def save_to_file(self, entry: Union[dict, list]):
        """
        Save to JSON file
        :param file_name: file_name to save
        :param entry: data entry to save
        """
        data: list
        if os.path.exists(self.db_path):
            with open(self.db_path, "r", encoding="utf8") as f:
                data = json.loads(f.read())
        else:
            data = []

        with open(self.db_path, "w", encoding="utf8") as f:
            if entry not in data:
                data.append(entry)
            json.dump(data, f, ensure_ascii=False, indent=4)
