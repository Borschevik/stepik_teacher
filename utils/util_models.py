"""
  Utils for models
"""
import json
import os
from functools import lru_cache

from config.config import ROOT_DIR
from database.models import User


@lru_cache()
def get_goals() -> dict:
    """
    Get goals
    :return: dict with goals
    """
    seeds_dir = os.path.join(ROOT_DIR, "fixtures")
    filename = os.path.join(seeds_dir, "goals.json")
    with open(filename, "r", encoding="utf8") as file:
        return {k: v[0] for k, v in json.load(file).items()}


def make_user(params):
    """
    Create model
    """
    name: str = params.get("name")
    phone: str = params.get("phone")
    user = User.query.filter(User.name == name, User.phone == phone).first()
    if not user:
        params = dict(name=name, phone=phone)
        user = User(**params)
    return user
