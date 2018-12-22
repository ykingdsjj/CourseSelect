#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 10:27 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : setting.py
# @Software: PyCharm

import os

#根路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#数据库路径
BASE_DBDIR = os.path.join(BASE_DIR,'db')
#打印日志路径
BASE_LOGDIR = os.path.join(BASE_DIR,"log")