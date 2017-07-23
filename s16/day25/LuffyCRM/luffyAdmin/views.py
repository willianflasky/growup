from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from luffyAdmin import app_config

# Create your views here.

from luffyAdmin.admin_base import site
print("注册的admin list:", site.registered_admins)


def app_index(request):
    print(site.registered_admins)
    return render(request, 'luffyadmin/app_index.html', {'site': site})


def get_filter_objs(request, admin_class):
    """返回filter的结果queryset"""
    filter_condtions = {}   # {'consultant': '1', 'status': '0'}
    for k,v in request.GET.items():
        # print("-----------:",k,v)
        if k == '_page':continue
        if v:   # valid condtion
            filter_condtions[k] = v
    queryset = admin_class.model.objects.filter(**filter_condtions)
    print('filter con',filter_condtions)
    return queryset,filter_condtions


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

            return render(request,"luffyadmin/model_table_list.html",locals())