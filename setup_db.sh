#!/bin/bash

# first, create db user under our account
sudo su - postgres -c "createuser --createdb `whoami`"

echo "DON'T FORGET TO INSTALL THE NEW postgis 2.0 from some repo!"

createdb manafeast
sudo su - postgres -c "psql manafeast -c 'CREATE EXTENSION postgis;'"
