#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


# 模仿django admin的方式,我们也自建个基类
class BaseAdmin(object):
    """默认值"""
    list_display = ()
    list_filter = ()
    list_per_page = 5
    search_fields = ()


class AdminSite(object):
    def __init__(self):
        # 大字典
        self.registered_admins = {}

    def register(self, model_or_iterable, admin_class=BaseAdmin, **options):
        """
        负责把每个APP下的表注册都存到self.registered_admins大字典中.
        :param model_or_iterable:       models.py中的类表映射关系
        :param admin_class:             表对应的管理类,默认用基类
        :param options:                 其它
        :return:
        """
        # 把modelu装到admin_class中,以供simple tags调用. 直接传递model到前端,HTML会报错.
        admin_class.model = model_or_iterable

        # 通过model._meta.app_label拿到model所在的APP名称
        app_label = model_or_iterable._meta.app_label

        # 如果app_label没有在大字典中,则加进去.
        if app_label not in self.registered_admins:
            self.registered_admins[app_label] = {}
        self.registered_admins[app_label][model_or_iterable._meta.model_name] = admin_class
        # {'crm':{'account':admin_class}}  注意:admin_class.model 存了表类

        # 例如: crm app下面的Account表
        # Account._meta.app_label  获取"crm"值
        # Account._meta.model_name 获取"account"值
# 实例化
site = AdminSite()

