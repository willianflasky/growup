#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from django.forms import ModelForm


# def CustomerForm(ModelForm):
#
#     class Meta:
#         model = model.Customer
#         fields = '__all__'


# 通过new来增加属性
def __new__(cls, *args, **kwargs):
    # base_fields拿到表的字段名
    for filed_name in cls.base_fields:
        # 通过字段名拿到字段对象
        field = cls.base_fields[filed_name]
        # 定义好的属性
        attr_dic = {# 'placeholder': field.help_text,
                    'class': 'form-control'
        }
        # 增加到里面
        field.widget.attrs.update(attr_dic)
    #     运行完自己的__new__,再运行父类的__new__
    return ModelForm.__new__(cls)


# 定义函数
def create_dynamic_modelform(model_class):

    # 定义一个类
    class Meta:
        # 表名
        model = model_class
        # 显示所有字段
        fields = "__all__"

    # 动态生成类,
    dynamic_modelform = type('DynamicModelForm',    # 类名
                             (ModelForm,),          # 继承
                             {'Meta': Meta, '__new__': __new__},)        # 传值,属性

    return dynamic_modelform

