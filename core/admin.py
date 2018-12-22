#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 10:29 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : src.py
# @Software: PyCharm

from interface import admin_interface
from interface import common_interface
from interface import teacher_interface
from interface import student_interface
from lib import common


#保存用户信息
admin_info = {'name':None}

def admin_register():
    while True:
        name = input("请输入名字>>>>:").strip()
        password = input("请输入密码>>>>:").strip()
        con_password = input("请确认密码>>>:").strip()
        if password == con_password:
            flg,msg = admin_interface.admin_register_interface(name,password)
            print(msg)
            if flg:
                admin_info['name'] = name
                # 注册成功了就返回上一层，失败了就继续执行
                break
        else:
            print("\033[31m两次密码输入不一致\033[0m")

def admin_login():
    while True:
        name = input("请输入名字>>>>:").strip()
        password = input("请输入密码>>>>:").strip()
        flg, msg = common_interface.login_interface(name, password,"admin")
        print(msg)
        if flg:
            # 登录成功了就返回上一层，失败了就继续执行
            admin_info['name'] = name
            break

@common.login_auth(user_type='admin')
def create_school():
    '''
    添加装饰器，没有登录先执行登陆在说
    :return:
    '''
    school_name = input("请输入学校名字>>>>:").strip()
    address = input("请输入学校地址>>>>:").strip()
    flg,msg = admin_interface.create_school_interface(admin_info['name'],school_name,address)
    print(msg)


@common.login_auth(user_type='admin')
def create_teacher():
    teacher_name = input("请输入老师名字>>>>:").strip()
    # password有一个默认值
    # password = input("请输入账号密码>>>>:").strip()
    flg, msg = admin_interface.create_teacher_interface(admin_info['name'], teacher_name)
    print(msg)


@common.login_auth(user_type='admin')
def create_course():
    #绑定学校列表，查询学校列表再去绑定
    while True:
        school_list = common_interface.check_all_schools()
        if school_list:
            print("学校列表".center(40, "*"))
            for i,school in enumerate(school_list):
                print("%s %s" %(i,school))
            print("end".center(40, "*"))
            choice = input("请选择学校，输入序号>>>>:").strip()
            if choice.isdigit():
                choice = int(choice)
                if choice < 0 and choice >= len(school_list): continue

                course_name = input("请输入课程名字>>>>:").strip()
                time = input("请输入学校地址>>>>:").strip()
                price = input("请输入课程价格>>>:").strip()
                flg, msg = admin_interface.create_course_interface(admin_info['name'], course_name, time, price)
                print(msg)
                if flg: break
            else:
                print("请输入数字")
        else:
            print('请先创建学校')



fun_dict = {
    "1":admin_register,
    "2":admin_login,
    "3":create_school,
    "4":create_teacher,
    "5":create_course
}

def admin_view():
    while True:
        print("""
        1  注册
        2  登录
        3  创建学校
        4  创建老师
        5  创建课程
        """)
        choice = input("请选择>>>:").strip()
        if choice == 'q': break
        if choice in fun_dict:
            fun_dict[choice]()
        else:
            print("\033[31m 输入不合法\033[0m")