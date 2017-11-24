from django.shortcuts import render, redirect
from app01.myforms import hosts_form
from app01.models import *


def index(request):
    data = hosts.objects.all()
    return render(request, 'index.html', locals())


def add(request):
    if request.method == 'POST':
        form = hosts_form(request.POST)
        if form.is_valid():
            hosts.objects.create(**form.cleaned_data)
            return redirect('/')
    else:
        form = hosts_form()
        return render(request, 'add.html', locals())
