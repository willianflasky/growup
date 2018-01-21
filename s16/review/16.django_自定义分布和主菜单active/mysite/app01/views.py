from django.shortcuts import render, redirect
from utils.page import PageInfo
# Create your views here.


def app(request):
    page_info = PageInfo(request.GET.get('p'), 6, 100, request.path_info, page_range=7)
    return render(request, 'index.html', locals())
