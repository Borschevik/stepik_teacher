"""
Save data to DB
"""
from importlib import import_module

from flask_wtf import FlaskForm

from database.models import Teacher
from utils.util_models import make_user


class SaveData:
    """
       Save data service
    """

    def __init__(self, form: FlaskForm, model_name: str):
        """
        Db to save
        :param db_name: str
        """
        self._model_name = model_name
        self._form: FlaskForm = form
        self._exclude_keys: list = ["name", "phone"] if model_name == "Request" else [
            "name",
            "phone",
            "teacher",
        ]

    def save(self) -> dict:
        """
        Save data from Flask Form

        :return: dict
        """
        entry = self._parse_form()

        return entry

    def _parse_form(self):
        """
        Parse Form
        """
        entry: dict = dict()
        for field in self._form:
            if not field.name.startswith("csrf"):
                entry.update({field.name: field.data})

        model = getattr(import_module("database.models"), self._model_name)
        users = make_user(entry)
        params = self._get_params(entry)

        if self._model_name == "Request":
            ent = model(**params).add()
            users.requests.append(ent)
            users.save()
        elif self._model_name == "Booking":
            teacher = Teacher.query.filter(
                Teacher.id == int(entry.get("teacher"))
            ).first()
            ent = model(**params)
            teacher.bookings.append(ent)
            users.bookings.append(ent)
            teacher.add()
            users.add()
            ent.save()

        return entry

    def _get_params(self, params: dict):
        """
        :return: filteted dict
        """
        return {
            k: params[k] for k in set(list(params.keys())) - set(self._exclude_keys)
        }
