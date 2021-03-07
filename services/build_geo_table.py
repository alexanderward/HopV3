import boto3
import dynamodbgeo
import uuid

# Import the AWS sdk and set up your DynamoDB connection
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# Create an instance of GeoDataManagerConfiguration for each geospatial table you wish to interact with
config = dynamodbgeo.GeoDataManagerConfiguration(dynamodb, 'geo_table_demo')

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