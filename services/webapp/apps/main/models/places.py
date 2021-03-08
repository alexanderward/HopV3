from django.conf import settings
from pynamodb.attributes import UnicodeAttribute, JSONAttribute, NumberAttribute
from pynamodb.constants import STREAM_NEW_AND_OLD_IMAGE
from pynamodb.indexes import AllProjection

from apps.main.models.base import BaseModel, BaseGeoModel


class Place(BaseGeoModel, BaseModel):
    class Meta:
        table_name = "places-geo-table"
        region = settings.AWS_REGION_NAME
        stream_view_type = STREAM_NEW_AND_OLD_IMAGE
        projection = AllProjection()

    hashKey = NumberAttribute(hash_key=True)
    rangeKey = UnicodeAttribute(range_key=True)
    geohash = NumberAttribute()
    data = JSONAttribute(null=True)
