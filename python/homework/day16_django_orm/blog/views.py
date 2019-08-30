from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from blog.models import *
from functools import wraps
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import time
# Create your views here.


def auth(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        username = request.COOKIES.get('username', "")
        if username:
            return func(request, username, **kwargs)
        else:
            return redirect('/')
    return wrapper


def login(request):
    username = request.COOKIES.get('username', "")
    if username:
        return redirect('/blog/')

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        ret = User.objects.filter(username=username).values('username', 'password')
        # <QuerySet [{'password': '123123', 'username': 'alex'}]>
        if ret.exists():
            if ret[0]['username'] == username and ret[0]['password'] == password:
                response = HttpResponseRedirect('/blog/')
                response.set_cookie('username', username, 3600)
                return response
            else:
                # 数据库中查到用户,但是密码不用
                return redirect("/blog/login/")
        else:
            # 数据库中没有查到用户
            return redirect("/blog/login/")

    return render(request, 'login.html')


@auth
def blog(request, *args, **kwargs):
    username = args[0]

    total_list = []
    objs = Artical.objects.all()

    for obj in objs:
        one_dict = {}
        one_dict['publish_username'] = obj.user.username
        one_dict['title'] = obj.title
        one_dict['text'] = obj.text
        one_dict['date'] = obj.date
        one_dict['id'] = obj.id
        tmp = []
        for line in obj.author.filter().values('name'):
            tmp.append(line['name'])
        one_dict['author_name'] = ";".join(tmp)
        total_list.append(one_dict)

    paginator = Paginator(total_list, 3)
    page = request.GET.get('p')
    try:
        info_obj = paginator.page(page)
    except PageNotAnInteger:
        info_obj = paginator.page(1)
    except EmptyPage:
        info_obj = paginator.page(paginator.num_pages)

    return render(request, 'blog.html', locals())


@auth
def detail(request, *args, **kwargs):
    username = args[0]
    num = kwargs['num']
    obj = Artical.objects.filter(id=num)[0]
    author_list = Artical.objects.filter(id=num).values("author__name", "author__city")
    return render(request, "detail.html", locals())


def logout(request):
    response = render(request, 'login.html')
    response.delete_cookie('username')
    return response


@auth
def append(request, *args, **kwargs):
    username = args[0]
    if request.method == 'POST':
        if request.GET.get('p') == "1":
            author_name = request.POST.get('author_name')
            author_age = request.POST.get('author_age')
            author_city = request.POST.get('author_city')
            if len(author_name) == 0 or len(author_age) == 0 or len(author_city) == 0:
                return HttpResponse("字段不能为空")
            Author.objects.create(name=author_name, age=author_age, city=author_city)

        elif request.GET.get('p') == '2':
            artical_title = request.POST.get('artical_title')
            artical_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            artical_text = request.POST.get('artical_text')
            if len(artical_title) == 0 or len(artical_date) == 0 or len(artical_text) == 0:
                return HttpResponse("字段不能为空")
            user_id = User.objects.filter(username=username).values('id')[0]
            Artical.objects.create(title=artical_title, date=artical_date, text=artical_text, user_id=user_id['id'])

        elif request.GET.get('p') == '3':
            artical_title = request.POST.get('artical_title')
            author_name = request.POST.get('author_name')

            ART = Artical.objects.filter(title=artical_title)    # Queryset对象
            author_id = Author.objects.filter(name=author_name)  # Queryset对象
            if ART.exists() and author_id.exists():
                ART[0].author.add(author_id[0])
            else:
                return HttpResponse("文章或者作者不存在!")
    return render(request, 'append.html', locals())
