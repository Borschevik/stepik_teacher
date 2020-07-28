# pylint: disable=W0612
from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, validators
from wtforms.fields.html5 import TelField


class BookingForm(FlaskForm):
    """
    Form for booking
    """

    weekday = HiddenField("client_weekday")
    time = HiddenField("client_time")
    teacher = HiddenField("client_teacher")
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
