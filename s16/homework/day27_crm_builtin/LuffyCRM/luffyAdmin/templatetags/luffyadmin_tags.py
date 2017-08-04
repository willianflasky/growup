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
def build_filter_ele(filter_column, admin_class, filter_conditions):
    """
    1. 拿到要过滤字段的对象field_obj
    2. 调用field_obj.get_choices()
    3. 生成select元素
    4. 循环choices列表，生成option元素
    :param filter_column:  过滤的字段
    :param admin_class: 表
    :param filter_conditions: 过滤条件
    :return:
    """
    # 拿表的字段的对象
    field_obj = admin_class.model._meta.get_field(filter_column)
    # 生成标签
    select_ele = "<select class='form-control' name=%s>" % filter_column
    # None或者有值
    filter_option = filter_conditions.get(filter_column)    # 1.None 代表没有对这个字段过滤，2.有值，选中的具体的option的val
    print('filter option::::', filter_option)
    if filter_option:   # 代表此字段过滤了
        # 数据:   [('', '---------'), (0, '已报名'), (1, '已退费'), (2, '未报名')]
        for choice in field_obj.get_choices():
            if filter_option == str(choice[0]):     # 如果相等, 变成 option标签的selected
                selected = 'selected'
            else:
                selected = ''
            option_ele = "<option value=%s  %s>%s</option>" % (choice[0], selected, choice[1])
            select_ele += option_ele
    else:   # None 这里没有过滤条件     ('', '---------')
        for choice in field_obj.get_choices():
            option_ele = "<option value=%s >%s</option>" % (choice[0], choice[1])
            select_ele += option_ele

    select_ele += "</select>"
    return mark_safe(select_ele)

"""
    <select class="form-control" name="status">
        <option value="">---------</option>
        <option value="0" selected="">已报名</option>
        <option value="1">已退费</option><option value="2">未报名</option>
    </select>
"""


@register.simple_tag
def build_table_row(row, admin_class):
    """
    1. 循环list_display , 反射出每个字段的值
    2. 判断是否是第一个字段， 如果是，加a标签
    3.
    :param row:
    :param admin_class:
    :return:
    """
    row_ele = "<tr><td><input class='row-obj' name='_selected_obj' type='checkbox' value='{obj_id}'></td>".format(obj_id=row.id)

    if admin_class.list_display:
        # 循环列表
        for index, column_name in enumerate(admin_class.list_display):
            # 拿到字段对象
            field_obj = row._meta.get_field(column_name)
            # 判断是否 choices
            if field_obj.choices:
                column_display_func = getattr(row, "get_%s_display" % column_name)
                column_val = column_display_func()
            else:
                column_val = getattr(row, column_name)
            # 判断第一个字段,增加A标签
            if index == 0:
                td_ele = "<td><a href='{obj_id}/change/'>{column_val}</a></td>".format(obj_id=row.id, column_val=column_val)
            else:
                td_ele = "<td>{column_val}</td>".format(column_val=column_val)
            row_ele += td_ele

    else:   # 显示对象的Str格式
        td_ele = "<td><a href='{obj_id}/change/'>{obj_str}</a></td>".format(obj_id=row.id, obj_str=row)
        row_ele += td_ele
    row_ele += "</tr>"
    return mark_safe(row_ele)


@register.simple_tag
def get_abs_value(loop_num, curent_page_number):
    """返回当前页与循环loopnum的差的绝对值"""
    return abs(loop_num - curent_page_number)


@register.simple_tag
def get_filter_condtions_string(filter_conditions, q_val):
    condtion_str = ""
    for k, v in filter_conditions.items():
        condtion_str += "&%s=%s" % (k, v)
    if q_val:   # 拼接search 字段
        condtion_str += "&_q=%s" % q_val
    return condtion_str


@register.simple_tag
def generate_orderby_icon(new_order_key):
    if new_order_key.startswith('-'):
        icon_ele = '<i class="fa fa-angle-down" aria-hidden="true"></i>'
    else:
        icon_ele = '<i class="fa fa-angle-up" aria-hidden="true"></i>'

    return mark_safe(icon_ele)


@register.simple_tag
def get_m2m_objects(admin_class, field_name, selected_objs):
    # 1.根据field_name, 从admin_class.model反射字段对象
    # 2.拿到关联表的所有数据
    # 3.返回数据
    field_obj = getattr(admin_class.model, field_name)
    all_objects = field_obj.rel.to.objects.all()
    # 拿到字段对象, 把关联表的数据都取到
    return set(all_objects) - set(selected_objs)


@register.simple_tag
def get_selected_m2m_objects(form_obj, field_name):
    """
    1. 根据field_name反射出form_obj.instance里的字段对象
    2. 拿到字段对象关联的所有数据
    :param admin_class:
    :param flied_name:
    :return:
    """
    # 判断空值就不反射
    if form_obj.instance.id:
        field_obj = getattr(form_obj.instance, field_name)
        return field_obj.all()
    else:
        return ""


@register.simple_tag
def object_delete(obj, recursive=False):
    """
    1. 通过obj.related_objects拿到所有外键关联的对象列表 如: obj = Account.objects.get(id=2); obj.related_objects
    2. 循环关联对象关系表. for i in obj.related_objects; 调用relate_name = i.get_accessor_name() 拿到反向查询的字段名.
    3. 根据反向查询字段名, 拿到关系的对象.  obj.relate_name.all()
    4. 对关联的对象再重复1,2,3步骤,直到没有更深入的关联关系为止.

    :param obj:
    :return:

    meta:
        1. related_objects获取别的表FK我. 获取个列表
            obj = Account.objects.get(id=2); obj.related_objects
        2. get_accessor_name()获取反向外键查询的名字通常是表名_set
            obj = Account.objects.get(id=2); A=obj.related_objects[0]; A.get_accessor_name()
    """
    if not recursive:
        ele = "<ul><li>{object_name}".format(object_name=obj)
    else:
        ele = "<ul>"

    local_m2m = obj._meta.local_many_to_many       # 处理多对多

    for m2m_field in local_m2m:
        m2m_objs = getattr(obj, m2m_field.name).all()
        for m2m_obj in m2m_objs:
            ele += "<li>{obj_name}:{m2m_name}</li>".format(obj_name=m2m_field.name, m2m_name=m2m_obj)

    for i in obj._meta.related_objects:
        reverse_lookup_key = i.get_accessor_name()
        try:
            reverse_lookup_field = getattr(obj, reverse_lookup_key)
            query_set = reverse_lookup_field.all()
            child_ele = "<ul>"
            for o in query_set:
                child_ele += "<li>{model_verbose_name}:<a>{obj_name}</a></li>".format(
                                                                        model_verbose_name=o._meta.verbose_name,
                                                                        obj_name=o)
                if o._meta.related_objects:   # 代表还有下一层
                    child_ele +=object_delete(o, recursive=True)
            child_ele += "</ul></li>"

            ele += child_ele
        except Exception as e:
            print(e)
    ele += "</ul>"
    return mark_safe(ele)


def get_readonly_field_val(field_name, obj_instance):
    field_type = obj_instance._meta.get_field(field_name).get_internal_type()
    if field_type == "ManyToManyField":
        m2m_obj = getattr(obj_instance, field_name)
        return ','.join([i.__str__() for i in m2m_obj.all()])
    return getattr(obj_instance,field_name)