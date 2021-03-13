# HopV3

## Local Dev
1. Create virtual environment
    -  `pip install -r services/requirements/dev.txt`
    
2. Localstack
    -  `cd services`
    -  `docker-compose up`
    
3. Build Services
    - `cd services/terraform/dev`
    -  `terraform apply -auto-approve`
 
4. Webapp
    - `cd services/webapp`
    - `python manage.py --settings=service.settings.dev`  
    
5. Teardown
    - `terraform destroy -auto-approve`
   
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