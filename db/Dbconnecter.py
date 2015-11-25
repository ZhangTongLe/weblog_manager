__author__ = 'franciscui'
#coding=utf-8

import MySQLdb
from config import *

class Dbconnecter:
    __host = ""
    __port = ""
    __dbuser = ""
    __dbpasswd = ""
    __dbname = ""
    __charset = ""
    __use_unicode= None

    def __init__(self, host=DBHOST, port=DBPORT, user=DBUSER, passwd=DBPASSWD, dbname=DBNAME,charset='utf8', use_unicode=True):
        self.__host = host
        self.__dbname = dbname
        self.__port = port
        self.__dbuser = user
        self.__dbpasswd = passwd
        self._charset = charset
        self.__use_unicode = use_unicode
        self.__conn = self.__conn()
        self.__conn.set_character_set('utf8')
        self.__cur = self.__conn.cursor()
        self.__cur.execute('SET NAMES utf8;')
        self.__cur.execute('SET CHARACTER SET utf8;')
        self.__cur.execute('SET character_set_connection=utf8;')

    def __conn(self):
        return MySQLdb.connect(host=self.__host, user=self.__dbuser, passwd=self.__dbpasswd, port=self.__port, db=self.__dbname, use_unicode=self.__use_unicode, charset=self.__charset)

    def executeSql(self, sql, value=None):
        try:
            result = self.__cur.execute(sql, value)
            self.__conn.commit()
            return result
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            return -1

    def selectSql(self, sql):
        try:
            result = self.__cur.execute(sql)
            records = self.__cur.fetchone()
            return records
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            return -1


    def __del__(self):
        self.__conn.commit()
        self.__cur.close()
        self.__conn.close()
