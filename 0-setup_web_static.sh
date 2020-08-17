#!/usr/bin/env bash
# Sets up folder sturcture for remote server

FILE="/etc/nginx/sites-available/default"
apt -y update
apt -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "<h1>Holberton Test</h1>" > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/current /data/web_static/releases/test/
chown -R ubuntu:ubuntu /data/
sed -i "38a location /hbnb_static {\nalias /data/web_static/current/;\n}" $FILE
service nginx restart
