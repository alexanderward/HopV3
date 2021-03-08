import boto3
import dynamodbgeo
import uuid

# Import the AWS sdk and set up your DynamoDB connection
from services.aws_toggle import AWS

dynamodb = AWS.client('dynamodb', region_name='us-east-1')

# Create an instance of GeoDataManagerConfiguration for each geospatial table you wish to interact with
config = dynamodbgeo.GeoDataManagerConfiguration(dynamodb, "places-geo-table")

# Initiate a manager to query and write to the table using this config object
geoDataManager = dynamodbgeo.GeoDataManager(config)

# Pick a hashKeyLength appropriate to your usage
config.hashKeyLength = 3

# Use GeoTableUtil to help construct a CreateTableInput.
table_util = dynamodbgeo.GeoTableUtil(config)
create_table_input=table_util.getCreateTableRequest()

#tweaking the base table parameters as a dict
create_table_input["ProvisionedThroughput"]['ReadCapacityUnits']=5

# Use GeoTableUtil to create the table
table_util.create_table(create_table_input)
# PutItemInput = {
#         'Item': {
#             'Country': {'S': "Tunisia"},
#             'Capital': {'S': "Tunis"},
#             'year': {'S': '2020'}
#         },
#         'ConditionExpression': "attribute_not_exists(hashKey)" # ... Anything else to pass through to `putItem`, eg ConditionExpression
#
# }
# import ipdb; ipdb.set_trace()
# geoDataManager.put_Point(dynamodbgeo.PutPointInput(
#         dynamodbgeo.GeoPoint(36.879163, 10.243120), # latitude then latitude longitude
#          str( uuid.uuid4()), # Use this to ensure uniqueness of the hash/range pairs.
#          PutItemInput # pass the dict here
#         ))
# QueryRadiusInput={
#         "FilterExpression": "Country = :val1",
#         "ExpressionAttributeValues": {
#             ":val1": {"S": "Italy"},
#         }
#     }

bb = geoDataManager.queryRadius(
    dynamodbgeo.QueryRadiusRequest(
        dynamodbgeo.GeoPoint(36.879131, 10.243057), # center point
        95, {}, sort = True))
import ipdb; ipdb.set_trace()