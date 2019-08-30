from django.template import Library
from django.utils.safestring import mark_safe

register = Library()

@register.simple_tag
def get_model_verbose_name(admin_class):
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
            td_ele = "<td><a href='{obj_id}/change/'>{column_val}</a></td>".format(obj_id=row.id,column_val=column_val)
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
def get_filter_condtions_string(filter_conditions,q_val):
    condtion_str = ""
    for k,v in filter_conditions.items():
        condtion_str += "&%s=%s" %(k,v)
    if q_val:#拼接search 字段
        condtion_str += "&_q=%s" % q_val
    return condtion_str


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
    1.根据field_name从admin_class.model反射出字段对象
    2.拿到关联表的所有数据
    3.返回数据
    :param admin_class:
    :param field_name:
    :return:
    """

    field_obj = getattr(admin_class.model,field_name)
    all_objects = field_obj.rel.to.objects.all()
    return set(all_objects) - set(selected_objs)

@register.simple_tag
def get_selected_m2m_objects(form_obj,field_name):
    """
    1.根据field_name反射出form_obj.instance里的字段对象
    2. 拿到字段对象关联的所有数据
    :param form_obj:
    :param field:
    :return:
    """

    if form_obj.instance.id:
        field_obj = getattr(form_obj.instance, field_name)
        return field_obj.all()
    else:
        return []