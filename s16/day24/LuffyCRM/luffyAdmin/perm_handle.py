#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.core.urlresolvers import resolve
from luffyAdmin import permissions
from LuffyCRM import settings


def perm_check(*args, **kwargs):
    """
    1.判断用户登录
        1.1 根据原生URL, 获取到相对的URL_NAME
        1.2 根据URL_name循环permission_dic,找到对应的权限条目
            1.2.1 判断request.method,请求参数都匹配上
            1.2.2 取得最终对应的权限条目
            1.2.3 判断用户是否有这台权限
            1.2.4 如果有放行,
            1.2.5 如果没有403
        1.3 找不到权限条目 403
    2.没有登录,拒绝

    :return:
    """
    request = args[0]
    resolve_url_obj = resolve(request.path)     # 通过URL转换成别名
    current_url_name = resolve_url_obj.url_name     # 别名
    match_key = None
    match_result = [None]
    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)

    for permission_key, permission_val in permissions.perm_dic.items():
        perm_url_name = permission_val[0]
        perm_method = permission_val[1]
        perm_args = permission_val[2]
        perm_kwargs = permission_val[3]
        custom_func_hook = None if len(permission_val) == 4 else permission_val[4]

        if perm_url_name == current_url_name:       # url
            if perm_method == request.method:       # get or post
                args_matched = False
                for item in perm_args:
                    request_method_func = getattr(request, perm_method)
                    if request_method_func.get(item, None):
                        args_matched = True
                    else:
                        args_matched = False
                    break
                else:
                    args_matched = True     # 列表里没有参数,直接为真

                kwargs_metched = False
                for k, v in perm_kwargs.items():
                    request_method_func = getattr(request, perm_method)
                    arg_val = request_method_func.get(k, None)
                    if arg_val == str(v):
                        kwargs_metched = True
                    else:
                        break
                else:
                    kwargs_metched = True

                func_hook_passed = False
                if custom_func_hook:
                    func_res = custom_func_hook(request, *args, **kwargs)
                    if func_res:
                        func_hook_passed = True

                match_result = [args_matched, kwargs_metched, func_hook_passed]
                if all(match_result):
                    match_key = permission_key      # 赋值
                    break

    if all(match_result):
        app_name, *per_name = match_key.split('_')      # ["crm"] ["table","index"]
        perm_obj = "%s.%s" % (app_name, match_key)      # crm.crm_table_index
        if request.user.has_perm(perm_obj):
            return True
        else:
            return False


def check_permission(func):
    def wrapper(*args, **kwargs):
        request = args[0]
        if perm_check(*args, **kwargs):
            return func(*args, **kwargs)
        else:
            return render(request, 'luffyadmin/403.html', locals())
    return wrapper

