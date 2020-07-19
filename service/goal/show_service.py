"""
   Filter teachers by goal
"""
from typing import Type

from service.json_service import JsonService


class ShowService:
    """
    Get tutors by goals
    """

    def __init__(
        self,
        goal: str,
        db_name: str = "teachers",
        *,
        service: Type[JsonService] = JsonService
    ):
        """
        Init service to get instructors by goal
        """
        self.goal = goal
        self._service = service(db_name)

    def get(self) -> list:
        """
        Return sorted list of teachers
        """

        data: list = self._service.filter("goals", self.goal).sort(
            "rating", desc=True
        ).all()

        return data
