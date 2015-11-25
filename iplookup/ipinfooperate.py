#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
#=============================================================================
#
#     FileName: ipinfooperate.py
#         Desc: 将ip信息存储到数据库
#
#       Author: franciscui
#
#
#=============================================================================
'''

from ipinfoapi import IpinfoApi
from db.Dbconnecter import Dbconnecter

class IpinfoOperater:
    __taobaoapi = None
    __dbconn = None
    def __init__(self):
        self.__taobaoapi = IpinfoApi()
        self.__dbconn = Dbconnecter()

    def __get_from_taobao(self, ip):
        retry = 3
        value = []
        while retry > 0:
            result = self.__taobaoapi.getipinfo(ip)
            if ('code' in result.keys()) and (result['code'] == 0):
                value.append(result['data']['ip'])
                value.append(result['data']['country'])
                value.append(result['data']['region'])
                value.append(result['data']['city'])
                value.append(result['data']['isp'])
                break
            retry = retry - 1
        return value

    def __check_ip_exist(self, ip):
        sql = 'select count(*) from ipinfo where ipaddr = ' + '\'' + ip.strip() + '\';'
        result = self.__dbconn.selectSql(sql)
        return result[0]

    def set_ipinfo(self, ip):
        if ip is None or ip == '':
            return -1
        if self.__check_ip_exist(ip) < 1:
            sql = "INSERT INTO ipinfo VALUES(%s,%s,%s,%s,%s)"
            value = self.__get_from_taobao(ip)
            #print value
            if len(value):
                retult = self.__dbconn.executeSql(sql,value)
                return retult
            print ip
            return -2

#a = IpinfoOperater()
#a.set_ipinfo('202.113.244.1')
