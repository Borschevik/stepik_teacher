"""
   Cli for custom commands for database
"""
import json
import os

import click
from flask.cli import with_appcontext
from flask_alembic.cli.click import cli as db_cli
from flask_migrate import cli
from sqlalchemy_utils import create_database, database_exists, drop_database

from config.config import ROOT_DIR, SQLALCHEMY_DATABASE_URI
from config.extenstions import db
from database.models import Goal, Teacher


@click.group()
@with_appcontext
def db_tasks():
    """Perform database relates commands"""
    pass


@db_cli.command()
@click.option(
    "--drop-db", is_flag=True, expose_value=True, prompt="Drop DB tables?",
)
@with_appcontext
@click.pass_context
def init_db(ctx, drop_db: bool):
    """Set the database up from scratch."""
    click.echo("Init.")
    if not database_exists(SQLALCHEMY_DATABASE_URI):
        ctx.invoke(create)
    else:
        ctx.invoke(drop, ctx=ctx, drop_db=drop_db)
    click.echo("Migrate.")
    ctx.invoke(cli.upgrade)
    click.echo("Done")
    ctx.invoke(seed)
    click.echo("Done")


@db_cli.command()
@with_appcontext
def create():
    """Create the database."""
    if not database_exists(SQLALCHEMY_DATABASE_URI):
        click.echo("Creating")
        create_database(SQLALCHEMY_DATABASE_URI)
        click.echo("Done")
    else:
        click.echo("Already exists.")


@db_cli.command()
@click.option("--drop-db/--no-drop-db", expose_value=True, prompt="Drop DB?")
@with_appcontext
def drop(ctx, drop_db: bool):
    """Drop database."""
    if drop_db:
        if database_exists(SQLALCHEMY_DATABASE_URI):
            click.echo("Dropping database.")
            drop_database(SQLALCHEMY_DATABASE_URI)
            click.echo("Done dropping database.")
        ctx.invoke(create)


@click.command("seed")
@with_appcontext
def seed():
    """Seed databse from json files"""
    model: db.Model
    click.echo("Seeding")
    seeds_dir = os.path.join(ROOT_DIR, "fixtures")
    filename = os.path.join(seeds_dir, "goals.json")
    with open(filename, "r", encoding="utf-8") as file:
        goals: dict = json.loads(file.read())
    filename = os.path.join(seeds_dir, "teachers.json")
    with open(filename, "r", encoding="utf-8") as file:
        click.echo("Adding seeds to Teacher")
        for fields in json.load(file):
            teacher = Teacher()
            teacher.id = fields.get("id")
            teacher.name = fields.get("name")
            teacher.about = fields.get("about")
            teacher.rating = fields.get("rating")
            teacher.price = fields.get("price")
            teacher.picture = fields.get("picture")
            teacher.free = fields.get("free")
            for goal in fields.get("goals"):
                g = Goal(**dict(eng=goal, ru=goals[goal][0], smile=goals[goal][1]))
                teacher.goals.append(g)
            teacher.save()
            click.echo(f"Added seed entry with id {teacher.id} to Teachers.")

    click.echo("Done seeding.")


db_tasks.add_command(init_db)
db_tasks.add_command(seed)
db_tasks.add_command(drop)
db_tasks.add_command(create)
