"""
    For data for booking page
"""
from typing import Optional

from database.models import Teacher


class FormData:
    """
       Form data service
    """

    def __init__(self, teacher_id: int, week: str, time: int):
        """
        Construct data for  booking

        :param id: int
        :param week: str
        :param time: int
        """
        self.id = teacher_id
        self.week = week
        self.time = time
        self.data: dict = {}

    def form_data(self) -> Optional[dict]:
        """
        Returning data formed data

        :return: dict
        """
        self.data["id"] = self.id
        self.data["week"] = self.week
        self.data["time"] = self.time
        self.data["name"] = Teacher.query.filter(Teacher.id == self.id).first().name

        return self.data
