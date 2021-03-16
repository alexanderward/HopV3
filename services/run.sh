rm terraform/dev/.terraform.lock.hcl 2> /dev/null
rm terraform/dev/terraform.tfstate 2> /dev/null
rm terraform/dev/terraform.tfstate.backup 2> /dev/null
docker-compose up --remove-orphans