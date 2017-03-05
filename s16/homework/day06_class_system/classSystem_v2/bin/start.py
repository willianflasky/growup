#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import os
import sys

BASE_DIR = os.path.normpath(os.path.join(__file__, os.pardir, os.pardir))
sys.path.insert(0, BASE_DIR)

from src.services import admin_service
from src.services import teacher_service
from src.services import student_service
from src.services import initialize_service


def show_role():
    msg = """
        0:初始化
        1:管理员
        2:老师
        3:学生
        """
    print(msg)


if __name__ == '__main__':
    role_main = {
        '0': initialize_service.main,
        "1": admin_service.main,
        "2": teacher_service,
        "3": student_service
    }

    while True:
        show_role()
        choice = input("输入角色: ").strip()
        if choice not in role_main:
            continue
        role_main[choice]()

