from rest_framework.response import Response

from apps.main.serializers.user_scan import UserScanSerializer
from apps.main.utils.response import CustomResponse
from apps.main.views.base import BaseGeoNoSql, GeoNoSQLListMixin


class UserScanViewset(BaseGeoNoSql,
                      GeoNoSQLListMixin):
    serializer_class = UserScanSerializer

    def filter_results(self, model):
        pass

    def list(self, request, *args, **kwargs):
        queryset = self.get_nodes(request, *args, **kwargs)
        if not queryset:
            lat, lon, radius = self.get_geo_data_from_url(request)

            self.serializer_class.Meta.model().create(lat, lon, data={})
            return CustomResponse.error("New scan started")
        serializer = self.serializer_class(queryset, many=True)
        return CustomResponse.success(serializer.data)
