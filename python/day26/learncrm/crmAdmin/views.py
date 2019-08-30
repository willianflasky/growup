from django.shortcuts import render,redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q
from crmAdmin import forms
#动态生成表单

from crmAdmin import app_config
#这个地方其实就是把所有的注册的都执行一遍,自动拿出 所有app 的 admin 中 已经注册的  models 牛掰~!!!
#并且不会重复执行,因为python的import只会执行一次

from crmAdmin.admin_base import site
print("注册的admin list",site.registered_admins)
# Create your views here.



def app_index(request):
    return render(request,'crmadmin/app_index.html',{'site':site})


def get_filter_objs(request,admin_class):
    """
    返回filter的结果queryset
    url仿照admind的 filter的 get请求
    """
    filter_condtions = {}
    for k,v in request.GET.items():
        if k in ['_page','_q','_o','_action']:
            continue
        if v:
            filter_condtions[k] = v

    queryset = admin_class.model.objects.filter(**filter_condtions).order_by('-id')
    #其实就是models.Customer.filter(条件字典),这样排序方便新建的item在最前面
    """
    modles.Customer.objects.filter()
    <QuerySet [<Customer: tangying1>, <Customer: tangying2>, <Customer: wendy1>, <Customer: wendy2>, <Customer: anni1>, <Customer: anni2>, <Customer: gaga1>, <Customer: gaga2>, <Customer: park1>, <Customer: park2>, <Customer: linkin1>, <Customer: linkin2>, <Customer: start1>, <Customer: start2>, <Customer: stone1>, <Customer: stone2>]>

    """
    return queryset,filter_condtions


def get_search_objs(request,querysets,admin_class):
    """
    1、拿到_q的值
    2、拼接Q查询条件
    3、调用filter(Q条件)查询
    4、返回查询结果
    :param request:请求
    :param querysets: filter的querysets
    :param admin_class: search_field
    :return:
    """
    q_val = request.GET.get('_q') #None
    if q_val:
        '''
        >>> from django.db.models import Q
        >>> Q(qq__contains='23')
        <Q: (AND: ('qq__contains', '23'))>
        >>> q = Q(qq__contains='23')
        >>> q
        <Q: (AND: ('qq__contains', '23'))>
        >>> models.Customer.objects.filter(q)
        <QuerySet [<Customer: tangying2>, <Customer: wendy1>, <Customer: wendy2>, <Customer: anni1>, <Customer: anni2>, <Customer: gaga2>, <Customer: park1>, <Customer: park2>, <Customer: linkin1>, <Customer: linkin2>, <Customer: start1>, <Customer: start2>, <Customer: stone1>, <Customer: stone2>]>
        >>>

        >>> q =  Q(qq__contains='QQ') | Q(source__name__contains='QQ')
        >>> q
        <Q: (OR: ('qq__contains', 'QQ'), ('source__name__contains', 'QQ'))>
        >>> models.Customer.objects.filter(q)
        <QuerySet [<Customer: tangying2>, <Customer: anni1>, <Customer: anni2>, <Customer: gaga1>, <Customer: park1>, <Customer: park2>, <Customer: linkin1>, <Customer: linkin2>, <Customer: start1>, <Customer: start2>, <Customer: stone1>, <Customer: stone2>]>
        >>>

        自动拼接查询条件
        >>> q1 = Q()
        >>> q1.connector
        'AND'
        >>> q1.connector = 'OR'
        >>> q1.children.append(('qq__contains','QQ'))
        >>> q1.children.append(('source__name__contains','QQ'))
        >>> q1
        <Q: (OR: ('qq__contains', 'QQ'), ('source__name__contains', 'QQ'))>
        '''
        q_obj = Q()
        q_obj.conntor = "OR"
        for search_field in admin_class.search_fields:
            q_obj.children.append(("%s__contains" %search_field,q_val))
        print("search obj",q_obj)

        search_results = querysets.filter(q_obj)
    else:
        search_results = querysets

    return  search_results,q_val  #返回查询条件这样刷新页面的时候还能带上


def get_order_objs(request,querysets):
    """
    排序
    1、获取_o的值
    2、调用order_by(_o的值)
    3、处理正负号,来确定下次的排序的顺序
    4、返回
    :param request:
    :param querysets:
    :return:
    """
    orderby_key = request.GET.get('_o') #-id
    last_orderby_key = orderby_key or '' #当前访问的的排序key 和 是否有排序

    if orderby_key: #如果有排序访问过来
        order_column = orderby_key.strip('-')
        order_results = querysets.order_by(orderby_key)
        #排序结果

        if orderby_key.startswith('-'):
            new_order_key = orderby_key.strip('-')
        else:
            new_order_key = "-%s" % orderby_key

        #有- 代表有排序查询过来,新查询就是正的 上下的三角, 没有代表第一次来就是下三角

        return order_results,new_order_key,order_column,last_orderby_key
        #排序结果,新排序是正负,排序的字段,最后的key或者是否有排序
    else:
        return  querysets,None,None,last_orderby_key


def model_table_list(request,app_name,model_name):
    """
    1、拿到表对象,取出表中的数据
    2、拿到此表对应的amdin class,
    :param request:
    :param app_name:
    :param model_name:
    :return:
    """
    if app_name in site.registered_admins:
        #判断url中的app name 是否在registered admins中
        if model_name in site.registered_admins[app_name]:
            #registered_admins 字典
            admin_class = site.registered_admins[app_name][model_name]
            ##因为admin_class 里面有list filter

            if request.method == 'GET':

                querysets,filter_conditions = get_filter_objs(request,admin_class)
                #过滤的查询结果

                querysets,q_val = get_search_objs(request,querysets,admin_class)
                #查询的查询结果,在过滤之后的

                querysets,new_order_key,order_column,last_orderby_key = get_order_objs(request,querysets)
                #排序在查询过滤之后

                paginator = Paginator(querysets,admin_class.list_per_page)
                page = request.GET.get('_page')
                try:
                    querysets = paginator.page(page)
                except PageNotAnInteger:
                    #第一页
                    querysets = paginator.page(1)
                except EmptyPage:
                    #最后一页
                    querysets = paginator.page(paginator.num_pages)

            elif request.method == 'POST':
                print(request.POST)
                Dictrequest = dict(request.POST)
                action = request.POST.get('_action')

                if action != '_delete_selected':

                    select_obj_action(Dictrequest,request, admin_class)

                    return redirect(request.path)

                else:

                    print('---------------------')
                    object_id = Dictrequest.get('_selected_action')
                    object_id_count = len(object_id)
                    querysets = admin_class.model.objects.get(id__in=object_id)

                    return render(request,'crmadmin/model_obj_del.html', locals())

            return render(request, 'crmadmin/model_table_list.html', locals())


def select_obj_action(Dictrequest,request,admin_class):

    '''
    这样取是因为单纯的querydic有问题取不出列表
    '''
    object_id = Dictrequest.get('_selected_action')
    print(object_id, type(object_id))

    querysets = admin_class.model.objects.filter(id__in=object_id)
    '''
    >>> models.Customer.objects.filter(id__in=['16','15']);
        <QuerySet [<Customer: stone1>, <Customer: stone2>]>
    '''
    # print(object,object_id,action)
    # print(admin_class,request,object)
    action = request.POST.get('_action')
    func_action = getattr(admin_class,action)
    func_action(site,request,querysets)
    #admin_class.status(site, request, querysets)


def table_obj_change(request,app_name,model_name,object_id):
    if app_name in site.registered_admins:
        if model_name in site.registered_admins[app_name]:
            #判断urlpath路径正确
            admin_class = site.registered_admins[app_name][model_name]
            #拿到admin_class model filter_horizontal ...
            object = admin_class.model.objects.get(id=object_id)
            #拿到前端需要看详细的那条数据记录
            form = forms.create_dynamic_modelform(admin_class.model)
            """
            admin_class
                model = admin_class.models.customer
            """

            if request.method == 'GET':
                form_obj = form(instance=object)

                '''
                class CustomerForm(ModelForm):
                    class Meta:
                        model = models.Customer
                        fields = '__all__'

                def customerform(request):
                    object = models.Customer.objects.filter(id=1).get()  #必须要是get 不然不能当字典传递进去
                    form_obj = CustomerForm(instance=object)
                    return render(request, 'testform/testform.html', {'form': form_obj})
                    前端就能显示出来了 见testform

                    页面非常丑,所以写把格式写进去 __new__
                '''


            elif request.method == 'POST':
                #print(request.POST,'提交数据')
                # print(object,'instance')
                '''
                <QueryDict: 'name': ['tangying1'], 'qq': ['38346812'], ....}>
                tangying1 实例
                '''

                form_obj = form(instance=object,data=request.POST)
                # 有这个实力就更新,没有这个实例就创建
                '''
                这个方法根据表单绑定的数据创建并保存数据库对象。模型表单的子类可以用关键字参数instance 接收一个已经存在的模型实例；
                如果提供，save() 将更新这个实例。如果没有提供，save() 将创建模型的一个新实例：
                >>> from myapp.models import Article
                >>> from myapp.forms import ArticleForm

                # Create a form instance from POST data.
                >>> f = ArticleForm(request.POST)

                # Save a new Article object from the form's data.
                >>> new_article = f.save()

                # Create a form to edit an existing Article, but use
                # POST data to populate the form.
                >>> a = Article.objects.get(pk=1)
                >>> f = ArticleForm(request.POST, instance=a)
                >>> f.save()

                '''
                if form_obj.is_valid():
                    form_obj.save()

            return render(request,'crmadmin/table_object_change.html',locals())


def table_obj_add(request,app_name,model_name):
    if app_name in site.registered_admins:
        if model_name in site.registered_admins[app_name]:
            #判断urlpath路径正确
            admin_class = site.registered_admins[app_name][model_name]
            #拿到admin_class model filter_horizontal ...

            form = forms.create_dynamic_modelform(admin_class.model)
            """
            admin_class
                model = admin_class.models.customer
            """

            if request.method == 'GET':
                form_obj = form()

                '''
                class CustomerForm(ModelForm):
                    class Meta:
                        model = models.Customer
                        fields = '__all__'

                def customerform(request):
                    form_obj = CustomerForm()
                '''

            elif request.method == 'POST':
                #print(request.POST,'提交数据')
                '''
                <QueryDict: 'name': ['tangying1'], 'qq': ['38346812'], ....}>
                '''
                form_obj = form(data=request.POST)
                # 创建实例
                if form_obj.is_valid():
                    form_obj.save()

                    return redirect(request.path.rstrip('add/'))

            return render(request,'crmadmin/table_object_add.html',locals())