#### 基于类的视图

```
#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

from django.shortcuts import HttpResponse
from django import http
from django.utils import six
from django.utils.decorators import classonlymethod
from django.conf.urls import url

class View(object):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

    def __init__(self, **kwargs):
        for key, value in six.iteritems(kwargs):
            setattr(self, key, value)

    @classonlymethod
    def as_view(cls, **initkwargs):
        for key in initkwargs:
            if key in cls.http_method_names:
                raise TypeError("禁止 %s 作为 %s()关键字参数" % (key, cls.__name__))
            if not hasattr(cls, key):
                raise TypeError("类 %s() 接收到非法参数 %s，只接受类存在类属性" % (cls.__name__, key))

        def view(request, *args, **kwargs):
            # 把 as_view()传入的关键字参数，赋值为相应的类变量
            self = cls(**initkwargs)  # 类的实例化，虽然只是一行代码，要理解原理：是有很多行代码执行完的结果
            if hasattr(self, 'get') and not hasattr(self, 'head'):
                self.head = self.get
            self.request = request
            self.args = args
            self.kwargs = kwargs
            return self.dispatch(request, *args, **kwargs)  # 一行代码，代表的是self.dispatch()的执行结果

        # 函数也是一种对象，可以有自己的属性****
        view.view_class = cls
        view.view_initkwargs = initkwargs

        # 返回闭合的函数对象
        return view

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)   # 一行代码，代表的是handler()的执行结果
    """最终dispatch结果：根据request.method.lower()得到相应的http请求方法，反射到同名类方法，执行"""

    def http_method_not_allowed(self, request, *args, **kwargs):
        return http.HttpResponseNotAllowed(self._allowed_methods())

    def _allowed_methods(self):
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]


class MyView(View):
    def get(self, request):
        return HttpResponse('get it')

    def post(self, request):
        return HttpResponse('post it')

    def head(self, request):
        return HttpResponse('head it')

urlpatterns = [
    url(r'^my_view/', MyView.as_view()),
]

吃透类View

```

#### 通用视图
*   ListView
*   DetailView
*   FormView
*   CreateView
*   UpdateView
*   DeleteView


文档
>   http://www.cnblogs.com/jonathan1314/p/7545298.html

>   https://docs.djangoproject.com/en/2.0/ref/class-based-views/