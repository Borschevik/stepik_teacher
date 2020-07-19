"""
Save data to JSON db
"""
from typing import Type

from flask_wtf import FlaskForm

from service.json_service import JsonService


class SaveData:

    def __init__(self, form: FlaskForm, db_name: str, *, service: Type[JsonService] = JsonService):
        """
        Db to save
        :param db_name: str
        """
        self._service = service(db_name)
        self._form: FlaskForm = form


    def save(self) -> dict:
        """
        Save data from Flask Form

        :return: dict
        """
        entry = self._parse_form()
        self._service.add(entry)

        return entry

    def _parse_form(self):
        """
        Parse Form
        """
        entry: dict = dict()
        for field in self._form:
            if not field.name.startswith('csrf'):
                entry.update({field.name: field.data})
        return entry
