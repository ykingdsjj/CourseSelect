#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 10:26 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : manager.py
# @Software: PyCharm

# 程序入口文件

import os,sys
# 添加环境变量
path = os.path.dirname(__file__)
sys.path.append(path)

from core import src

src.run()