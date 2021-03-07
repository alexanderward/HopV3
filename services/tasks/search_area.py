import os
from sys import path
import django
from multiprocessing.pool import ThreadPool
path.append('../../..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings.local")
django.setup()


def lambda_handler(event=None, context=None):
    from django.conf import settings
    from apps.places.tasks.utils.google.maps import Maps
    from apps.places.tasks import batch_records_and_upload, start_next_step
    latitude = event['lat']
    longitude = event['long']
    search_id = event['search_id']
    try:
        tfids = Maps(debug=not settings.DEPLOYED).search(latitude, longitude, settings.MAP_KEYWORDS, pool_class=ThreadPool)
        filenames = batch_records_and_upload(records=tfids, batch_size=settings.DATA_PIPELINE_BATCH_SIZE,
                                             s3_bucket_name=settings.DATA_PIPELINE_S3_BUCKET,
                                             prefix='tfids',
                                             latitude=latitude, longitude=longitude, search_id=search_id)
        if settings.DEPLOYED:
            for filename in filenames:
                start_next_step(filename=filename,
                                function_name=f'hop-tasks-get-details-{settings.SETTINGS_MODULE.split(".")[-1]}')
        else:
            from apps.places.tasks.get_details import lambda_handler
            from multiprocessing.pool import Pool
            with Pool(processes=settings.DATA_PIPELINE_WORKERS) as pool:
                pool.starmap(lambda_handler, [[dict(filename=x)] for x in filenames])
    except Exception as e:
        from apps.places.models.places import PlaceSearch
        search = PlaceSearch.objects.get(id=search_id)
        search.errored = True
        search.save()
        raise e


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