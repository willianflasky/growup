"""
python2
    文件存储默认是ascii方式,启动加#coding:utf8就是文件以utf8方式打开.否则就是以ascii.变量则是str.

    例子:
    name='中国'
    print(name.decode('utf-8').encode('gbk'))
    #name.decode('utf-8')   意思是:name是UTF8格式先解码成Unicode.注意utf-8这里的意思，原字符(name)是utf8.
    #encode('gbk')  意思是:转码成gbk.
    #注意:str = bytes这两个在python2是一样的。

python3
    文件存储默认是utf8方式,打开文件也是UTF8.变量则是unicode.注意python3中没有decode.

    例子:
    name='中国'
    print(name.encode('gbk'))
    str = unicode
    bytes = python2的bytes(二进制表现形式)
"""


def auth(func):
    def wrapper(*args, **kwargs):
        print("in the wrapper,begin!")
        ret = func(*args, **kwargs)
        print("in the wrapper,stop!")
        return ret
    return wrapper


@auth
def foo(name):
    print("in the foo! i am [%s]" % name)
    return True

ret = foo('tom')
print(ret)
