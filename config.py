__author__ = 'franciscui'
#coding=utf-8
DBHOST="127.0.0.1"
DBPORT=3306
DBUSER=""
DBPASSWD=""
DBNAME=""


web_log_paths = [{'api.example.com': '/data/log/nginx/api.example.com/access/access.log'},
           {'www.example.com': '/data/log/nginx/www.example.com/access/access.log'},
           ]

nginx_pid = "/var/run/nginx.pid"