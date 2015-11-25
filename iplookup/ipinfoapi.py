#!/usr/bin/python
#coding=utf-8

'''
#=============================================================================
#
#     FileName: ipinfoapi.py
#         Desc: 获取Ip相关信息的api
#
#       Author:francis
#
#      Created: 2014-4-5 
#      Version: 1.0.0
#      History:
#               1.0.0 | francis
#
#=============================================================================
'''

import copy
import json

from common.sns_network  import SNSNetwork

OPEN_HTTP_TRANSLATE_ERROR = 1801

class IpinfoApi(object):
    __api = None

    def __init__(self, iplist=('ip.taobao.com',)):
        super(IpinfoApi, self).__init__()
        self.__api = SNSNetwork(iplist)

    def call(self,  params, url_path='/service/getIpInfo.php', method='get', protocol='http'):
        '''
        调用接口，并将数据格式转化成json
        只需要传入pf, openid, openkey等参数即可，不需要传入sig
        format即使传xml也没有用，会被强制改为json
        '''
        cp_params = copy.deepcopy(params)
        cp_params.update(
            {
                #'username': self.__username
                'format': 'json'
            }
            )
        try:
            data = self.__api.open(method, url_path, cp_params, protocol)
        except Exception, e:
            msg = 'exception occur.msg[%s], traceback[%s]' % (str(e), __import__('traceback').format_exc())
            return {'ret':OPEN_HTTP_TRANSLATE_ERROR, 'msg':msg}
        else:
            #print data
            return json.loads(data)

    def getipinfo(self, ip):
        jdata = self.call({'ip': ip})
        return jdata


#a = IpinfoApi()
#print a.getipinfo('203.195.183.146')