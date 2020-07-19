# pylint: disable=W0612
from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField
from wtforms.fields.html5 import TelField


class BookingForm(FlaskForm):
    """
    Form for booking
    """

    weekday = HiddenField("client_weekday")
    time = HiddenField("client_time")
    teacher = HiddenField("client_teacher")
    name = StringField("Вас зовут")
    phone = TelField("Ваш телефон")
