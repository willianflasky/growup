from luffyAdmin import  permissions
from django.core.urlresolvers import resolve

from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.conf import settings

def perm_check(*args,**kwargs):
    """
    1.判断用户是否已认证
        1.1 根据原生url 获取到 相对的 url_name
        1.2 根据url_name 循环 permission_dic , 找到对应的权限条目
            1.2.1 判断 request.method ,请求参数 都匹配上
            1.2.2 取得 最终对应的权限条目
            1.2.3 判断用户 是否有这条权限
            1.2.4 如果有，放行
            1.2.5 没有 返回403
        1.3 找不到权限条目， 403
    2. 没登录，拒绝
    :return:
    """

    request = args[0]
    resolve_url_obj = resolve(request.path)
    print("resolve ",resolve_url_obj)
    current_url_name = resolve_url_obj.url_name  # 当前url的url_name
    print('---perm:',request.user,request.user.is_authenticated(),current_url_name)
    #match_flag = False
    match_key = None
    match_results = [None]
    if not request.user.is_authenticated():
         return redirect(settings.LOGIN_URL)

    for permission_key,permission_val in  permissions.perm_dic.items():

        perm_url_name = permission_val[0]
        perm_method = permission_val[1]
        perm_args = permission_val[2]
        perm_kwargs = permission_val[3]
        custom_func_hook = None if len(permission_val) == 4 else permission_val[4]

        if perm_url_name == current_url_name: #matches current request url
            if perm_method == request.method: #matches request method
                #if not perm_args: #if no args defined in perm dic, then set this request to passed perm
                    #逐个匹配参数，看每个参数时候都能对应的上。
                args_matched = False #for args only
                for item in perm_args:
                    request_method_func = getattr(request,perm_method) #GET or POST
                    if request_method_func.get(item,None):# request字典中有此参数
                        args_matched = True
                    else:
                        print("arg not match......")
                        args_matched = False
                        break  # 有一个参数不能匹配成功，则判定为假，退出该循环。
                else:
                    args_matched = True
                #匹配有特定值的参数
                kwargs_matched = False
                for k,v in perm_kwargs.items():
                    request_method_func = getattr(request, perm_method)
                    arg_val = request_method_func.get(k, None)  # request字典中有此参数
                    print("perm kwargs check:",arg_val,type(arg_val),v,type(v))
                    if arg_val == str(v): #匹配上了特定的参数 及对应的 参数值， 比如，需要request 对象里必须有一个叫 user_id=3的参数
                        kwargs_matched = True
                    else:
                        kwargs_matched = False
                        break # 有一个参数不能匹配成功，则判定为假，退出该循环。
                else:
                    kwargs_matched = True

                func_hook_passed = False
                if custom_func_hook: #设置了自定义函数
                    func_res = custom_func_hook(request,*args,**kwargs)
                    if func_res:
                        func_hook_passed = True


                match_results = [args_matched,kwargs_matched,func_hook_passed]
                print("--->match_results ", match_results)
                if all(match_results): #都匹配上了
                    match_key = permission_key
                    break


    if all(match_results): #要确定循环是因为匹配上然后跳出了，还是循环结束了，但没有匹配上
        app_name, *perm_name = match_key.split('_')
        print("--->matched ",match_results,match_key)
        print(app_name, *perm_name)
        perm_obj = '%s.%s' % (app_name,match_key)
        print("perm str:",perm_obj)
        if request.user.has_perm(perm_obj):
            print('当前用户有此权限')
            return True
        else:
            print('当前用户没有该权限')
            return False

    else:
        print("未匹配到权限项，当前用户无权限")

def check_permission(func):

    def wrapper(*args,**kwargs):
        print('wrapper',func,args,kwargs)
        request = args[0]
        if perm_check(*args,**kwargs):
            return func(*args,**kwargs) #  app_index(request):
        else:
            return render(request,'luffyadmin/403.html')
    return wrapper




