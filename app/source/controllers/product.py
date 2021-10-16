from app.source.services.product import save, findAll, findById, insertOne


class ProductController:
    def _save(self, data):
        return save(data)

    def _findAll(self):
        return findAll()

    def _findById(self, id):
        return findById(id)

    def _insertOne(self, data):
        return insertOne(data)
