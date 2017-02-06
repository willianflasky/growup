from django.shortcuts import render, HttpResponse
import os
# Create your views here.


def upload(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        # img = request.POST.get('img')
        img = request.FILES.get('img')
        f = open(os.path.join('static', img.name), 'wb')
        for chunk in img.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse("ok")
    return render(request, 'upload.html')


def ajax(request):
    return render(request, 'ajax.html')


def xhr_ajax(request):
    print(request.GET)
    print(request.POST)
    return HttpResponse('ok')
