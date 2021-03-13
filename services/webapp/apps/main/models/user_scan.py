from django.conf import settings
from pynamodb.attributes import TTLAttribute
from pynamodb.constants import STREAM_NEW_AND_OLD_IMAGE
from pynamodb.indexes import AllProjection

from apps.main.models.base import BaseModel, BaseGeoModel


class UserScan(BaseGeoModel, BaseModel):
    class Meta:
        table_name = f"user-search-table-{settings.STACK}"
        region = settings.AWS_REGION_NAME
        stream_view_type = STREAM_NEW_AND_OLD_IMAGE
        projection = AllProjection()

    ttl = TTLAttribute(default=settings.USER_SEARCH_AGE_OFF)
