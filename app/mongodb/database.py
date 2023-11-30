from pymongo import MongoClient


class MongoDB:
    def __init__(self, database_url: str, database_name: str):
        self.client = MongoClient(database_url)
        self.db = self.client[database_name]


mongo_db = MongoDB("mongodb://localhost:27017/", "puntodb")
