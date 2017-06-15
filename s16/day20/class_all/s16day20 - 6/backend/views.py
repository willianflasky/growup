from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def order(request):
    return render(request, 'order.html')

def host(request):
    return render(request, 'host.html')


def user(request):
    return render(request, 'user.html')

def news(request):
    if request.method == 'GET':
        return render(request, 'news.html')
    else:
        pass