import json
import os
from resource import data

import click

from config.config import ROOT_DIR


@click.command()
def create_db():
    """
    Creates JSON databases
    """
    db_path: str

    for var in dir(data):
        if not var.startswith("_"):
            db_path = os.path.join(ROOT_DIR, "database", f"{var}.json")

            with open(db_path, "w", encoding="utf-8") as f:
                json.dump(getattr(data, var), f, ensure_ascii=False, indent=4)
