import requests
from flask import jsonify

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
