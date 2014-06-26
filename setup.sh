#!/bin/bash

sudo apt-get update
sudo apt-get -y install python-pip postgresql binutils libproj-dev gdal-bin postgresql-9.1-postgis postgresql-server-dev-9.1 python-dev

pip install -r requirements.txt

./setup_db.sh
