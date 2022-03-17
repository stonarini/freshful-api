import json
import click
from flask import g
from flask.cli import with_appcontext
from pymongo import MongoClient
from pymongo.errors import ConfigurationError
from .settings import USER, PASSWORD, DB_URI


def get_db(name):
    if "db" not in g:
        URI = f"mongodb+srv://{USER}:{PASSWORD}@{DB_URI}/{name}?retryWrites=true&w=majority"

        try:
            client = MongoClient(URI)
        except ConfigurationError:
            print("Connection failed")
        else:
            g.connection = client
            g.db = client.get_default_database()

    return g.db


def close_db(e=None):
    g.pop("db", None)
    connection = g.pop("connection", None)

    if connection is not None:
        connection.close()


def init_db(name):
    db = get_db(name)
    db.items.drop()
    with open("repository/test_db.json") as f:
        db.items.insert_many(json.load(f))


def drop_db(name):
    db = get_db(name)
    db.command("dropDatabase")


@click.command("init-db")
@click.option("--name", default="GildedRose", help="Name of the database")
@with_appcontext
def init_db_command(name):
    init_db(name)
    click.echo(f"Initialized the {name} database.")


@click.command("drop-db")
@click.option("--name", default="GildedRose", help="Name of the database")
@with_appcontext
def drop_db_command(name):
    drop_db(name)
    click.echo(f"Deleted the {name} database.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(drop_db_command)
