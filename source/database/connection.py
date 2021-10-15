from pymongo import MongoClient
from dotenv import dotenv_values

env = dotenv_values('.env')


class Connection:
    def __init__(self):
        self.URL_CONNECTION = env['DB_URL']
        self.DB = env['DB_NAME']

        print(self.URL_CONNECTION)

    def connection(self):
        client = MongoClient(self.URL_CONNECTION)
        database = client[self.DB]
        return database

    def insertOne(self, collection, data):
        """
        ## Description
            - Gets a dict and saves it into the database

        #### Parameters
            1. collection : str
              - Set the collection's name

            2. data : dict
              - Data to be saved

        #### Returns
            - nil
        """
        col = self.connection()[collection]
        col.insert_one(data)
