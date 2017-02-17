from django.shortcuts import render, HttpResponse
import os
import json
# Create your views here.

def upload(request):
    if request.method == 'POST':
        ret = {'status': False, 'data': None, 'error': None}
        try:
            user = request.POST.get('user')
            # img = request.POST.get('img')
            img = request.FILES.get('img')
            file_path = os.path.join('static', img.name)
            f = open(file_path, 'wb')
            for chunk in img.chunks():
                f.write(chunk)
            f.close()
            ret['status'] = True
            ret['data'] = file_path
        except Exception as e:
            ret['error'] = str(e)
        return HttpResponse(json.dumps(ret))
    return render(request, 'upload.html')


def ajax(request):
    return render(request, 'ajax.html')


def xhr_ajax(request):
    print(request.GET)
    print(request.POST)
    return HttpResponse('ok')


def check_code(request):
    import io
    import random
    i = random.randrange(1, 50)
    request.session['CheckCode'] = i
    # 生成图片,在图片中写内容,内容保存在session中,然后将图片返回给用户.
    # from backend import check_code as CK
    stream = io.BytesIO()
    # img, code = CK.create_validate_code()
    # img.save(stream, 'png')
    # request.session['CheckCode'] = code
    # return HttpResponse(stream.getvalue())


def login(request):
    if request.method == 'POST':
        input_code = request.POST.get('check_code')
        print(input_code.upper(), request.session['CheckCode'].upper())

    return render(request, 'login.html')
