from flask import Flask
from flask_restful import Api
from repository.db import init_app
from resources import Home, Item, Items


def create_app():
    app = Flask(__name__)

    api = Api(app, catch_all_404s=True)

    api.add_resource(Home, "/")
    api.add_resource(Item, "/items/<name>")
    api.add_resource(Items, "/items")

    init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
