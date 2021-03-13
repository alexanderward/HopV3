import dynamodbgeo
import uuid

# Import the AWS sdk and set up your DynamoDB connection
from service.settings.connections.aws import AWS

dynamodb = AWS.client('dynamodb', localstack=False, region_name='us-east-1')

# Create an instance of GeoDataManagerConfiguration for each geospatial table you wish to interact with
config = dynamodbgeo.GeoDataManagerConfiguration(dynamodb, "places-table-dev")

# Initiate a manager to query and write to the table using this config object
geoDataManager = dynamodbgeo.GeoDataManager(config)

# Pick a hashKeyLength appropriate to your usage
config.hashKeyLength = 3

# Use GeoTableUtil to help construct a CreateTableInput.
table_util = dynamodbgeo.GeoTableUtil(config)
create_table_input=table_util.getCreateTableRequest()

#tweaking the base table parameters as a dict
create_table_input["ProvisionedThroughput"]['ReadCapacityUnits']=5
# TODO - Find a way to build this table via serverless so we can add record age off capabilities

def dict_to_item(raw):
    if type(raw) is dict:
        resp = {}
        for k, v in raw.items():
            if type(v) is str:
                resp[k] = {
                    'S': v
                }
            elif type(v) is int:
                resp[k] = {
                    'I': str(v)
                }
            elif type(v) is dict:
                resp[k] = {
                    'M': dict_to_item(v)
                }
            elif type(v) is list:
                resp[k] = []
                for i in v:
                    resp[k].append(dict_to_item(i))

        return resp
    elif type(raw) is str:
        return {
            'S': raw
        }
    elif type(raw) is int:
        return {
            'I': str(raw)
        }
# # Use GeoTableUtil to create the table
table_util.create_table(create_table_input)
PutItemInput = {
        'Item': {
            'nodeData': {'M': dict_to_item({"test": "asdf"})},
        },
        'ConditionExpression': "attribute_not_exists(hashKey)" # ... Anything else to pass through to `putItem`, eg ConditionExpression

}
# # import ipdb; ipdb.set_trace()
geoDataManager.put_Point(dynamodbgeo.PutPointInput(
        dynamodbgeo.GeoPoint(36.879163, 10.243120), # latitude then latitude longitude
         str( uuid.uuid4()), # Use this to ensure uniqueness of the hash/range pairs.
         PutItemInput # pass the dict here
        ))
QueryRadiusInput={
        "FilterExpression": "Country = :val1",
        "ExpressionAttributeValues": {
            ":val1": {"S": "Italy"},
        }
    }

# bb = geoDataManager.queryRadius(
#     dynamodbgeo.QueryRadiusRequest(
#         dynamodbgeo.GeoPoint(36.879131, 10.243057), # center point
#         95, {}, sort = True))
# import ipdb; ipdb.set_trace()