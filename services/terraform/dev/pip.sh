#!/bin/bash
set -e
rm -rf ../../terraform/source
mkdir ../../terraform/source
pip3 install -r ../../requirements/dev.txt -t $1 --upgrade
rsync -arv --rsync-path=../../ --exclude=node_modules --exclude=terraform --exclude=requirements ../../ $1