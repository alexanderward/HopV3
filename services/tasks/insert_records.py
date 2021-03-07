import os
import sys

import django

sys.path.append('../../..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings.local")
django.setup()


def lambda_handler(event=None, context=None):
    from django.conf import settings
    from apps.places.tasks.utils.google.maps import Maps
    from apps.places.tasks import download_batch_records
    from apps.places.tasks import delete_batch_record

    data = download_batch_records(filename=event['filename'], s3_bucket_name=settings.DATA_PIPELINE_S3_BUCKET)
    longitude = data['longitude']
    latitude = data['latitude']
    search_id = data['search_id']
    places = data['data']

    try:
        Maps(debug=not settings.DEPLOYED).bulk_insert(places, latitude, longitude, search_id)
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

    lambda_handler(event={'filename': '99a893a0dcba4df49249ac5bebfa26ca.json'})
