# HopV3

## Local Dev
1. Start
    -  `cd services`
    -  `docker-compose up`
2. Debugging
    - `docker attach services_webapp_1`
    - use ipdb as you normally would
   
## Flow

### New Area workflow
- User -> checks area -> endpoint says no records exist:
    *  Add entry into user search table
    * Starts lambda to search area
        * Lambda gets resulting TFIDS and stores in Redis via the Redis geo module.  Add age off of 2 hours +

### Existing Area Workflow
- User -> checks area -> endpoints comes back w/ records.  Done

### Refresh Area Workflow
- Cloudwatch event triggers lambda to search redis for tfids.
    - Add each tfid returned to SQS for detail search


### Detail Search
- Do the google search and store in result DynamoDB table

- GET - places
   - User -> search for places lambda -> get Redis Key of cached list from previous query
    - If exists, return cached value
    - If not exist,
        - Query Places table
            - If Places, Add tfids to Redis for future refresh, Add cached response for future places search lambda
            - If not places, return []
    

## Flow V2
- User -> checks area via Redis user-query: