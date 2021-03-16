import os
from sys import path
import django
from multiprocessing.pool import ThreadPool
path.append('webapp')
path.append('tasks')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings.local")
django.setup()
from core.google.config import MAP_KEYWORDS
from core.google.maps import Maps

from django.conf import settings
from service.settings.connections.elasticache import SmartCache

def lambda_handler(event=None, context=None):
    return settings.SMART_CACHE.connection.time()

