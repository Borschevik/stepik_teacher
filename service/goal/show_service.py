"""
   Filter teachers by goal
"""
from database.models import Goal, Teacher


class ShowService:
    """
    Get tutors by goals
    """

    def __init__(
        self, goal: str,
    ):
        """
        Init service to get instructors by goal
        """
        self.goal = goal

    def get(self) -> list:
        """
        Return sorted list of teachers
        """

        entries: list = Teacher.query.join(Goal, Teacher.goals).filter(
            Goal.eng == self.goal
        ).order_by(Teacher.rating.desc()).all()

        return [entry.__dict__ for entry in entries]
