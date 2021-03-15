import os
from sys import path
import django
from multiprocessing.pool import ThreadPool
from core.google.config import MAP_KEYWORDS
from core.google.maps import Maps

path.append('../webapp')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings.local")
django.setup()
from service.settings.connections.elasticache import SmartCache


from service.settings.dev import REDIS
#
# # from apps.main.models.user_scan import UserScan

def lambda_handler(event=None, context=None):
    return True


if __name__ == "__main__":
    lat = '29.424349'  # San Antonio
    long = '-98.491142'
    #
    # long = '-77.050636'  # DC
    # lat = '38.889248'

    lambda_handler(event={'lat': lat, 'long': long})

    # San Antonio
    #  client = boto3.client('lambda');client.invoke(FunctionName=fn_name, InvocationType='Event', Payload=json.dumps({'lat': '29.424349', 'long': '-98.491142'}))

    # DC
    #  client = boto3.client('lambda');client.invoke(FunctionName=fn_name, InvocationType='Event', Payload=json.dumps({'lat': '38.889248', 'long': '-77.050636'}))

    # Corpus Christi
    #  client = boto3.client('lambda');client.invoke(FunctionName=fn_name, InvocationType='Event', Payload=json.dumps({'lat': '27.800583', 'long': '-97.396378'}))

    # Austin
    #  client = boto3.client('lambda');client.invoke(FunctionName=fn_name, InvocationType='Event', Payload=json.dumps({'lat': '30.266666', 'long': '-97.733330'}))
