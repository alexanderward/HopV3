import json
import os

import redis

from service.settings.connections.aws import AWS


class Redis:

    def __new__(cls, *args, **kwargs):
        cls.connection = redis.Redis(
            host=os.environ['REDIS_HOST'],
            port=os.environ['REDIS_PORT'],
            password=os.environ['REDIS_PASS']
        )
        cls.connection.ping()
        return cls.connection


class SmartCache:
    TFID = "tfid:{0}"

    def __init__(self, connection):
        self.connection = connection

    def add_with_expiration(self, key, value=None, expire_in=5):
        self.connection.set(key, value if value else 1)
        self.connection.expire(key, expire_in)


if __name__ == '__main__':
    bb = Redis(stack="dev")
    bb.set(SmartCache.TFID.format("2342342342343"), 1)
    bb.expire('a', 5)
