import re
import copy


# 一、生成HTML的插件
class TextInput(object):
    def __init__(self, attrs={None: None}):
        if attrs:
            self.attrs = attrs

    def __str__(self):
        data_list = []
        for k, v in self.attrs.items():
            tmp = "{0}='{1}'".format(k, v)
            data_list.append(tmp)
        tpl = "<input type='text' {0} />".format(" ".join(data_list))
        return tpl


class EmailInput(object):
    def __init__(self, attrs={None: None}):
        if attrs:
            self.attrs = attrs

    def __str__(self):
        data_list = []
        for k, v in self.attrs.items():
            tmp = "{0}='{1}'".format(k, v)
            data_list.append(tmp)
        tpl = "<input type='email' {0} />".format(" ".join(data_list))
        return tpl


class PasswordInput(object):
    def __init__(self, attrs={None: None}):
        if attrs:
            self.attrs = attrs
        else:
            attrs = {}

    def __str__(self):
        data_list = []
        for k, v in self.attrs.items():
            tmp = "{0}='{1}'".format(k, v)
            data_list.append(tmp)

        tpl = "<input type='password' {0} />".format(" ".join(data_list))
        return tpl


# obj = TextInput(attrs={'name': 'user', 'value': 123})
# print(obj)


# 二、验证字段
class Field(object):
    def __str__(self):
        if self.value:
            self.widget.attr['value'] = self.value
        return str(self.widget)


class CharField(Field):
    default_widget = TextInput
    regex = "\w+"

    def __init__(self, widget=None):
        self.value = None
        self.widget = widget() if widget else self.default_widget()

    def valid_field(self, value):
        self.value = value
        if re.match(self.regex, value):
            return True
        else:
            return False


class EmailField(Field):
    default_widget = TextInput
    regex = "\w+@\w+"

    def __init__(self, widget=None):
        self.value = None
        self.widget = widget() if widget else self.default_widget()

    def valid_field(self, value):
        self.value = value
        if re.match(self.regex, value):
            return True
        else:
            return False


# class form(object):
#     name = CharField(widget=PasswordInput)
#
# obj = form()
# print(obj.name)

# 三、定制Form类

class BaseForm(object):
    def __init__(self, data={}):
        self.data = data
        self.fields = {}
        # 1. type(self)拿到对象是类是谁 2. 类的.__dict__.items() 遍历类中所有的字段。
        for name, field in type(self).__dict__.items():
            if isinstance(field, Field):
                new_field = copy.deepcopy(field)
                setattr(self, name, new_field)
                self.fields[name] = new_field

    def is_valid(self):
        flag = True
        for name, field in self.fields.items():
            user_input_val = self.data.get(name)
            result = field.valid_field(user_input_val)
            if not result:
                flag = False
        return flag


# 四、使用表单

class LoginForm(BaseForm):
    user = CharField()
    email = EmailField()


form = LoginForm()
print(form.user)
