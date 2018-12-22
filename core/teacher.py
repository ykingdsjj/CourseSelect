#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 10:29 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : src.py
# @Software: PyCharm

teacher_info = {'name':None}


def teacher_login():
    pass

def choose_teacher_course():
    pass

def check_course():
    pass

def check_student():
    pass

def change_student_score():
    pass

fun_dict = {
    "1":teacher_login,
    "2":choose_teacher_course,
    "3":check_course,
    "4":check_student,
    "5":change_student_score
}

def teacher_view():
    while True:
        print("""
        1  登录
        2  选择课程
        3  查看课程
        4  查看学生
        5  修改学生成绩
        """)
        choice = input("请选择>>>:").strip()
        if choice == 'q': break
        if choice in fun_dict:
            fun_dict[choice]()
        else:
            print("\033[31m 输入不合法\033[0m")