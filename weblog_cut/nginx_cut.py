__author__ = 'franciscui'
# coding=utf-8
# Usage crontab: 59 23 * * * python /path/logcron.py

import os
import glob
import time
import shutil


class Nginxcut:
    __path = ''
    __cut_path = ''
    __nginx_pid = ''
    __filename = ''

    def __init__(self, path, cut_path, nginx_pid, filename):
        self.__cut_path = cut_path
        self.__nginx_pid = nginx_pid
        self.__path = path
        self.__filename = filename

    def cutlog(self):
        if not os.path.exists(self.__cut_path):
            os.makedirs(self.__cut_path)
        sfile = self.__path+'/'+self.__filename
        newfilename = self.__cut_path + '/' + self.__filename + '_' + str(time.strftime("%Y%m%d", time.localtime())) + '.log'
        os.system("mv %s %s"%(sfile,newfilename))
        os.system("kill -s USR1 `cat %s`"%(self.__nginx_pid))
        os.system("kill -s USR1 `cat %s`"%(self.__nginx_pid))
        return newfilename


