from django.shortcuts import render,HttpResponse
from app01 import models
#
# def create_temp_data(request):
#     for i in range(104,1004):
#         models.UserInfo.objects.create(
#             username='root%s' %i,
#             password="123123",
#             email='root%s@qq.com' %i
#         )
#     return HttpResponse('创建成功')

def users1(request):

    from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
    current_page = request.GET.get('p')
    user_list = models.UserInfo.objects.all()

    paginator = Paginator(user_list,10)
    # per_page: 每页显示条目数量
    # count:    数据总个数
    # num_pages:总页数
    # page_range:总页数的索引范围，如: (1,10),(1,200)
    try:
        page_obj = paginator.page(current_page)
    except EmptyPage as e:
        page_obj = paginator.page(1)
    except PageNotAnInteger as e:
        page_obj = paginator.page(1)
    # has_next              是否有下一页
    # next_page_number      下一页页码
    # has_previous          是否有上一页
    # previous_page_number  上一页页码
    # object_list           分页之后的数据列表
    # number                当前页
    # paginator             paginator对象
    return render(request,'users1.html',{'page_obj':page_obj})


from utils.page import PageInfo

def users2(request):
    all_count = models.UserInfo.objects.all().count()

    page_info = PageInfo(request.GET.get('p'),10,all_count,request.path_info)

    user_list = models.UserInfo.objects.all()[page_info.start():page_info.end()]


    return render(request,'users2.html',{'user_list':user_list,'page_info': page_info})

