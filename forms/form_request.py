"""
    Form for request
"""
from flask_wtf import FlaskForm
from wtforms import RadioField, StringField

from config.config import TIME_INT
from service.json_service import JsonService
from utils.util_form import create_choices


class FormRequest(FlaskForm):
    """
    Class with forms for request
    """

    goal = RadioField("goal", choices=create_choices(JsonService("goals").all()))
    time = RadioField("time", choices=create_choices(TIME_INT))
    name = StringField("Вас зовут")
    phone = StringField("Ваш телефон")
