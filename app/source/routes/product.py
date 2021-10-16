from crypt import methods
from flask import Blueprint, request
from app.source.controllers.product import ProductController

product = Blueprint('products', __name__, url_prefix='/products')


@product.route('/', methods=['GET'])
def index():
    return ProductController()._findAll()


@product.route('/<id>', methods=['GET'])
def routeFindByFilter(id):
    return ProductController()._findById(id)


@product.route('/', methods=['POST'])
def routeInsertOne():
    return ProductController()._insertOne(request.json)
