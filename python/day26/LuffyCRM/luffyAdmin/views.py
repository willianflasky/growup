from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from luffyAdmin import app_config
from luffyAdmin import forms
# Create your views here.

from luffyAdmin.admin_base import site
print("注册的admin list:",site.registered_admins)

def app_index(request):

    return render(request,'luffyadmin/app_index.html',{'site':site})

def get_filter_objs(request,admin_class):
    """返回filter的结果queryset"""
    filter_condtions = {}
    for k,v in request.GET.items():
        #print(k,v)
        if k in ['_page','_q','_o']:
            continue
        if v:#valid condtion
            filter_condtions[k] = v
    queryset = admin_class.model.objects.filter(**filter_condtions).order_by('-id')
    print('filter con', filter_condtions)
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


def get_orderby_objs(request,querysets):
    """
    排序
    1.获取_o的值
    2.调用order_by(_o的值)
    3.处理正负号，来确定下次的排序的顺序
    4.返回
    :param request:
    :param querysets:
    :return:
    """
    orderby_key = request.GET.get('_o') #-id
    last_orderby_key = orderby_key or ''
    if orderby_key:
        order_column = orderby_key.strip('-')
        order_results = querysets.order_by(orderby_key)
        # new_order_key =
        # if request.GET.get('_page'):#代表有分页，不对_o的值取反
        #     print("不取反",orderby_key)
        #     new_order_key = orderby_key
        # else:
        if orderby_key.startswith('-'):
            new_order_key = orderby_key.strip('-')
        else:
            new_order_key = "-%s"% orderby_key

        return order_results,new_order_key,order_column,last_orderby_key
    else:
        return querysets,None,None,last_orderby_key


def model_table_list(request, app_name, model_name):
    """
    1. 拿到表对象，取出表里的数据
    2. 拿到此表对应的admin class，
    :param request:
    :param app_name:
    :param model_name:
    :return:
    """

    if app_name in site.registered_admins:
        if model_name in site.registered_admins[app_name]:
            admin_class = site.registered_admins[app_name][model_name]
            # print("--model class",model_class,locals())
            querysets,filter_conditions = get_filter_objs(request,admin_class)
            querysets, q_val = get_search_objs(request, querysets, admin_class)
            querysets,new_order_key,order_column,last_orderby_key= get_orderby_objs(request,querysets)

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


def table_obj_change(request,app_name,model_name,object_id):
    if app_name in site.registered_admins:
        if model_name in site.registered_admins[app_name]:
            admin_class = site.registered_admins[app_name][model_name]
            object = admin_class.model.objects.get(id=object_id)
            form = forms.create_dynamic_modelform(admin_class.model)
            if request.method == "GET":
                form_obj = form(instance=object)
            elif request.method == "POST":
                form_obj = form(instance=object,data=request.POST)
                if form_obj.is_valid():
                    form_obj.save()

    return render(request,'luffyadmin/table_object_change.html',locals())


def table_obj_add(request,app_name,model_name):
    print("requestpath", request.path)
    if app_name in site.registered_admins:
        if model_name in site.registered_admins[app_name]:
            admin_class = site.registered_admins[app_name][model_name]

            form = forms.create_dynamic_modelform(admin_class.model)
            if request.method == "GET":
                form_obj = form()
            elif request.method == "POST":
                form_obj = form(data=request.POST)
                if form_obj.is_valid():
                    form_obj.save()

                    return redirect(request.path.rstrip("add/"))

    return render(request, 'luffyadmin/table_object_add.html', locals())