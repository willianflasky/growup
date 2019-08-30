#!/usr/bin/env python
#-*- coding: utf-8 -*-
# by Wendy

from django.template import Library
from django.utils.safestring import mark_safe

register = Library()

@register.simple_tag
def get_model_verbose_name(admin_class):
    """
    m1 = models.Customer
    m1._meta.verbose_name
    '客户表'
    返回表名的verbose name 有中文名的就会显示中文
    :param admin_class:这里有一个bug 如果没有传入admin_class,就应该输出model name
    :return:
    """
    return admin_class.model._meta.verbose_name


@register.simple_tag
def build_action_ele(admin_class):
    """
    1、拿到action列表
    2、循环
    3、拿到循环中的短标识名
    :param admin_class:
    :return:
    """
    '''
    >>> from crm import models
    >>> from crmAdmin.admin_base import site,BaseAdmin
    >>> class CustomerAdmin(BaseAdmin):
    ...     actions = ['status', ]
    ...     def status(self, request, querysets):
    ...             querysets.update(status=0)
    ...     status.short_description = "状态修改成报名"
    ...
    >>>
    >>> site = CustomerAdmin()
    >>> site.status
    <bound method CustomerAdmin.status of <CustomerAdmin object at 0x10ecc25c0>>
    >>> site.status.short_description
    '状态修改成报名'
    >>> site.actions
    ['status']
    >>> site.actions[0]
    'status'
    >>> site.status
    <bound method CustomerAdmin.status of <CustomerAdmin object at 0x10ecc25c0>>
    >>> func = getattr(site,'status')
    >>> func
    <bound method CustomerAdmin.status of <CustomerAdmin object at 0x10ecc25c0>>
    >>> func.short_description
    '状态修改成报名'
    >>>
    '''

    action_list = admin_class.actions

    select_ele = "<select class='form-control' name='_action'>"

    select_ele += "<option value="" selected="">---------</option>"
    select_ele += "<option value='_delete_selected'>Delete selected %s</option>"%admin_class.model._meta.verbose_name

    for action in action_list:

        func = getattr(admin_class, action)

        name = func.short_description

        option_ele = "<option value=%s >%s</option>"%(action,name)

        select_ele += option_ele


    select_ele += "</select>"
    return mark_safe(select_ele)




@register.simple_tag
def build_filter_ele(filter_column,admin_class,filter_conditions):
    """
    1、拿到要过来字段的对象 field_obj
    2、调用field_obj.get_choices()
    3、生成select元素
    4、循环choices列表,生成option元素
    :param filter_column: list filter
    :param admin_class:
    :param filter_conditions:  为了下次返回以后保留上次过滤的条件
    :return:
    """
    field_obj = admin_class.model._meta.get_field(filter_column)
    '''
    m1 = models.Customer
    m1._meta.get_field('name')
        <django.db.models.fields.CharField: name>
    '''
    select_ele = "<select class='form-control' name=%s>" %filter_column
    #select 元素 name是过滤的字段名

    filter_option = filter_conditions.get(filter_column)
    '''
    1、None代表没有对这个字段过滤
    2、有值选定的具体的option的val
    '''

    if filter_option: #字段过滤
        for choice in field_obj.get_choices():
            '''
            >>> m1._meta.get_field('name').get_choices() 对这种正常的反而没有效了
                Traceback (most recent call last):
                  File "<console>", line 1, in <module>
                  File "/usr/local/lib/python3.6/site-packages/django/db/models/fields/__init__.py", line 807, in get_choices
                    rel_model = self.remote_field.model
                AttributeError: 'NoneType' object has no attribute 'model'
                >>>针对外键和choices有效
                >>> m1._meta.get_field('status').get_choices()
                [('', '---------'), (0, '已报名'), (1, '已退费'), (2, '未报名')]
                >>> m1._meta.get_field('source').get_choices()
                [('', '---------'), (1, '百度推广'), (2, 'QQ')]
            '''
            if filter_option == str(choice[0]):
                selected = 'selected'
            else:
                selected = ''

            option_ele = "<option value=%s  %s>%s</option>" %(choice[0],selected,choice[1])
            select_ele += option_ele

    else:
         for choice in field_obj.get_choices():
             option_ele = "<option value=%s >%s</option>" %(choice[0],choice[1])
             select_ele += option_ele

    select_ele += "</select>"
    return mark_safe(select_ele)


@register.simple_tag
def build_table_row(row,admin_class):
    """
    1、循环list display 反射出每个字段的值
    2、判断是否是第一个字段,如果是,加a标签
    :param row: querysets中的每条记录
    :param admin_class: 里面有list display
    :return:
    """
    row_ele = "<tr>"
    for index,column_name in enumerate(admin_class.list_display):
        field_obj = row._meta.get_field(column_name)
        if field_obj.choices:
            '''
            >>> queryset = models.Customer.objects.filter()
            >>> for row in queryset:
            ...     print(row)
            ...
            tangying1
            tangying2

            >>> for row in queryset:
            ...     row._meta.get_field('name').choices
            ...
            []
            []
            >>> for row in queryset:
            ...     row._meta.get_field('status').choices
            ...  #choice字段是有值的
            ((0, '已报名'), (1, '已退费'), (2, '未报名'))
            ((0, '已报名'), (1, '已退费'), (2, '未报名'))
            ((0, '已报名'), (1, '已退费'), (2, '未报名'))
            '''
            column_display_func = getattr(row,"get_%s_display"%column_name)
            column_val = column_display_func()
            '''
            >>> for row in queryset:
            ...     row.get_status_display()
            ...
            '未报名'
            '已退费'
            '''
        else:
            column_val = getattr(row,column_name)
            """
            >>> for row in queryset:
            ...     row.name
            ...
            'tangying1'
            'tangying2'
            """

        if index == 0:
            # 进入详细页面http://127.0.0.1:8007/admin/crm/customer/16/change/  django admin
            # 仿照django admin的详细页面的url
            '''
            >>> queryset = models.Customer.objects.filter()
            >>> for row in queryset:
            ...     print(row.id)
            ...
            1
            2
            '''
            td_ele1 = "<td><label><input name='_selected_action' value='%s' type='checkbox'></label></td>"%row.id
            td_ele2 = "<td><a href='{obj_id}/change/'>{column_val}</a></td>".format(obj_id=row.id,column_val=column_val)
            td_ele = td_ele1 + td_ele2
        else:
            td_ele = "<td>{column_val}</td>".format(column_val=column_val)

        row_ele += td_ele

    row_ele += "</tr>"
    return mark_safe(row_ele)


@register.simple_tag
def get_filter_condtions_string(filter_conditions,q_val):
    condtion_str = ""
    for k,v in filter_conditions.items():
        condtion_str += "&%s=%s"%(k,v)
        #翻页的时候依旧带上过滤的信息
        if q_val: #拼接serach字段
            condtion_str += "&_q=%s" %q_val
    return condtion_str


@register.simple_tag
def get_abs_value(loop_num,current_page_number):
    """返回当前页与循环loopnum的差的绝对值"""
    return abs(loop_num - current_page_number)


@register.simple_tag
def generate_orderby_icon(new_order_key):
    if new_order_key.startswith('-'):
        icon_ele = """<i class="fa fa-angle-down" aria-hidden="true"></i>"""
    else:
        icon_ele = """<i class="fa fa-angle-up" aria-hidden="true"></i>"""
    return mark_safe(icon_ele)


@register.simple_tag
def get_m2m_objects(admin_class,field_name,selected_objs):
    """
    1、根据field_name从admin_class.model反射出字段对象
    2、拿到关联表所有数据
    3、返回数据
    :param admin_class:
    :param field_name:
    :param selected_objs:
    :return:
    """
    field_obj = getattr(admin_class.model,field_name)
    all_objects = field_obj.rel.to.objects.all()
    return set(all_objects) - set(selected_objs)

'''
    >>> field_obj = models.Customer.consult_courses
    >>>
    >>> models.Customer.consult_courses
    <django.db.models.fields.related_descriptors.ManyToManyDescriptor object at 0x106f5e128>
    >>>
    >>> field_obj.rel
    <ManyToManyRel: crm.customer>
    >>>
    >>> field_obj.rel.to
    <class 'crm.models.Course'>
    >>>
    >>> field_obj.rel.to.objects.all()
    <QuerySet [<Course: Go>, <Course: Python>]>
'''




@register.simple_tag
def get_selected_m2m_objects(form_obj,field_name):
    """
    1、根据field_name反射出form_obj.instance里的字段对象,即目前用户数据库中记录的数据的显示
    2、拿到字段对象关联的所有数据
    :param form_obj:
    :param field_name:
    :return:
    """
    if form_obj.instance.id:
        field_obj = getattr(form_obj.instance,field_name)
        return field_obj.all()
    else:
        return []

'''
    >>> from crm import models
    >>> from django.forms import ModelForm
    >>> class CustomerForm(ModelForm):
    ...     class Meta:
    ...             model = models.Customer
    ...             fields = '__all__'
    ...
    >>> object = models.Customer.objects.get(id=1)
    >>> form_obj = CustomerForm(instance=object)
    >>> form_obj.instance.id
    1
    >>>

    field_obj = getattr(form_obj.instance,field_name)
        return field_obj.all()
    反射
    >>> form_obj.instance.tags.all()
    <QuerySet []>
    >>> form_obj.instance.consult_courses.all()
    <QuerySet [<Course: Go>]>
    '''

@register.simple_tag
def get_relationships(admin_class):
    return admin_class.model._meta.many_to_many
