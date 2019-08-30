from django.template import Library
from django.utils.safestring import mark_safe

register = Library()


@register.simple_tag
def get_model_verbose_name(admin_class):
    # 显示表的 verbose_name
    # admin_class这个类中存放了model这个是表类,通过他的_meta可以拿到verbose_name
    return admin_class.model._meta.verbose_name


@register.simple_tag
def get_model_name(model_class):
    return model_class._meta.model_name


@register.simple_tag
def get_app_name(model_class):
    return model_class._meta.app_label


@register.simple_tag
def build_filter_ele(filter_column,admin_class,filter_conditions):
    """
    1.拿到要过滤字段的对象field_obj
    2. 调用field_obj.get_choices()
    3. 生成select元素
    4.循环choices列表，生成option元素
    :param filter_column:
    :param model_class:
    :return:
    """
    field_obj = admin_class.model._meta.get_field(filter_column)
    select_ele = "<select class='form-control' name=%s>"% filter_column
    filter_option = filter_conditions.get(filter_column) #1.None 代表没有对这个字段过滤，2.有值，选中的具体的option的val
    print('filter option',filter_option)
    if filter_option:#代表此字段过滤了
        for choice in field_obj.get_choices():
            if filter_option == str(choice[0]):
                selected = 'selected'
            else:
                selected = ''
            option_ele = "<option value=%s  %s>%s</option>" % (choice[0],selected,choice[1])
            select_ele += option_ele
    else:
        for choice in field_obj.get_choices():
            option_ele = "<option value=%s >%s</option>" % (choice[0],choice[1])
            select_ele += option_ele


    select_ele += "</select>"
    return mark_safe(select_ele)

@register.simple_tag
def build_table_row(row,admin_class):
    """
    1.循环list_display , 反射出每个字段的值
    2. 判断是否是第一个字段， 如果是，加a标签
    3.
    :param row:
    :param admin_class:
    :return:
    """
    row_ele = "<tr>"
    for index,column_name in enumerate(admin_class.list_display):
        field_obj = row._meta.get_field(column_name)
        if field_obj.choices:
            column_display_func = getattr(row,"get_%s_display"% column_name)
            column_val = column_display_func()
        else:
            column_val = getattr(row,column_name)

        if index == 0:
            td_ele = "<td><a href='#'>{column_val}</a></td>".format(column_val=column_val)
        else:
            td_ele = "<td>{column_val}</td>".format(column_val=column_val)
        row_ele += td_ele

    row_ele += "</tr>"
    return mark_safe(row_ele)


@register.simple_tag
def get_abs_value(loop_num , curent_page_number):
    """返回当前页与循环loopnum的差的绝对值"""
    return abs(loop_num - curent_page_number)

@register.simple_tag
def get_filter_condtions_string(filter_conditions):
    condtion_str = ""
    for k,v in filter_conditions.items():
        condtion_str += "&%s=%s" %(k,v)

    return condtion_str