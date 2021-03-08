import dynamodbgeo
from django.conf import settings
from pynamodb.attributes import MapAttribute
from pynamodb.models import Model

from services.aws_toggle import AWS


class BaseModel(Model):
    def __init__(self, **attributes):
        super().__init__(**attributes)

    def __iter__(self):
        for name, attr in self.get_attributes().items():
            if isinstance(attr, MapAttribute):
                yield name, getattr(self, name).as_dict()
            else:
                yield name, attr.serialize(getattr(self, name))


class BaseGeoModel:
    def __init__(self, **attributes):
        super().__init__(**attributes)
        # Create an instance of GeoDataManagerConfiguration for each geospatial table you wish to interact with
        config = dynamodbgeo.GeoDataManagerConfiguration(settings.DYNAMODB, self.Meta.table_name)
        # Initiate a manager to query and write to the table using this config object
        config.hashKeyLength = 3
        self.geoDataManager = dynamodbgeo.GeoDataManager(config)

    def create(self):
        pass

