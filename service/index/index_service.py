"""
   Index tutors on the page
"""
from sqlalchemy.sql.expression import func

from database.models import Teacher
from utils.util_models import get_goals


class IndexService:
    """
       Get tutors for page
    """

    @staticmethod
    def get() -> list:
        """
         Get random list of tutors
        """
        return [
            entry.__dict__
            for entry in Teacher.query.order_by(func.random()).limit(6).all()
        ]

    @staticmethod
    def get_goals() -> dict:
        """
        :return: dict with goals
        """

        return get_goals()

    @staticmethod
    def all() -> list:
        """
        Get list of all tutors
        """
        return [entry.__dict__ for entry in Teacher.query.all()]
