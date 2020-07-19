"""
    For data for booking page
"""
from typing import Optional, Type

from service.json_service import JsonService


class FormData:
    def __init__(self, teacher_id: int, week: str, time: int, * , service: Type[JsonService] = JsonService):
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
        self._service = service("teachers")

    def form_data(self) -> Optional[dict]:
        """
        Returning data formed data

        :return: dict
        """
        self.data["id"] = self.id
        self.data["week"] = self.week
        self.data["time"] = self.time
        self.data["name"] = self._service.filter("id", self.id).first()[0].get("name")

        return self.data
