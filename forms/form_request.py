"""
    Form for request
"""
from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, validators
from wtforms.fields.html5 import TelField

from config.config import TIME_INT
from utils.util_form import create_choices
from utils.util_models import get_goals


class FormRequest(FlaskForm):
    """
    Class with forms for request
    """

    goal = RadioField("goal", choices=create_choices(get_goals()))
    time = RadioField("time", choices=create_choices(TIME_INT))
    name = StringField(
        "Вас зовут",
        [
            validators.DataRequired(message="Требуется ваше имя"),
            validators.Length(min=2, max=25, message="Имя слишком короткое"),
        ],
    )
    phone = TelField(
        "Ваш телефон",
        [
            validators.DataRequired(message="Требуется ваш телефон"),
            validators.Length(min=6, max=25, message="Номер слишком короткий"),
        ],
    )
