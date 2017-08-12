#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from luffyAdmin import perm_custom_funcs

perm_dic = {
    'crm_table_index': ['app_index', 'GET', [], {}],                     # 查看CRM APP里面所有数据库的表
    'crm_table_list': ['model_table_list', 'GET', [], {'source': 1}, perm_custom_funcs.only_view_own_customers],    # 查看每张表里所有的数据
    'crm_table_list_view': ['table_obj_change', 'GET', [], {}],          # 查看每条数据的修改页
    'crm_table_list_change': ['table_obj_change', 'POST', [], {}],       # 可以对表里的每条数据进行修改
    }
