from flask import Flask, g
from flask_restful import Api
from resources import Home, Item, Books


app = Flask(__name__)

api = Api(app, catch_all_404s=True)

api.add_resource(Home, "/")
api.add_resource(Item, "/item/<name>")
api.add_resource(Books, "/books")


if __name__ == "__main__":
    app.run()
