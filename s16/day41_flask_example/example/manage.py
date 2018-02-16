#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from flask_script import Manager, Server
from app import create_app

app = create_app()
manager = Manager(app)


@manager.command
def custom(arg):
    """
    自定义命令
    python manage.py custom 123
    :param arg:
    :return:
    """
    print(arg)


@manager.option('-n', '--name', dest='name')
@manager.option('-u', '--url', dest='url')
def cmd(name, url):
    """
    自定义命令
    执行： python manage.py  cmd -n wupeiqi -u http://www.oldboyedu.com
    :param name:
    :param url:
    :return:
    """
    print(name, url)


@manager.command
def import_news(path):
    """
    批量导入
    :param name:
    :param url:
    :return:
    """
    import xlrd
    from xlrd.book import Book
    from xlrd.sheet import Sheet
    from xlrd.sheet import Cell
    workbook = xlrd.open_workbook(path)
    sheet_names = workbook.sheet_names()
    # sheet = workbook.sheet_by_name('工作表1')
    sheet = workbook.sheet_by_index(0)

    # 循环Excel文件的所有行
    for row in sheet.get_rows():
        # print(row)
        # 循环一行的所有列
        for col in row:
            # 获取一个单元格中的值
            print(col.value,end=';')
        print('')

# 自定义命令
manager.add_command("runserver", Server())

if __name__ == "__main__":
    manager.run()
