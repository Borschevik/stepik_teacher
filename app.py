# pylint: disable=W0621,W0622,W0613
"""Flask app"""
from typing import Optional

from flask import Flask, render_template

from config.extenstions import db, migrate
from forms.booking_form import BookingForm
from forms.form_request import FormRequest
from service.booking.form_data import FormData as BookingFormData
from service.goal.show_service import ShowService
from service.index.index_service import IndexService
from service.profile.profile_service import ProfileService
from service.save_data import SaveData


def add_cli_commands(app: Flask):
    """
    Add cli commands for flask servie

    :param app:
    """
    # pylint: disable=C0415
    from cli.commands.cli_create_db import db_tasks

    app.cli.add_command(db_tasks)


def register_filters(app: Flask):
    """
    Add new jinja filters

    :param app:
    """
    # pylint: disable=C0415
    from utils.util_templates import (
        get_goal,
        get_hour,
        get_nav_item,
        get_ru_week,
        get_str_time,
        get_smiles,
        lower_byindex,
    )

    app.jinja_env.filters["get_hour"] = get_hour
    app.jinja_env.filters["get_ru_week"] = get_ru_week
    app.jinja_env.filters["get_str_time"] = get_str_time
    app.jinja_env.filters["get_goal"] = get_goal
    app.jinja_env.filters["lower_byindex"] = lower_byindex
    app.jinja_env.filters["get_smiles"] = get_smiles
    app.jinja_env.filters["get_nav_item"] = get_nav_item


def register_extensions(app: Flask):
    """
    Register extensions for application
    """
    db.init_app(app)
    with app.app_context():
        migrate.init_app(app, db, directory=app.config["MIGRATION_DIR"])


def create_app() -> Flask:
    """
    App facrtory
    """
    app: Flask = Flask(__name__)
    app.config.from_pyfile("config/config.py")
    app.secret_key = "vcnvsjkrfkao"
    app.jinja_env.lstrip_blocks = True
    app.jinja_env.trim_blocks = True
    add_cli_commands(app)
    register_filters(app)
    register_extensions(app)

    return app


app: Flask = create_app()


@app.route("/")
def index():
    """
    Main page

    :return: rendered page
    """
    service = IndexService()
    data: list = service.get()
    goal_data: dict = service.get_goals()

    return render_template("index.html", data=data, goals_dict=goal_data)


@app.route("/tutors/")
def tutors():
    """
    Main page

    :return: rendered page
    """
    service = IndexService()
    data: list = service.all()
    goal_data: dict = service.get_goals()

    return render_template("index.html", data=data, goals_dict=goal_data)


@app.route("/goals/<string:goal>/")
def goals(goal: str):
    """
    Leaning goal

    :param goal: str
    :return: rendered page
    """
    data: list = ShowService(goal).get()

    return render_template("goal.html", data=data, goal=goal)


@app.route("/profiles/<int:id>/")
def profiles(id: int):
    """
    Teacher profiles

    :param id: int
    :return: rendered page
    """
    profile: Optional[dict] = ProfileService(id).parse_data()
    if profile:
        return render_template("profile.html", profile=profile)
    else:
        return render_template("404.html")


@app.route("/request/")
def request_page():
    """
    Request selection

    :return: rendered page
    """
    form = FormRequest()

    return render_template("request.html", form=form)


@app.route("/request_done/", methods=["POST"])
def request_done():
    """
    Request done

    :return: rendered page
    """
    form = FormRequest()
    data: Optional[dict] = SaveData(form, "Request").save()

    return render_template("request_done.html", data=data)


@app.route("/booking/<int:id>/<string:week>/<int:booking_time>/")
def booking(id: int, week: str, booking_time: int):
    """
    Booking form

    :param id: int
    :param week: str
    :param booking_time: int
    :return: rendered page
    """
    data: Optional[dict] = BookingFormData(id, week, booking_time).form_data()
    form: BookingForm = BookingForm()  # noqa: assignment-from-no-return, no-value-for-parameter

    return render_template("booking.html", data=data, form=form)


@app.route("/booking_done/", methods=["POST"])
def booking_done():
    """
    Return when booking is done

    :return: rendered page
    """
    form: BookingForm = BookingForm()
    save: dict = SaveData(form, "Booking").save()

    return render_template("booking_done.html", save=save)


if __name__ == "__main__":
    app.run()
