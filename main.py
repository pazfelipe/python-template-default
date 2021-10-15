import requests
from source.database.connection import Connection
from source.libs.redis import Redis

connect = Connection()
redis = Redis()

r = requests.get('https://reqres.in/api/users')
data = r.json()

userId = data['data'][1]['id']

redis.insert(userId, data['data'][1])

for user in data['data']:
    connect.insertOne('products', user)
    print(f'\nUser {user["id"]} has been successful inserted')
