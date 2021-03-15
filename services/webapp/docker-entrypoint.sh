#!/bin/bash
set -e

echo "Terraforming"
cd terraform/dev
terraform init
terraform get
terraform apply -auto-approve

cd ../../webapp

echo "Make migrations"
python manage.py makemigrations --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate --noinput


# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000