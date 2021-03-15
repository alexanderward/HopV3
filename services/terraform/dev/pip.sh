#!/bin/bash
set -e

pip3 install -r ../../requirements/dev.txt -t $1 --upgrade
rsync -av ../.. ../../terraform/source --exclude ../../terraform --exclude ../../requirements --exclude ../../node_modules
