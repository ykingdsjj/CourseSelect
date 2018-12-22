#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 10:29 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : src.py
# @Software: PyCharm

student_info = {'name':None}

def student_register():
    pass

def student_login():
    pass

def choose_school():
    pass

def choose_course():
    pass

def check_score():
    pass

fun_dict = {
    "1":student_register,
    "2":student_login,
    "3":choose_school,
    "4":choose_course,
    "5":check_score
}


def student_view():
    while True:
        print("""
        1  注册
        2  登录
        3  选择学校
        4  选择课程
        5  查看成绩
        """)
        choice = input("请选择>>>:").strip()
        if choice == 'q': break
        if choice in fun_dict:
            fun_dict[choice]()
        else:
            print("\033[31m 输入不合法\033[0m")