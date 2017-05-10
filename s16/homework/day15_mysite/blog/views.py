from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django import forms
from blog.models import *
from functools import wraps
# Create your views here.


class BookForm(forms.Form):
    id = forms.CharField(required=False)
    title = forms.CharField(required=True)
    author = forms.CharField(required=True)
    price = forms.CharField(required=True)
    pub_date = forms.CharField(required=True)


def auth(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        username = request.COOKIES.get('username', "")
        if username:
            return func(request, username, **kwargs)
        else:
            return redirect('/blog/login/')
    return wrapper


def index(request):
    return redirect('/blog/')


def login(request):
    _user = request.COOKIES.get('username', "")
    if _user:
        return redirect('/blog/')

    if request.method == 'POST':
        _user = request.POST.get('username')
        _pass = request.POST.get('password')
        if _user == 'alex' and _pass == '123':
            # obj = render(request, 'login.html')
            # obj.set_cookie('username', _user, 3600)
            response = HttpResponseRedirect('/blog/')
            response.set_cookie('username', _user, 3600)
            return response
        else:
            return HttpResponseRedirect('/blog/login')
    return render(request, 'login.html')


def logout(request):
    response = render(request, 'logout.html')
    response.delete_cookie('username')
    return response


@auth
def show_data(request, *args, **kwargs):
    # username = request.COOKIES.get('username', "")
    # if username:
    #     all_books = Books.objects.all()
    #     return render(request, 'index.html', locals())
    # else:
    #     return redirect('/blog/login/')
    username = args[0]
    all_books = Books.objects.all()
    return render(request, 'index.html', locals())


def add_books(request):
    # if request.method == 'POST':
    if request.POST:
        bf = BookForm(request.POST)
        if bf.is_valid():
            title = bf.cleaned_data['title']
            author = bf.cleaned_data['author']
            price = bf.cleaned_data['price']
            pub_date = bf.cleaned_data['pub_date']
            Books.objects.create(title=title, author=author, price=price, pub_date=pub_date)
            return redirect('/blog/')
    return render(request, 'add_books.html')


def del_books(request):
    nid = request.GET.get('id')
    Books.objects.filter(id=nid).delete()
    return redirect('/blog/')


def edit_books(request):
    if request.POST:
        ebf = BookForm(request.POST)
        if ebf.is_valid():
            nid = ebf.cleaned_data['id']
            title = ebf.cleaned_data['title']
            author = ebf.cleaned_data['author']
            price = ebf.cleaned_data['price']
            pub_date = ebf.cleaned_data['pub_date']
            # b = request.GET.get(nid)
            # b.price=price
            # b.save()  # 效率低
            Books.objects.filter(id=nid).update(id=nid, title=title, author=author, price=price, pub_date=pub_date)
    return redirect('/blog/')
