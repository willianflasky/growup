from django.shortcuts import render, HttpResponse

# Create your views here.


def kind(request):
    return render(request, 'kind.html', locals())


def upload_img(request):
    # request.GET.get('dir') 通过这里可以判断上传的文件类型
    print(request.FILES.get('fafafa'))
    # 获取文件数据保存，将存放的路径返回
    #
    import json

    dic = {
        'error': 0,
        'url': "/static/01.jpg",
        'message': ""
    }

    return HttpResponse(json.dumps(dic))