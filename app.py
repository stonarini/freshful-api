from flask import Flask
from flask_restful import Api
from resources import Home, Item, Items


def app_setup():
    app = Flask(__name__)

    api = Api(app, catch_all_404s=True)

    api.add_resource(Home, "/")
    api.add_resource(Item, "/items/<name>")
    api.add_resource(Items, "/items")

    return app


if __name__ == "__main__":
    app = app_setup()
    app.run()
