#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Function: 环境初始化：创建上层目录kenny_data(子目录 day,macro,...)
Author: jinyuwang
Date: 2018/1/6
"""
import os, errno
from code.pub.common import DATA_PATH


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5 (except OSError, exc: for Python <2.5)
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


if __name__ == '__main__':
    # DATA_PATH = os.path.dirname(os.path.dirname(WORK_DIR)) + PATH_SEP + 'kenny_data'
    if not os.path.exists(DATA_PATH):
        os.mkdir(DATA_PATH)
    else:
        print DATA_PATH, ' exists'
