#!/usr/bin/env python
# -*- coding: utf-8 -*-  

"""
@desc:  1、str(e)
返回字符串类型，只给出异常信息，不包括异常信息的类型，如1/0的异常信息
'integer division or modulo by zero'
2、repr(e)
给出较全的异常信息，包括异常信息的类型，如1/0的异常信息
"ZeroDivisionError('integer division or modulo by zero',)"
3、e.message
获得的信息同str(e)
4、采用traceback模块
需要导入traceback模块，此时获取的信息最全，与python命令行运行程序出现错误信息一致。
使用traceback.print_exc()打印异常信息到标准错误，就像没有获取一样，
或者使用traceback.format_exc()将同样的输出获取为字符串。
你可以向这些函数传递各种各样的参数来限制输出，或者重新打印到像文件类型的对象。
@version: python 2.7
@author: jinyuwang
@contact: wjy.wxl@gmail.com
@license: Apache Licence
@software: practise on A stock
@file: get_exception_info.py
@time: 2018/1/10 上午9:51
"""

import traceback

print '########################################################'
print "1/0 Exception Info"
print '---------------------------------------------------------'
try:
    1/0
except Exception as e:
    print 'str(Exception):\t', str(Exception)
    print 'str(e):\t\t', str(e)
    print 'repr(e):\t', repr(e)
    print 'e.message:\t', e.message
    print 'traceback.print_exc():'; traceback.print_exc()
    print 'traceback.format_exc():\n%s' % traceback.format_exc()
print '########################################################'
print '\n########################################################'
print "i = int('a') Exception Info"
print '---------------------------------------------------------'
try:
    i = int('a')
except Exception, e:
    print 'str(Exception):\t', str(Exception)
    print 'str(e):\t\t', str(e)
    print 'repr(e):\t', repr(e)
    print 'e.message:\t', e.message
    print 'traceback.print_exc():'; traceback.print_exc()
    print 'traceback.format_exc():\n%s' % traceback.format_exc()
print '########################################################'

def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass