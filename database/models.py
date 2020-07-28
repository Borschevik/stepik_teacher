"""
   ORM models for sqlalchemy library
"""
import json

from config.extenstions import db
from database.basemodel import BaseModel

teacher_to_goal = db.Table(
    "teacher_to_goal",
    db.metadata,
    db.Column(
        "teacher_id", db.Integer, db.ForeignKey("teachers.id", ondelete="CASCADE"),
    ),
    db.Column("goal_id", db.Integer, db.ForeignKey("goals.id", ondelete="CASCADE"),),
)


class Teacher(BaseModel):
    """ Model for teachers """

    __tablename__ = "teachers"

    name = db.Column(db.String, nullable=False)
    about = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, default=0.0)
    picture = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, default=0)
    free_raw = db.Column(db.Text)
    bookings = db.relationship("Booking", passive_deletes=True)
    goals = db.relationship("Goal", secondary=teacher_to_goal)

    def __init__(self, **kwargs):
        """Init models"""
        super(Teacher, self).__init__(**kwargs)
        self.free_raw: str = json.dumps(kwargs.get("free"))

    @property
    def free(self) -> dict:
        """
        Deserialize property

        :return: dict
        """
        return json.loads(self.free_raw)

    @free.setter
    def free(self, value: dict):
        """
        Serialize property
        """
        self.free_raw = json.dumps(value)

    def get_goals(self) -> list:
        """
        Return goals for teacher as list

        :return: list
        """
        return [goal.eng for goal in self.goals]


class Booking(BaseModel):
    """
    Booking model
    """

    __tablename__ = "bookings"

    weekday = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id", ondelete="CASCADE"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"))


class Request(BaseModel):
    """
    Request model
    """

    __tablename__ = "requests"

    goal = db.Column(db.String)
    time = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"))


class User(BaseModel):
    """
    User model
    """

    __tablename__ = "users"

    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    requests = db.relationship("Request", passive_deletes=True)

    bookings = db.relationship("Booking", passive_deletes=True)


class Goal(BaseModel):
    """
    Goal model
    """

    __tablename__ = "goals"

    eng = db.Column(db.String)
    ru = db.Column(db.String)
    smile = db.Column(db.String)
    teachers = db.relationship("Teacher", secondary=teacher_to_goal)
