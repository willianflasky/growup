#!/usr/bin/env python
#-*- coding: utf-8 -*-
# by Wendy

from django.forms import ModelForm

########################type 动态创建类##########################
"""
>>> type
<class 'type'>
>>> type('MyClass',(object,),{'name':'tangying'})
<class 'MyClass'>
>>>
>>> c = type('MyClass',(object,),{'name':'tangying'})
>>> c
<class 'MyClass'>
>>> c()
<MyClass object at 0x1051efe80>
>>> obj = c()
>>> obj
<MyClass object at 0x1052946a0>
>>> dir(obj)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name']
>>> obj.name
'tangying'


普通创建类的方式
>>> class Foo(object):
...     def func(self):
...             print('hello world')
...
>>> obj = Foo()
>>> obj.func()
hello world

type的方式创建
>>> def func(self):
...     print('hello world')
...
>>> Foo = type('Foo',(object,),{'func':func})
#type 参数1: 类名
#type 参数2: 当前类的基类
#type 参数3: 类的成员
>>> obj = Foo()
>>> obj.func()
hello world

type方式加上 init 构造函数
>>> def func(self):
...     print('hello world')
...
>>> def __init__(self,name,age):
...     self.name = name
...     self.age = age
...
>>> Foo = type('Foo',(object,),{'func':func,'__init__':__init__})
>>> f = Foo("tangying","00")
>>> f.func()
hello world
>>> f.age
'00'
>>> f.name
'tangying'

重点: 类是由type类实例化产生

想重新元类__new__ 重写这个方法

"""

##########################关于元类的自定义#################
'''
重新写了__new__方法(遗忘了。。。。)
class MyType(type):
    def __init__(self,*args,**kwargs):

        print("Mytype __init__",*args,**kwargs)

    def __call__(self, *args, **kwargs):
        print("Mytype __call__", *args, **kwargs)
        obj = self.__new__(self)
        print("obj ",obj,*args, **kwargs)
        print(self)
        self.__init__(obj,*args, **kwargs)
        return obj

    def __new__(cls, *args, **kwargs):
        print("Mytype __new__",*args,**kwargs)
        return type.__new__(cls, *args, **kwargs)

print('here...')
class Foo(object,metaclass=MyType):


    def __init__(self,name):
        self.name = name

        print("Foo __init__")

    def __new__(cls, *args, **kwargs):
        print("Foo __new__",cls, *args, **kwargs)
        return object.__new__(cls)

f = Foo("Alex")
print("f",f)print("fname",f.name)
'''


#########################根据类来生成表单#################
'''
django form类
通模型类的属性映射到数据库的字段一样,表单类的字段会映射到HTML的<input>表单元素
ModelForm通过一个Form映射模型类的字段到HTML表单的<input>元素

Form表单功能
1、自动生成HTML表单元素
2、检查表单数据的合法性
3、如果验证错误,重新显示表单(数据不会重置)

Form相关的对象
widget: 用来渲染成HTML元素的工具
field: form对象中的一个字段
form: 一系列的field对象集合,验证和显示HTML元素
from media : 渲染表单的css和javascript资源

定义Form有两种方式: 参见此项目中的testform
方式一: 直接继承Form
from django import forms

class CustormForm(forms.Form):
    name = forms.CharField(max_length=64)
    qq = forms.CharField(max_length=64)

def customerform(request):
    return render(request,'testform/testform.html',{'form':CustormForm})

方法二:结合model,继承django.forms.ModelForm

from django.forms import ModelForm
from crm import models

class CustomerForm(ModelForm):
    class Meta:
        model = models.Customer
        fields = '__all__'

def customerform(request):
    return render(request, 'testform/testform.html', {'form': CustomerForm})

前端渲染
<form  method="POST">
    {% for field in form %}
        {{ field.name }} {{ field }}
    {% endfor %}
</form>

后端验证
form = CustomerForm(request.POST)
if form.is_valid(): #查看验证是否通过


field属性
{{ field }}  field.lable field.lable_tag field.value field.errors

另外 form_obj

'''



from django.forms import ModelForm


def __new__(cls,*args,**kwargs):
    #print(cls.base_fields,'类的base_fields方法')
    '''
    OrderedDict([('name', <django.forms.fields.CharField object at 0x10b5b67b8>),
    ('qq', <django.forms.fields.CharField object at 0x10b5b6ac8>),
    ('weixin', <django.forms.fields.CharField object at 0x10b5b6d68>),
    ('phone', <django.forms.fields.IntegerField object at 0x10b5b6dd8>),
    .......
    '''
    for field_name in cls.base_fields:
        field = cls.base_fields[field_name]
        #print(field,"field")
        '''
        <django.forms.fields.CharField object at 0x10b5b67b8> field
        <django.forms.fields.CharField object at 0x10b5b6ac8> field
        <django.forms.fields.CharField object at 0x10b5b6d68> field

        widget
        comment = forms.CharField(widget=forms.Textarea)
        '''

        #print(field.widget,'field.widget')
        """
        <django.forms.widgets.TextInput object at 0x10febf828> field.widget
        <django.forms.widgets.TextInput object at 0x10febfb38> field.widget
        """

        attr_dic = {'class': 'form-control'}

        field.widget.attrs.update(attr_dic)

        #print(field.widget.attrs, 'field.widget new 添加一个新的方法 一个样式')
        '''
        {'class': 'form-control'} field.widget new
        {'class': 'form-control'} field.widget new
        {'class': 'form-control'} field.widget new
        '''
    return ModelForm.__new__(cls)


def create_dynamic_modelform(model_class):

    class Meta:
        model = model_class
        fields = "__all__"

    dynamic_modelform = type("DynamicModelForm",
                             (ModelForm,),
                             {'Meta':Meta,'__new__':__new__})

    '''
    就是 用model生成表单的格式
    class DynamicModelForm(ModelForm):
        class Meta:
            model = Customer
            fields = "__all__"

        def __new__(cls,*args,**kwargs):
            .....

    '''
    return dynamic_modelform

    #form_obj = dynamic_modelform(instance=model_obj)
    #类似于 form_obj = CustomerForm(request.POST)

