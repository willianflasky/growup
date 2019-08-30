import s2

def callback1(data):
    print('百度回来了',data)

def callback2(data):
    print('必应回来了',data)

url_list = [
    ['www.baidu.com',callback1],
    ['www.bing.com',callback2]
]
s2.async_request(url_list)

# #################################  twisted #################################
from twisted.web.client import getPage, defer
from twisted.internet import reactor


def all_done(arg):
    reactor.stop()


def callback1(contents):
    print(contents)

def callback2(contents):
    print(contents)
deferred_list = []

url_list = [
    ('http://www.bing.com',callback1),
    ('http://www.baidu.com',callback2)
]
for url in url_list:
    deferred = getPage(bytes(url[0], encoding='utf8'))
    deferred.addCallback(url[1])
    deferred_list.append(deferred)

dlist = defer.DeferredList(deferred_list)
dlist.addBoth(all_done)

reactor.run()