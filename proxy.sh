#!/bin/bash
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.386
mv cloud_sql_proxy.linux.386 cloud_sql_proxy
chmod +x cloud_sql_proxy
./cloud_sql_proxy -instances=bgn-hack22lon-6501:europe-west2:yougle-server=tcp:3306 -credential_file=config.json
