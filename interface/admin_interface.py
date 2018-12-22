#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 10:29 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : common_interface.py
# @Software: PyCharm

from db import models

def admin_register_interface(name,password):
    '''
    注册管理员对象
    :param name:
    :param password:
    :return:
    '''
    admin_obj = models.Admin.get_obj_by_name(name)
    if admin_obj:
        return False,"管理员已存在"
    else:
        models.Admin(name,password)
        return True, "管理员注册成功"



def create_school_interface(admin_name,school_name,addr):
    '''
    创建学校的方法
    :param admin_name: 管理员名称
    :param school_name: 学校名称
    :param addr: 学校地址
    :return:
    '''
    school_obj = models.School.get_obj_by_name(school_name)
    if school_obj:
        return False,"该学校已经存在"
    else:
        #获取管理员对象,管理员创建学校对象
        admin_obj = models.Admin.get_obj_by_name(admin_name)
        admin_obj.create_school(school_name,addr)

        return True,"创建学校成功"


def create_teacher_interface(admin_name,teacher_name,password='123456'):
    '''
    创建老师
    :param admin_name:
    :param teacher_name:
    :param password:
    :return:
    '''
    teacher_obj = models.Teacher.get_obj_by_name(teacher_name)
    if teacher_obj:
        return False,'该老师已经存在'
    else:
        admin_obj = models.Admin.get_obj_by_name(admin_name)
        admin_obj.create_teacher(teacher_name,password)
        return True,"老师创建成功"


def create_course_interface(admin_name,school_name,course_name,time,price):
    course_obj = models.Course.get_obj_by_name(course_name)
    if course_obj:
        return False, '该课程已经存在'
    else:
        admin_obj = models.Admin.get_obj_by_name(admin_name)
        admin_obj.create_course(course_name, time,price)

        #把课程加到学校里面
        school_obj = models.School.get_obj_by_name(school_name)
        school_obj.add_course(course_name)
        return True, "课程创建成功"

