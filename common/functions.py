#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
#=============================================================================
#
#     FileName: functions.py
#         Desc: 功能函数
#
#       Author: franciscui
#
#
#=============================================================================
'''

import re

def month_replace(str):
    month = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    rule = re.compile(r'[^a-zA-z]')
    str_en = rule.sub("", str)
    rule2 = re.compile(str_en)
    str_num = rule2.sub(month[str_en], str)
    return str_num


def trasferdate(date):
    date = month_replace(date)
    if(len(date) <> 19 ):
        return None
    day = date[0:2]
    month = date[3:5]
    year = date[6:10]
    time = date[11:19]
    date = year + '-' + month + "-" + day + " " + time
    return date