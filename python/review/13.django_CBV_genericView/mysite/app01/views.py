from django.shortcuts import render, HttpResponse
from django.views.generic import View
from django.views.generic import ListView, DetailView, CreateView
from .models import *


# Create your views here.

class About(View):
    temp = "good day"

    def get(self, request):
        return render(request, 'about.html')

    def post(self, request):
        return HttpResponse(self.temp)


class PublisherList(ListView):
    model = Publisher  # 类属性：指定解析的model
    # queryset = Publisher.objects.all()[0:1]      # 和model二选一，获取指定数据
    context_object_name = 'publishers'  # 默认object_list，前端渲染时的上下文参数
    template_name = 'publisher_list.html'  # 指定渲染的模板文件,默认 'app01/publisher_list.html'

    # 联系类的queryset，而该方法为实例的定制
    # def get_queryset(self):
    #     print(self.request)  # 根据 self.request进行判断，返回符合条件的queryset
    #     return Publisher.objects.all()[0:1]


class PublisherDetial(DetailView):
    model = Publisher
    context_object_name = 'publisher'
    template_name = 'publisher_detail.html'

    def get_context_data(self, **kwargs):  # 继承类的属性，再增加数据
        context = super(PublisherDetial, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context


class PublisherCreate(CreateView):
    model = Publisher
    fields = ['name', 'address', 'city', 'state_province', 'country', 'website']
    template_name = 'publisher_form.html'
    # success_url = reverse_lazy
    # success_message = ""
