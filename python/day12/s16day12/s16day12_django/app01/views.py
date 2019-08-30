from django.shortcuts import render,HttpResponse

# Create your views here.


def index(request):
    # print("提交方式：",request.method)
    # print("POST方式数据：",request.POST)
    # print("GET方式数据：",request.GET)

    obj = request.FILES.get('fafafa')

    f = open(obj.name,'wb')
    for chunk in obj.chunks():
        f.write(chunk)
    f.close()

    return HttpResponse('提交成功')