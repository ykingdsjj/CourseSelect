#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 10:27 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : db_handler.py
# @Software: PyCharm

from conf import setting
import os
import pickle

def save(obj):
    '''
    存储文件，保存为pickle对象
    :param obj:
    :return:
    '''
    path_dir = os.path.join(setting.BASE_DBDIR,obj.__class__.__name__.lower())
    if not os.path.isdir(path_dir):
        os.mkdir(path_dir)
    path_obj = os.path.join(path_dir,obj.name)
    with open(path_obj,"wb") as f:
        pickle.dump(obj,f)


def select(name,dir_type):
    '''
    根据类型-读取文件信息，
    :param name:
    :param dir_type:
    :return:
    '''
    path_dir = os.path.join(setting.BASE_DBDIR,dir_type)
    if not os.path.isdir(path_dir):
        os.mkdir(path_dir)
    path_obj = os.path.join(path_dir,name)
    if os.path.exists(path_obj):
        with open(path_obj,'rb') as f:
            return pickle.load(f)
    else:
        return False

