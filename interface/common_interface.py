#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 10:29 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : common_interface.py
# @Software: PyCharm
from db import models

def login_interface(name,password,user_type):
    '''

    :param name:
    :param password:
    :param user_type:
    :return:
    '''
    #保持程序健壮性
    obj = None
    if user_type == 'admin':
        obj = models.Admin.get_obj_by_name(name)
    elif user_type == 'teacher':
        obj = models.Teacher.get_obj_by_name(name)
    elif user_type == 'student':
        obj = models.Student.get_obj_by_name(name)
    else:
        return False,"没有这个用户类型"

    if obj:
        if obj.password == password:
            return True,"%s %s 登录成功" %(user_type,name)
        else:
            return False, "密码错误"
    else:
        return False,'用户不存在'


def check_all_schools():
    '''
    查询所有的学校
    :return:
    '''
    import os
    from conf import setting
    from lib import common
    path = os.path.join(setting.BASE_DBDIR,'school')
    return common.get_all_obj_list(path)
