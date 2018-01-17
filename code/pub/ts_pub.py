#!/usr/bin/env python
# -*- coding: utf-8 -*-  

"""
Desc: 
File: ts_bar.py
Author: wangjinyu
Date: 2018/1/17 16:45
"""
import os
import sys
import tushare as ts
from code.pub.common import DATA_PATH, PATH_SEP
from tushare.fund import cons as ct
from tushare.util import dateu as du

reload(sys)
sys.setdefaultencoding('utf-8')

today = du.today()
profit_data_file = DATA_PATH + PATH_SEP + 'profit_data' + today + '.csv'
# 删除一周前同一天文件,如果天天运行,则只保留一周数据
del_file = DATA_PATH + PATH_SEP + 'profit_data' + du.day_last_week() + '.csv'
if os.path.exists(del_file):
    os.remove(del_file)

if not os.path.exists(profit_data_file):
    df = ts.profit_data(year=today[:4])
    if df.loc[0, 'code'] == '000nan':
        df = ts.profit_data(year=int(today[:4]) - 1)
    df.to_csv(profit_data_file, sep=',', header=True, index=False, encoding='GBK')

if __name__ == '__main__':
    pass
