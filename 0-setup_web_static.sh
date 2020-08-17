#!/usr/bin/env bash
# Sets up folder sturcture for remote server

CONTENT="location /hbnb_static {
    alias /data/web_static/current/;
    index.html;
}"
FILE="/etc/nginx/sites-available/default"
apt -y update
apt -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "<h1>Holberton Test</h1>" > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/current /data/web_static/releases/test/
chown -R ubuntu:ubuntu /data/
sed -i '/"root /var/www/html;"/ a\"$CONTENT"/' $FILE
service nginx restart
