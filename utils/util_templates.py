from functools import lru_cache

from config.config import DAY_MAP, SMILES, TIME_MAP
from service.json_service import JsonService


@lru_cache()
def get_hour(string_time: str) -> int:
    """
    Filter to get hour
    """
    return int(string_time.split(":")[0])


@lru_cache()
def get_ru_week(eng_name: str) -> str:
    """
    Filter to week name in ru
    """
    return DAY_MAP[eng_name]


@lru_cache()
def get_str_time(int_hour: int) -> str:
    """
    Filter to get string time by int time
    """
    return TIME_MAP[int_hour]


@lru_cache()
def get_goal(goal_id: str) -> str:
    """
    Get goal full name
    """
    return JsonService("goals").all()[goal_id]


@lru_cache()
def lower_byindex(string: str, index: int) -> str:
    """
    Lower string by index
    :param string:
    :return: lowered by index string
    """
    return "".join([s.lower() if i == index else s for i, s in enumerate(string)])


@lru_cache()
def get_smiles(relocate: str) -> str:
    """
    :param relocate: str

    :return: string with smiles
    """
    return SMILES[relocate]


@lru_cache()
def get_nav_item(path: str, location: str) -> str:
    """
    :param relocate: str

    :return: string with smiles
    """
    return "nav-item active" if location in path else "nav-item"
