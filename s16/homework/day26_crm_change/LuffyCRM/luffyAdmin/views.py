from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from luffyAdmin import app_config
from luffyAdmin import forms

# Create your views here.

from luffyAdmin.admin_base import site
print("注册的admin list:", site.registered_admins)


# http://127.0.0.1:8000/luffyadmin/  显示项目名和对应的表名
def app_index(request):
    return render(request, 'luffyadmin/app_index.html', {'site': site})


def get_filter_objs(request, admin_class):
    """返回filter的结果queryset"""
    filter_condtions = {}  # 过滤条件: 是个字典{'consultant': '1', 'status': '0'}
    for k, v in request.GET.items():
        if k in ['_page', '_q', '_o']:
            continue
        if v:   # 当条件有效果,将K,V增加到字典中
            filter_condtions[k] = v
    queryset = admin_class.model.objects.filter(**filter_condtions).order_by('-id')  # 去表里查数据
    return queryset, filter_condtions


def get_search_objs(request, querysets, admin_class):
    """
    1.拿到_q的值
    2.拼接Q查询条件
    3.调用filter(Q条件)查询
    4.返回查询结果
    :param request:
    :param querysets:
    :param admin_class:
    :return:
    """
    q_val = request.GET.get('_q')   # None      第一步_q拿值
    if q_val:
        q_obj = Q()         # 生效Q对象
        q_obj.connector = "OR"      # 默认值是AND,改成OR
        for search_field in admin_class.search_fields:      # 循环search_fields
            q_obj.children.append(("%s__contains" % search_field, q_val))   # 把值加到Q对象中. 第二步
        print("serach obj", q_obj)

        search_results = querysets.filter(q_obj)     # 第三步:过滤结果
    else:
        search_results = querysets      # 如果_q值为空, 直接返回原值

    return search_results, q_val


def get_orderby_objs(request, querysets):
    """
        1. 获取_o值
        2. 调用order_by
        3. 处理正负号, 来确定
        4. 返回
    """
    # 获取_o的值
    orderby_key = request.GET.get('_o')
    last_orderby_key = orderby_key or ""
    # 如果有值
    if orderby_key:
        # 脱掉-,拿到字段
        order_column = orderby_key.strip('-')
        # 查询querysets
        order_result = querysets.order_by(orderby_key)

        # 返回数据
        if orderby_key.startswith('-'):
            # orderby_key的反值
            new_order_key = orderby_key.strip('-')
        else:
            # orderby_key的反值
            new_order_key = "-%s" % orderby_key
        #   order_result:排序后的querysets, new_order_key:字段值,与前相反(id,-id), order_column:字段名, id
        return order_result, new_order_key, order_column, last_orderby_key
    else:
        # 没有值,返回原值
        return querysets, None, None, last_orderby_key


def model_table_list(request, app_name, model_name):
    """
    1. 拿到表对象，取出表里的数据
    2. 拿到此表对应的admin class，
    :param request:
    :param app_name:       APP名字
    :param model_name:      表类
    :return:
    """
    # site.registered_admins是所有的数据,大字典. 判断APP_NAME是否在大字典中
    if app_name in site.registered_admins:
        # 如果APP在大字典中, 再判断"表类"在没在这个APP里
        if model_name in site.registered_admins[app_name]:
            # 拿到管理类
            admin_class = site.registered_admins[app_name][model_name]
            # print("--model class",model_class,locals())
            # querysets从DB里查询的结果, filter_conditions = {'consultant': '1', 'status': '0'}
            querysets, filter_conditions = get_filter_objs(request, admin_class)
            # 处理搜索函数
            querysets, q_val = get_search_objs(request, querysets, admin_class)
            # 排序
            querysets, new_order_key, order_column, last_orderby_key = get_orderby_objs(request, querysets,)
            # django版本分页
            paginator = Paginator(querysets, admin_class.list_per_page)  # Show 25 contacts per page
            page = request.GET.get('_page')
            try:
                querysets = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                querysets = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                querysets = paginator.page(paginator.num_pages)

            return render(request, "luffyadmin/model_table_list.html", locals())
    else:   # 没有的APP名字
        return HttpResponse("没有:%s" % app_name)


# app_name= crm     model_name = customer       object_id = 1
def table_obj_change(request, app_name, model_name, object_id):
    # 如果crm在这个字典中
    if app_name in site.registered_admins:
        # 再如果表在这个内层字典中      {'crm':{'customer':admin_class}}
        if model_name in site.registered_admins[app_name]:
            # 获取到admin_class (这就是管理类, 同时表也存在属性里admin_class.model)
            admin_class = site.registered_admins[app_name][model_name]
            # 去表中获取数据,通过ID
            data_obj = admin_class.model.objects.get(id=object_id)
            # 动态类,实例化
            form = forms.create_dynamic_modelform(admin_class.model)

            if request.method == 'GET':
                # 将数据放入这个实例中, 将form_obj返回给前端.
                form_obj = form(instance=data_obj)
            elif request.method == 'POST':
                form_obj = form(instance=data_obj, data=request.POST)
                if form_obj.is_valid():
                    form_obj.save()

    return render(request, 'luffyadmin/table_object_change.html', locals())


def table_obj_add(request, app_name, model_name):
    if app_name in site.registered_admins:
        # 再如果表在这个内层字典中      {'crm':{'customer':admin_class}}
        if model_name in site.registered_admins[app_name]:
            # 获取到admin_class (这就是管理类, 同时表也存在属性里admin_class.model)
            admin_class = site.registered_admins[app_name][model_name]

            # 动态类,实例化
            form = forms.create_dynamic_modelform(admin_class.model)
            if request.method == 'GET':
                form_obj = form()
            elif request.method == 'POST':
                form_obj = form(data=request.POST)
                if form_obj.is_valid():
                    form_obj.save()
                    return redirect(request.path.rstrip('add/'))

    return render(request, 'luffyadmin/table_object_add.html', locals())
