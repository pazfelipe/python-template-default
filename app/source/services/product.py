import requests
from flask import jsonify

from app.source.utils.validator import Validator
from app.source.model.product import Product
from app.source.libs.redis import Redis


def save():
    model = Product()
    redis = Redis()

    r = requests.get('https://reqres.in/api/users')
    data = r.json()

    userId = data['data'][1]['id']

    redis.insert(userId, data['data'][1])

    for user in data['data']:
        model.insertOne(user)
        print(f'\nUser {user["id"]} has been successful inserted')

    return data


def findAll():

    model = Product()
    return jsonify(model.findAll({'_id': False}))


def findById(id):

    model = Product()
    product = model.findById({'id': int(id)}, {'_id': False})

    if not product:
        return 'Nenhum produto encontrado', 404
    return product


def insertOne(data):
    validator = Validator()
    validator.isRequired(data['name'], 'Campo name é obrigatório')
    validator.isEmail(data['email'], 'Informe um e-mail válido')

    if not validator.isValid():
        return jsonify(validator.errors()), 400

    model = Product()
    model.insertOne(data)

    return 'Produto cadastrado', 201
