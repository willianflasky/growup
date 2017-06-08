from django.shortcuts import render,HttpResponse
from app01 import models
import time
from utils import BaseReponse

def index(request):
    news_list = models.News.objects.all()
    return render(request,'index.html',{'news_list': news_list})

