"""
   Util for forms
"""


def create_choices(choices: dict) -> list:
    """
    Create choices
    :param coices:

    :return: dict with choice for radio buttons
    """
    return [(key, value) for key, value in choices.items()]
