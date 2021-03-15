import json
import os
import time

import redis


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
    USER_SEARCH = "user-search"

    def __init__(self, connection):
        self.connection = connection

    def add_with_expiration(self, key, value=None, expire_in=5):
        self.connection.set(key, value if value else 1)
        self.connection.expire(key, expire_in)

    def add_geo_with_expiration(self, set_key, lon, lat, item_key, expire_in=5, value=None):
        """
        GEOADD report-geo-set 30.52439985197 50.56539003041 john
        ZADD geo-timeout 1452600528 john //1452600528 is unix time stamp current + X hours
        """
        if value is None:
            value = {}
        assert isinstance(value, dict)
        self.connection.geoadd(set_key, lon, lat, item_key)
        self.connection.zadd(f"{set_key}-timeout", {item_key: int(time.time()) + expire_in})
        self.connection.set("place", json.dumps(value))

    def remove_expired_geo(self, set_key):
        """
        local currentTime = redis.call('TIME');
        local list = redis.call('ZRANGEBYSCORE', 'geo-timeout', 0, currentTime[0]);
        for i, name in ipairs(list) do
            redis.call('ZREM', 'geo-timeout', name);
        """
        now = self.connection.time()[0]
        expired = self.connection.zrangebyscore(f"{set_key}-timeout", 0, now)
        if expired:
            self.connection.zrem(f"{set_key}-timeout", *expired)
            self.connection.zrem(f"{set_key}", *expired)

    def get_unexpired_geo(self, set_key, lon, lat, radius, max_boundary=31536000):
        # get keys that are within a year of expiration, but not expired
        # now = self.connection.time()[0]
        now = int(time.time())
        unexpired_expired = set(self.connection.zrangebyscore(f"{set_key}-timeout", now, now + max_boundary))
        geo_nodes = set(self.connection.georadius(set_key, lon, lat, radius, unit="km"))
        return geo_nodes.intersection(unexpired_expired)

    def add_user_search(self, lon, lat, expire_in=5, set_key=USER_SEARCH):
        import uuid
        search_id = uuid.uuid4().hex
        self.add_geo_with_expiration(set_key, lon, lat,
                                     item_key=search_id,
                                     expire_in=expire_in)

    def check_for_recent_search(self, lon, lat, radius):
        return len(self.get_unexpired_geo(self.USER_SEARCH, lon, lat, radius)) > 0


if __name__ == '__main__':
    bb = Redis(stack="dev")
    bb.set(SmartCache.TFID.format("2342342342343"), 1)
    bb.expire('a', 5)
