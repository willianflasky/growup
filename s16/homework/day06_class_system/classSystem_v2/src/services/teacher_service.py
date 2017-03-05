#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
#
# from src.models import Admin
# from src.models import School
# from src.models import Teacher
# from src.models import Course
#
#
# def show():
#     msg = '''
#
#     '''
#     print(msg)
#
#
# def main():
#     choice_dic = {
#     }
#     show()
#
#     while True:
#         choice = input("请输入选项: ").strip()
#         if choice not in choice_dic:
#             continue
#         ret = choice_dic[choice]()
#         if ret:
#             if ret['status']:
#                 print(ret['data'].center(60, '-'))
#             else:
#                 print(ret['error'].center(60, '-'))
#
#
# def login():
#     ret = Admin.login()
#     if ret:
#         if ret['status']:
#             print(ret['data'].center(60, '-'))
#         else:
#             print(ret['error'].center(60, '-'))
#
#
# if __name__ == '__main__':
#     main()
