terraform {
  backend "local" {}
}

provider "aws" {
  access_key                  = "test"
  region                      = "us-east-1"
  s3_force_path_style         = true
  secret_key                  = "test"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    cloudwatchlogs = "http://localstack:4566"
    cloudwatchevents = "http://localstack:4566"
    cloudwatch = "http://localstack:4566"
    s3     = "http://localstack:4566"
    lambda = "http://localstack:4566"
    iam    = "http://localstack:4566"
    dynamodb = "http://localstack:4566"
    ssm = "http://localstack:4566"
    sqs = "http://localstack:4566"
  }
}

//resource "aws_dynamodb_table" "places-table" {
//  name           = local.dynamo-places-table
//  billing_mode   = "PROVISIONED"
//  read_capacity  = 5
//  write_capacity = 5
//  hash_key       = "hashKey"
//  range_key      = "rangeKey"
//  stream_enabled = true
//  stream_view_type = "NEW_AND_OLD_IMAGES"
//
//  attribute {
//    name = "hashKey"
//    type = "N"
//  }
//
//  attribute {
//    name = "rangeKey"
//    type = "S"
//  }
//
//  attribute {
//    name = "geohash"
//    type = "N"
//  }
//
//  ttl {
//    attribute_name = "TimeToExist"
//    enabled        = false
//  }
//
//  local_secondary_index {
//    name = "geohash-index"
//    projection_type = "ALL"
//    range_key = "geohash"
//  }
//}
//
//resource "aws_dynamodb_table" "tfids-table" {
//  name           = local.dynamo-tfids-table
//  billing_mode   = "PROVISIONED"
//  read_capacity  = 5
//  write_capacity = 5
//  hash_key       = "hashKey"
//  range_key      = "timestamp"
//  stream_enabled = true
//  stream_view_type = "NEW_AND_OLD_IMAGES"
//
//  attribute {
//    name = "hashKey"
//    type = "N"
//  }
//
//  attribute {
//    name = "timestamp"
//    type = "N"
//  }
//
//  ttl {
//    attribute_name = "TimeToExist"
//    enabled        = false
//  }
////
////  local_secondary_index {
////    name = "geohash-index"
////    projection_type = "ALL"
////    range_key = "geohash"
////  }
//}
//
//resource "aws_dynamodb_table" "user-search-table" {
//  name           = local.dynamo-user-search-table
//  billing_mode   = "PROVISIONED"
//  read_capacity  = 5
//  write_capacity = 5
//  hash_key       = "hashKey"
//  range_key      = "rangeKey"
//  stream_enabled = true
//  stream_view_type = "NEW_AND_OLD_IMAGES"
//
//  attribute {
//    name = "hashKey"
//    type = "N"
//  }
//
//  attribute {
//    name = "rangeKey"
//    type = "S"
//  }
//
//  attribute {
//    name = "geohash"
//    type = "N"
//  }
//
//
//  ttl {
//    attribute_name = "ttl"
//    enabled        = true
//  }
//
//  local_secondary_index {
//    name = "geohash-index"
//    projection_type = "ALL"
//    range_key = "geohash"
//  }
//}

module "lambda" {
  source  = "nozaq/lambda-auto-package/aws"

  source_dir  = "../../terraform/source"
  output_path = "project.zip"

  build_triggers = {
    requirements = base64sha256(file("../../requirements/dev.txt"))
    execute      = base64sha256(file("pip.sh"))
  }
  build_command = "${path.module}/pip.sh ../../terraform/source"

  iam_role_name_prefix = "example-lambda-role"

  function_name = "example-lambda"
  handler       = "tasks.sample.lambda_handler"
  runtime       = "python3.7"

  environment = {
    variables = {
      DOCKERIZED="true"
      DJANGO_SECRET_KEY="mysecretpassword"
      DJANGO_SETTINGS_MODULE="service.settings.local"
      LOCALSTACK_HOST="localhost"
      LOCALSTACK_PORT=4566
      AWS_REGION="us-east-1"
      REDIS_HOST="localhost"
      REDIS_PORT=6379
      REDIS_PASS=""
      POSTGRES_HOST="localhost"
      POSTGRES_PORT=5432
      POSTGRES_USER="postgres"
      POSTGRES_PASS="mysecretpassword"
      POSTGRES_SCHEMA="postgres"
      SQS_USER_SEARCH="user-search-queue-dev"
    }
  }
}


resource "aws_sqs_queue" "user_search_queue" {
  name                      = "user-search-queue-${var.prefix}"
  delay_seconds             = 90
  max_message_size          = 2048
  message_retention_seconds = 86400
  receive_wait_time_seconds = 10
//  redrive_policy = jsonencode({
//    deadLetterTargetArn = aws_sqs_queue.dlq.arn
//    maxReceiveCount     = 4
//  })
}
//
//resource "aws_lambda_event_source_mapping" "user_search_lambda_stream" {
//  event_source_arn = aws_sqs_queue.user_search_queue.arn
//  function_name    = aws_lambda_function.example.arn
//}




//'NAME': 'multi_schema_db',
//            'USER': 'django_user',
//            'PASSWORD': 'secret',

//resource "aws_elasticache_cluster" "geo_redis" {
//  cluster_id = "geo-redis-${var.prefix}"
//  engine = "redis"
//  node_type = "cache.t3.micro"
//  num_cache_nodes      = 1
//  parameter_group_name = "default.redis3.2"
//  engine_version       = "3.2.10"
//  port                 = 6379
//}
//
//output "geo_redis_host" {
//  value = aws_elasticache_cluster.geo_redis.cache_nodes[0].address
//}

//resource "aws_lambda_event_source_mapping" "example" {
//  event_source_arn  = aws_dynamodb_table.places-geo.stream_arn
//  function_name     = aws_lambda_function.example.arn
//  starting_position = "LATEST"
//}

//resource "aws_lambda_event_source_mapping" "example" {
//  event_source_arn = aws_sqs_queue.sqs_queue_test.arn
//  function_name    = aws_lambda_function.example.arn
//}