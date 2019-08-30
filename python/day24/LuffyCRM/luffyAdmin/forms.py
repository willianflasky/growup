#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from django.forms import ModelForm,forms


# 通过new来增加属性
def __new__(cls, *args, **kwargs):
    # base_fields拿到表的字段名
    for filed_name in cls.base_fields:
        # 通过字段名拿到字段对象
        field = cls.base_fields[filed_name]
        # 定义好的属性
        attr_dic = {        # 'placeholder': field.help_text,
                    'class': 'form-control'
        }

        if filed_name in cls.admin_class.readonly_fields:
            attr_dic['disabled'] = True
        # 增加到里面
        field.widget.attrs.update(attr_dic)

    #     运行完自己的__new__,再运行父类的__new__
    return ModelForm.__new__(cls)


# 定义函数
def create_dynamic_modelform(model_class, admin_class):
    # 定义一个类
    class Meta:
        # 表名
        model = model_class
        # 显示所有字段
        fields = "__all__"

    # 重写clean方法, 只读字段为了防止修改前端,所以从数据库取数据,对比,如果不相头则raise.
    def default_clean(self):
        for field in self.admin_class.readonly_fields:
            if hasattr(self.instance, field):
                field_val_in_db = getattr(self.instance, field)     # instance 就是一条数据对象
                new_val = self.cleaned_data.get(field)
                # 如果是many to many
                field_type = self.instance._meta.get_field(field).get_internal_type()
                if field_type == 'ManyToManyField':
                    field_val_in_db = field_val_in_db.all()
                    # 这块是因为ORM没有真实取数据,两个queryset不相等
                    field_val_in_db = [obj.id for obj in field_val_in_db]
                    new_val = [obj.id for obj in new_val]
                if field_val_in_db != new_val:
                    self.add_error(field, '这值不能被修改')
            else:
                raise forms.ValidationError("没有这个字段,你却写在readonly_fields")
    # 动态生成类,
    dynamic_modelform = type('DynamicModelForm',    # 类名
                             (ModelForm,),          # 继承
                             {'Meta': Meta,
                              'clean': default_clean,
                              'admin_class': admin_class,
                              '__new__': __new__},)        # 传值,属性

    return dynamic_modelform
