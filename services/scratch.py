import json
import os
import time
import uuid

from service.settings.connections.elasticache import Redis, SmartCache

os.environ['REDIS_HOST'] = "localhost"
os.environ['REDIS_PORT'] = "6379"
os.environ['REDIS_PASS'] = ""

cache = SmartCache(connection=Redis())
expire = 500
lon = 30.52439985197
lat = 50.56539003041
# cache.add_user_search(lon=30.52439985197,
#                       lat=50.56539003041,
#                       expire_in=expire)
exists = cache.check_for_recent_search(lon=lon, lat=lat, radius=1)
print(exists)
# cache.add_geo_with_expiration("user-search", 30.52439985197, 50.56539003041,
#                               item_key=search_id,
#                               expire_in=expire)
# cache.remove_expired_geo("user-search")
# cache.get_unexpired_geo("user-search")
# items = cache.connection.georadius("user-search", 30.52439985197, 50.56539003041, 1, unit="km", withcoord=True)
# print(items)
cache.connection.set("place", json.dumps({"asf": "test"}))