"""
   Index tutors on the page
"""
import random
from typing import Type

from service.json_service import JsonService


class IndexService:
    """
       Get tutors for page
    """

    def __init__(self, *, service: Type[JsonService] = JsonService):
        """
        Init for index
        """
        self._service = service("teachers")

    def get(self) -> list:
        """
         Get random list of tutors
        """
        return random.choices(self._service.all(), k=6)

    @staticmethod
    def get_goals() -> dict:
        """
        Get goals
        :return: dict with goals
        """
        return JsonService("goals").all()

    def all(self) -> list:
        """
        Get random list of tutors
        """
        return self._service.all()
