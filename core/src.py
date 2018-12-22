#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 10:29 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : src.py
# @Software: PyCharm

from core import admin,student,teacher

fun_dic = {"1":admin.admin_view,
           "2":student.student_view,
           "3":teacher.teacher_view}

def run():
    while True:
        print("""
        1 管理员视图
        2 学生视图
        3 老师视图
        """)
        choice = input("请选择用户身份,输入q退出>>>:").strip()
        if choice == 'q': break
        if choice in fun_dic:
            fun_dic[choice]()
        else:
            print("\033[31m 输入不合法\033[0m")


