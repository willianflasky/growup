#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/2/16 下午4:40
__author__ = "willian"

from flask import Flask, render_template, Markup, request

app = Flask(__name__)

app.secret_key = 'xx'


# 插件
class Widget(object):
    pass


class InputText(Widget):
    def __call__(self, *args, **kwargs):
        return "<input type='text' name='name'/>"


class TextArea(Widget):
    def __call__(self, *args, **kwargs):
        return "<textarea name='email'></textarea>"


# 字段
class Field(object):
    def __str__(self):
        return self.widget()


class StringField(Field):
    widget = InputText()

    def validate(self, val):
        if val:
            return True


class EmailField(Field):
    widget = TextArea()
    reg = ".*@.*"

    def validate(self, val):
        import re
        if re.match(self.reg, val):
            return True


# Form
class BaseForm(object):
    def __init__(self):
        # 获取当前字段
        _fields = {}
        # 循环类的所有静态字段,如果是Field类型加到_fields字典
        for name, field in self.__class__.__dict__.items():  # 这块很牛，在这里拿到LoginForm类中所有静态字段
            if isinstance(field, Field):
                _fields[name] = field
        self._fields = _fields  # 放到对象中
        self.data = {}

    def validate(self, request_data):
        # 找到所有的字段，执行每个字段的validate方法
        flag = True
        for name, field in self._fields.items():
            input_val = request_data.get(name, '')
            result = field.validate(input_val)
            if not result:
                flag = False
            else:
                self.data[name] = input_val
        return flag


# 定义配置
class LoginForm(BaseForm):
    name = StringField()
    email = EmailField()


@app.route('/login', methods=['get', 'post'])
def index():
    # 使用
    form = LoginForm()
    ret = form.validate(request.form)
    print("验证成功", ret)
    print("验证成功值", form.data)
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run()
