#!/usr/bin/env python
#coding:utf8
import re
from common.functions import trasferdate
import hashlib

class Nginxetl:
    #__logfile=open("testapi.uhouzz.com.access.log")
    #203.208.60.230
    __ipP = r"?P<ip>[\d.]*"
    __timeP = r"""?P<time>\[[^\[\]]*\]"""
    #"GET /EntpShop.do?method=view&shop_id=391796 HTTP/1.1"
    #"GET /EntpShop.do?method=view&shop_id=391796 HTTP/1.1"
    __requestP = r"""?P<request>\"[^\"]*\""""
    __statusP = r"?P<status>\d+"
    __bodyBytesSentP = r"?P<bodyByteSent>\d+"
    #"http://test.myweb.com/myAction.do?method=view&mod_id=&id=1346"
    __referP = r"""?P<refer>\"[^\"]*\""""
    #"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"'
    __userAgentP = r"""?P<userAgent>\"[^\"]*\""""
    #(compatible; Googlebot/2.1; +http://www.google.com/bot.html)"'
    __userSystems = re.compile(r'\([^\(\)]*\)')
    __userlius = re.compile(r'[^\)]*\"')
    __nginxLogPattern = None
    __lastline = ''
    __linenum = 0
    def __init__(self, Pattern=r"(%s)\ -\ -\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)"):
        self.__nginxLogPattern = re.compile(Pattern % (self.__ipP, self.__timeP, self.__requestP, self.__statusP, self.__bodyBytesSentP, self.__referP, self.__userAgentP), re.VERBOSE)

    def getetl(self, line):
        matchs = self.__nginxLogPattern.match(line)
        if matchs != None:
            allGroup = matchs.groups()
            m = hashlib.md5()
            if self.__lastline == line:
                m.update(self.__lastline+str(self.__linenum))
                self.__linenum = self.__linenum + 1
            else :
                self.__linenum = 0
                m.update(line)
            self.__lastline = line
            id = m.hexdigest()
            ip = allGroup[0].strip("\"")
            time = allGroup[1].strip("\"")
            request = allGroup[2].strip("\"")
            status = allGroup[3].strip("\"")
            bodyBytesSent = allGroup[4].strip("\"")
            refer = allGroup[5].strip("\"")
            userAgent = allGroup[6].strip("\"")
            Time = time.replace('T',' ')[1:-7]
            Time = trasferdate(Time).strip("\"")
            if len(userAgent) > 20:
                userinfo = userAgent.split(' ')
                userkel =  userinfo[0].strip("\"")
                try:
                    usersystem = self.__userSystems.findall(userAgent)
                    usersystem = usersystem[0].strip("\"")
                    #print usersystem
                    userliu = self.__userlius.findall(userAgent)
                    value = [id,ip,Time,request,status,bodyBytesSent,refer,userkel,usersystem,userliu[1].strip("\"")]
                    return value
                except IndexError:
                    userinfo = userAgent.strip("\"")
                    value = [id,ip,Time,request,status,bodyBytesSent,refer,userinfo,"",""]
                    return value
            else:
                useraa = userAgent.strip("\"")
                value = [id,ip,Time,request,status,bodyBytesSent,refer,useraa,"",""]
                #print value
                return value

