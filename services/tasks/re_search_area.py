import os
import sys
import django

sys.path.append('../../..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings.dev")
django.setup()


def lambda_handler(event=None, context=None):
    from django.conf import settings
    from apps.places.tasks.utils.google.maps import Maps
    data = {}  # todo json load the s3 file, will contain lat, long, tfids
    longitude = data['longitude']
    latitude = data['latitude']
    tfids = data['tfids']
    maps = Maps(debug=not settings.DEPLOYED)

    places = maps.get_place_details_pool(latitude, longitude, tfids)
    # todo - upload places
    import ipdb;
    ipdb.set_trace()
    pass


if __name__ == "__main__":
    lat = '29.424349'  # San Antonio
    long = '-98.491142'
    #
    # long = '-77.050636'  # DC
    # lat = '38.889248'

    lambda_handler(event={'s3_file': ''})
