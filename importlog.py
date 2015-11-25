#coding=utf-8
__author__ = 'franciscui'

from weblog_etl.nginxetl import Nginxetl
from iplookup.ipinfooperate import IpinfoOperater
from db.Dbconnecter import Dbconnecter
from weblog_cut.nginx_cut import Nginxcut
from config import web_log_paths
import os
from config import nginx_pid

#logfile = open("testapi.uhouzz.com.access.log")

etl = Nginxetl()
ipinfo = IpinfoOperater()


sql = "INSERT INTO web_log.nginx_log VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
for web_log_path in web_log_paths:
    servername = web_log_path.keys()[0]
    fullpath = web_log_path[servername]
    filename = os.path.basename(fullpath)
    path = os.path.dirname(fullpath)
    cut = Nginxcut(path, path, nginx_pid, filename)
    newfilename = cut.cutlog()
    logfile = open(newfilename)
    dbconn = Dbconnecter()
    lastline = ''
    while True:
        line = logfile.readline()
        if not line:
            break
        value = etl.getetl(line)
        if not value:
            continue
        #print value[0]
        value.append(servername)
        #print value
        ipinfo.set_ipinfo(value[1])
        ret = dbconn.executeSql(sql, value)
        if ret == -1:
            print value
