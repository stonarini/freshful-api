from pymongo import MongoClient
from pymongo.errors import ConfigurationError
from .settings import URI


def get_db():

    try:
        client = MongoClient(URI)
    except ConfigurationError:
        print("Connection failed")
    else:
        database = client["bunyols-library"]
        collection = database["items"]
        return collection
