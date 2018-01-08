#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Function: 本项目会用到的公共变量或函数
Author: jinyuwang
Date: 2018/1/6
"""
import os
import platform

WORK_DIR = os.getcwd()
sysstr = platform.system()
if (sysstr == "Windows"):
    PATH_SEP = '\\'
elif (sysstr == "Linux"):
    PATH_SEP = '/'
DATA_PATH = os.path.dirname(os.path.dirname(WORK_DIR)) + PATH_SEP + 'kenny_data'

#


def TestPlatform():
    print ("----------Operation System--------------------------")
    #  获取Python版本
    print platform.python_version()

    #   获取操作系统可执行程序的结构，，(’32bit’, ‘WindowsPE’)
    print platform.architecture()

    #   计算机的网络名称，’acer-PC’
    print platform.node()

    # 获取操作系统名称及版本号，’Windows-7-6.1.7601-SP1′
    print platform.platform()

    # 计算机处理器信息，’Intel64 Family 6 Model 42 Stepping 7, GenuineIntel’
    print platform.processor()

    # 获取操作系统中Python的构建日期
    print platform.python_build()

    #  获取系统中python解释器的信息
    print platform.python_compiler()

    if platform.python_branch() == "":
        print platform.python_implementation()
        print platform.python_revision()
    print platform.release()
    print platform.system()

    # print platform.system_alias()
    #  获取操作系统的版本
    print platform.version()

    #  包含上面所有的信息汇总
    print platform.uname()


def UsePlatform():
    sysstr = platform.system()
    if (sysstr == "Windows"):
        print ("Call Windows tasks")
    elif (sysstr == "Linux"):
        print ("Call Linux tasks")
    else:
        print ("Other System tasks")


if __name__ == '__main__':
    pass
    print "WORK_DIR = %s" % WORK_DIR
    print "PATH_SEP = %s" % PATH_SEP
    print "DATA_PATH = %s" % DATA_PATH
