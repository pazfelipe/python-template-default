from app.source.database.connection import Connection


class Product:

    def __init__(self):
        self.conn = Connection()
        self.collection = self.conn.connection().get_collection('products')

    def insertOne(self, data):
        """
        # Description
            - Gets a dict and saves it into the database

        # Parameters
            1. collection : str
              - Set the collection's name

            2. data : dict
              - Data to be saved

        # Returns
            - nil
        """
        self.collection.insert_one(data)

    def findAll(self, filter=None):
        products = self.collection.find({}, filter)
        return list(products)
