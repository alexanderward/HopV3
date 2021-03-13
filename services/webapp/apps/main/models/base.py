import uuid

import dynamodbgeo
from django.conf import settings
from pynamodb.attributes import MapAttribute, NumberAttribute, UnicodeAttribute, JSONAttribute
from pynamodb.models import Model


def dict_to_dynamodb(raw):
    if type(raw) is dict:
        resp = {}
        for k, v in raw.items():
            if type(v) is str:
                resp[k] = {
                    'S': v
                }
            elif type(v) is int:
                resp[k] = {
                    'N': str(v)
                }
            elif type(v) is dict:
                resp[k] = {
                    'M': dict_to_dynamodb(v)
                }
            elif type(v) is list:
                resp[k] = []
                for i in v:
                    resp[k].append(dict_to_dynamodb(i))

        return resp
    elif type(raw) is str:
        return {
            'S': raw
        }
    elif type(raw) is int:
        return {
            'N': str(raw)
        }
    elif type(raw) is list:
        return {
            'L': [dict_to_dynamodb(x) for x in raw]
        }


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
    hashKey = NumberAttribute(hash_key=True)
    rangeKey = UnicodeAttribute(range_key=True)
    geoJson = UnicodeAttribute()
    geohash = NumberAttribute()
    nodeData = JSONAttribute(null=True)

    def __init__(self, **attributes):
        super().__init__(**attributes)
        # Create an instance of GeoDataManagerConfiguration for each geospatial table you wish to interact with
        config = dynamodbgeo.GeoDataManagerConfiguration(settings.DYNAMODB, self.Meta.table_name)
        # Initiate a manager to query and write to the table using this config object
        config.hashKeyLength = 3
        self.geoDataManager = dynamodbgeo.GeoDataManager(config)

    def create(self, lat, lon, data, range_key=None):
        # assert isinstance(data, dict)
        if isinstance(lat, str):
            lat = float(lat)
        if isinstance(lon, str):
            lon = float(lon)

        if isinstance(data, list):
            node_data = dict_to_dynamodb(data)
        else:
            node_data = {"M": dict_to_dynamodb(data)}

        put_input = {
            'Item': {
                'nodeData': node_data,
            },
            # 'ConditionExpression': "attribute_not_exists(hashKey)"
            # ... Anything else to pass through to `putItem`, eg ConditionExpression
        }
        ttl = self._ttl_attribute()
        if ttl:
            put_input['Item']['ttl'] = {"N": str(int(ttl.serialize(getattr(self, ttl.attr_name))))}
        if not range_key:
            range_key = str(uuid.uuid4())

        results = self.geoDataManager.put_Point(dynamodbgeo.PutPointInput(
            dynamodbgeo.GeoPoint(lat, lon),  # latitude then latitude longitude
            range_key,  # Use this to ensure uniqueness of the hash/range pairs.
            put_input  # pass the dict here
        ))
        if results == 'Error':
            raise Exception("Dev Error - Create")
        return results

    def update(self, range_key, lat, lon, data):
        put_input = {  # Dont provide TableName and Key, they are filled in for you
            "UpdateExpression": "set nodeData = :nodeData",
            "ConditionExpression": "rangeKey = :range_key",
            "ExpressionAttributeValues": {
                ":range_key": {"S": range_key},
                ":nodeData": {"M": dict_to_dynamodb(data)}
            },
            "ReturnValues": "ALL_NEW"
        }
        results = self.geoDataManager.update_Point(dynamodbgeo.UpdateItemInput(
            dynamodbgeo.GeoPoint(lat, lon),  # latitude then latitude longitude
            range_key,  # Use this to ensure uniqueness of the hash/range pairs.
            put_input  # pass the dict that contain the remaining parameters here
        ))
        if results == 'Error':
            raise Exception("Dev Error - Update")
        return results
