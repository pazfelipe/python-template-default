from pymongo import MongoClient
from dotenv import dotenv_values

env = dotenv_values('.env')


class Connection:
    def __init__(self):
        self.URL_CONNECTION = env['DB_URL']
        self.DB = env['DB_NAME']

    def connection(self):
        client = MongoClient(self.URL_CONNECTION)
        database = client[self.DB]
        return database
