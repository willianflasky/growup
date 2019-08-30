import spider


def f1(data):
    print("\033[31;1m{0}\033[0m".format(data))


def f2(data):
    print("\033[32;1m{0}\033[0m".format(data))

url_list = [
    {'host': "www.baidu.com", 'url': '/', 'callback': f1},   # socket
    {'host': "www.bing.com", 'url': '/', 'callback': f2},
    {'host': "www.cnblogs.com", 'url': '/wupeiqi', 'callback': f1},
    {'host': "www.oldboyedu.com", 'url': '/', 'callback': f1},
]
obj = spider.NbIO()
obj.connect(url_list)
obj.send()
