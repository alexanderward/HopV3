from apps.main.serializers.places import PlacesSerializer
from apps.main.views.base import BaseNoSQL, NoSQLListMixin, BaseGeoNoSql, GeoNoSQLListMixin


class PlacesViewset(BaseGeoNoSql,
                    GeoNoSQLListMixin):

    serializer_class = PlacesSerializer

    def filter_results(self, model):
        pass





