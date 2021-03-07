import os
import sys
from multiprocessing.pool import ThreadPool
import django

from apps.places.tasks import delete_batch_record

sys.path.append('../../..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings.local")
django.setup()


def lambda_handler(event=None, context=None):
    from django.conf import settings
    from apps.places.tasks.utils.google.maps import Maps
    from apps.places.tasks import download_batch_records
    from apps.places.tasks import batch_records_and_upload, start_next_step

    data = download_batch_records(filename=event['filename'], s3_bucket_name=settings.DATA_PIPELINE_S3_BUCKET)
    longitude = data['longitude']
    latitude = data['latitude']
    tfids = data['data']
    search_id = data['search_id']

    try:
        places = Maps(debug=not settings.DEPLOYED).get_place_details_pool(latitude, longitude, tfids,
                                                                          pool_class=ThreadPool)

        filenames = batch_records_and_upload(records=places, batch_size=settings.DATA_PIPELINE_BATCH_SIZE,
                                             s3_bucket_name=settings.DATA_PIPELINE_S3_BUCKET,
                                             prefix='details',
                                             latitude=latitude, longitude=longitude, search_id=search_id)
        if settings.DEPLOYED:
            for filename in filenames:
                start_next_step(filename=filename,
                                function_name=f'hop-tasks-insert-records-{settings.SETTINGS_MODULE.split(".")[-1]}')
        else:
            from apps.places.tasks.insert_records import lambda_handler
            with ThreadPool(processes=settings.DATA_PIPELINE_WORKERS) as pool:
                pool.starmap(lambda_handler, [[dict(filename=x)] for x in filenames])

        delete_batch_record(filename=event['filename'], s3_bucket_name=settings.DATA_PIPELINE_S3_BUCKET)
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

    lambda_handler(event={'filename': '0382c5f6675e45ceab53fe0156cf2568.json'})
