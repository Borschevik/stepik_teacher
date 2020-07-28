"""
    Service for selecting profile from JSON database
"""
from collections import defaultdict
from typing import Optional

from database.models import Teacher


class ProfileService:
    """
    Service for teacher's profile
    """

    def __init__(self, teacher_id: int):
        """
        :param id: int for teacher id
        """
        self.id = teacher_id
        self.parsed_data: dict = dict()

    def parse_data(self) -> Optional[dict]:
        """
        Read data from JSON file and get by id

        :return: dict with parsed data
        """
        teacher_data: Teacher = self._get_teacher()
        if teacher_data:
            self.parsed_data["id"] = teacher_data.id
            self.parsed_data["name"] = teacher_data.name
            self.parsed_data["about"] = teacher_data.about
            self.parsed_data["rating"] = teacher_data.rating
            self.parsed_data["picture"] = teacher_data.picture
            self.parsed_data["price"] = teacher_data.price
            self.parsed_data["goals"] = teacher_data.get_goals()
            self.parsed_data["time"] = ProfileService.profile_booking_time(
                teacher_data.free
            )

            return self.parsed_data
        else:
            return None

    def _get_teacher(self) -> Teacher:
        """
        Get teacher by id
        :return: dict with teahcer
        """
        return Teacher.query.filter(Teacher.id == self.id).first()

    @staticmethod
    def profile_booking_time(booking_data: dict) -> dict:
        """
        Filter available time
        :param booking_data: dict

        :return: profiled booking time
        """
        filtered_day: dict = defaultdict(list)
        for day in booking_data:
            for time, free in booking_data[day].items():
                if free:
                    filtered_day[day].append(time)

        return filtered_day
