import json


class DB:
	with open('model/db.json') as json_file:
		stock = json.load(json_file)

	@classmethod
	def get_items(cls):
		return cls.stock

	@classmethod
	def get_item(cls, title):
		return [book for book in cls.stock if book["title"] == title]