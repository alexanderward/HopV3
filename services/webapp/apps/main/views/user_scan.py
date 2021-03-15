from django.conf import settings

from apps.main.utils.response import CustomResponse
from apps.main.views.base import BaseGeoRedis


class UserScanViewset(BaseGeoRedis):

    def list(self, request, *args, **kwargs):
        lat, lon, radius = self.get_geo_data_from_url(request)
        found = self.SMART_CACHE.check_for_recent_search(lat=lat,
                                                         lon=lon,
                                                         radius=settings.MAX_SEARCH_RADIUS / 1000)
        if not found:
            # todo - add to SQS?
            self.SMART_CACHE.add_user_search(lon=lon,
                                             lat=lat,
                                             expire_in=settings.USER_SEARCH_AGE_OFF_SECONDS)
            return CustomResponse.error("New scan started")
        return CustomResponse.success({"message": "Area already searched recently."})
