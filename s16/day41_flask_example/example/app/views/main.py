#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, request, render_template, redirect

main = Blueprint('main', __name__)


@main.route('/index')
def index():
    # return "Index"
    # import xlrd
    # from xlrd.book import Book
    # from xlrd.sheet import Sheet
    # from xlrd.sheet import Cell
    #
    # workbook = xlrd.open_workbook("/Users/wupeiqi/PycharmProjects/Flask课程/6.Flask-Login/task_data_881788.xlsx")
    #
    # sheet_names = workbook.sheet_names()
    #
    # # sheet = workbook.sheet_by_name('工作表1')
    # sheet = workbook.sheet_by_index(0)

    # 循环Excel文件的所有行
    # for row in sheet.get_rows():
    #     # print(row)
    #     # 循环一行的所有列
    #     for col in row:
    #         # 获取一个单元格中的值
    #         print(col.value,end=';')
    #     print('')
    #     break

    # return render_template('index.html',sheet=sheet)
    return render_template('index.html')
