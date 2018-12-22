#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 10:28 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : models.py
# @Software: PyCharm

from db import db_handler

class BaseClass():

    def save(self):
        '''
        保存对象
        :return:
        '''
        db_handler.save(self)

    @classmethod
    def get_obj_by_name(cls,name):
        '''
        定义为一个类方法，不需要实例化变量直接使用
        :param name:
        :return: 查询的对象
        '''
        return db_handler.select(name,cls.__name__.lower())



class Admin(BaseClass):
    '''
    管理员
    '''
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.save()

    def create_school(self,school_name,addr):
        '''创建学校'''
        School(school_name,addr)


    def create_course(self,course_name,time,price):
        '''创建课程'''
        Course(course_name,time,price)


    def create_teacher(self,name,password):
        '''创建老师'''
        Teacher(name,password)



class Teacher(BaseClass):
    '''
    老师
    '''
    def __init__(self,name,password):
        self.name = name
        self.password = password

        self.save()


class Student(BaseClass):
    '''
    学生
    '''
    def __init__(self, name, password):
        self.name = name
        self.password = password

        self.save()

class School(BaseClass):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.course_list = []

        self.save()

    def add_course(self,course_name):
        self.course_list.append(course_name)
        #重新存放数据
        self.save()


class Course(BaseClass):
    def __init__(self, name,time, price):
        self.name = name
        self.time = time
        self.price = price

        self.save()
