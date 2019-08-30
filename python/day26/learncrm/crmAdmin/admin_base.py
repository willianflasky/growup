#!/usr/bin/env python
#-*- coding: utf-8 -*-
# by Wendy

class BaseAdmin(object):
    list_display = ()
    list_filter = ()
    list_per_page = 5
    search_fields = []
    filter_horizontal = []
    action = []

class AdminSite(object):
    def __init__(self):
        self.registered_admins = {}

    def register(self, model_or_iterable, admin_class=BaseAdmin, **options):
        """
        负责把每个App下的表注册self.registered_admins 集合里
        :param model_or_iterable: models.Customer
        :param admin_class: 自定义admin显示,默认是BaseAdmin不然会报错,如果这里没有BaseAdmin那么下面的装载modles会报错
        :param options:
        :return:
        """

        admin_class.model = model_or_iterable #把model装到admin class 里面以供simple tags 调用
        """
        admin_class
            model = admin_class.models.customer
            list_display .....
        """

        app_label = model_or_iterable._meta.app_label
        """
        #models.Customer._meta.app_lable
        根据models.Customer 拿到app的名字
        from crm import models
        m1 = models.Customer
        dir(m1._meta)
        m1._meta.app_label
        'crm'
        """

        if app_label not in self.registered_admins:
            self.registered_admins[app_label] = {}
            #{crm : {}} 出这么一个字典
        self.registered_admins[app_label][model_or_iterable._meta.model_name] = admin_class
        """
        拿到{crm:{customer:{这个中间是的value}}} = admin_class
        #拿到表名customer
        m1._meta.model_name
        'customer'

        其实就是最后拼成这么一个货
        {crm:{customer:{admin_class(models.cutomer,list_display....)}}}
        """

site = AdminSite()
#实例化