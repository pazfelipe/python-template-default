import redis
from dotenv import dotenv_values

env = dotenv_values('.env')


class Redis:
    def connection(self):
        client = redis.Redis(
            host=env['REDIS_HOST'],
            port=env['REDIS_PORT']
        )
        return client

    def insert(self, key, data):
        client = self.connection()
        client.set(key, str(data))
        client.expire(key, 10)
