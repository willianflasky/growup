from flask import Flask
app = Flask(import_name=__name__)

# 定义类
from werkzeug.routing import BaseConverter
class RegexConverter(BaseConverter):
    """
    自定义URL匹配正则表达式
    """
    def __init__(self, map, regex):
        super(RegexConverter, self).__init__(map)
        self.regex = regex

    def to_python(self, value):
        """
        路由匹配时，匹配成功后传递给视图函数中参数的值
        :param value:
        :return:
        """
        print(value) # "111"
        return int(value)

    def to_url(self, value):
        """
        使用url_for反向生成URL时，传递的参数经过该方法处理，返回的值用于生成URL中的参数
        :param value:
        :return:
        """
        val = super(RegexConverter, self).to_url(value)
        return val

# 添加到flask中
app.url_map.converters['regex'] = RegexConverter


@app.route('/index/<regex("\d+"):nid>',methods=['GET'])
def index_get(nid):
    return 'Index'


class MiddleWare:
    def __init__(self, wsgi_app):
        # app.wsgi_app
        self.wsgi_app = wsgi_app

    def __call__(self, *args, **kwargs):
        print('之前')
        v = self.wsgi_app(*args, **kwargs)
        print('之后')
        return v

if __name__ == '__main__':
    app.wsgi_app = MiddleWare(app.wsgi_app) # 原来的app.wsgi_app
    app.run()