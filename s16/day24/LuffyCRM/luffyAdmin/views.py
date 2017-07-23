from django.shortcuts import render,HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from luffyAdmin import app_config

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
        if k == '_page':
            continue
        if v:   # 当条件有效果,将K,V增加到字典中
            filter_condtions[k] = v
    queryset = admin_class.model.objects.filter(**filter_condtions)  # 去表里查数据
    return queryset, filter_condtions


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
