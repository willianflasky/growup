from scrapy.http import Response,Request
class DownMiddleware1(object):
    def process_request(self, request, spider):
        """
        请求需要被下载时，经过所有下载器中间件的process_request调用
        :param request:
        :param spider:
        :return:
            None,继续后续中间件去下载；
            Response对象，停止process_request的执行，开始执行process_response
            Request对象，停止中间件的执行，将Request重新调度器
            raise IgnoreRequest异常，停止process_request的执行，开始执行process_exception
        """

        # print("DownMiddleware1.process_request")
        # response = Response(url=request.url,body=b'sdkfjksdjflusdfsdfksljdf',request=request)
        # return response
        # return request
        # request.headers['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8"
        request.headers['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8"
        pass


    def process_response(self, request, response, spider):
        """
        spider处理完成，返回时调用
        :param response:
        :param result:
        :param spider:
        :return:
            Response 对象：转交给其他中间件process_response
            Request 对象：停止中间件，request会被重新调度下载
            raise IgnoreRequest 异常：调用Request.errback
        """
        print('DownMiddleware1.process_response')

        return response

    def process_exception(self, request, exception, spider):
        """
        当下载处理器(download handler)或 process_request() (下载中间件)抛出异常
        :param response:
        :param exception:
        :param spider:
        :return:
            None：继续交给后续中间件处理异常；
            Response对象：停止后续process_exception方法
            Request对象：停止中间件，request将会被重新调用下载
        """
        return None


class DownMiddleware2(object):
    def process_request(self, request, spider):
        """
        请求需要被下载时，经过所有下载器中间件的process_request调用
        :param request:
        :param spider:
        :return:
            None,继续后续中间件去下载；
            Response对象，停止process_request的执行，开始执行process_response
            Request对象，停止中间件的执行，将Request重新调度器
            raise IgnoreRequest异常，停止process_request的执行，开始执行process_exception
        """
        print("DownMiddleware2.process_request")

    def process_response(self, request, response, spider):
        """
        spider处理完成，返回时调用
        :param response:
        :param result:
        :param spider:
        :return:
            Response 对象：转交给其他中间件process_response
            Request 对象：停止中间件，request会被重新调度下载
            raise IgnoreRequest 异常：调用Request.errback
        """
        print('DownMiddleware2.process_response')
        return response

    def process_exception(self, request, exception, spider):
        """
        当下载处理器(download handler)或 process_request() (下载中间件)抛出异常
        :param response:
        :param exception:
        :param spider:
        :return:
            None：继续交给后续中间件处理异常；
            Response对象：停止后续process_exception方法
            Request对象：停止中间件，request将会被重新调用下载
        """
        return None

import six
import random
import base64
def to_bytes(text, encoding=None, errors='strict'):
    if isinstance(text, bytes):
        return text
    if not isinstance(text, six.string_types):
        raise TypeError('to_bytes must receive a unicode, str or bytes '
                        'object, got %s' % type(text).__name__)
    if encoding is None:
        encoding = 'utf-8'
    return text.encode(encoding, errors)

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        PROXIES = [
            {'ip_port': '111.11.228.75:80', 'user_pass': ''},
            {'ip_port': '120.198.243.22:80', 'user_pass': ''},
            {'ip_port': '111.8.60.9:8123', 'user_pass': ''},
            {'ip_port': '101.71.27.120:80', 'user_pass': ''},
            {'ip_port': '122.96.59.104:80', 'user_pass': ''},
            {'ip_port': '122.224.249.122:8088', 'user_pass': ''},
        ]
        proxy = random.choice(PROXIES)

        if proxy['user_pass'] is not None:
            request.meta['proxy'] = to_bytes("http://%s" % proxy['ip_port'])
            encoded_user_pass = base64.encodestring(to_bytes(proxy['user_pass']))
            request.headers['Proxy-Authorization'] = to_bytes('Basic ' + encoded_user_pass)
            print("**************ProxyMiddleware have pass************" + proxy['ip_port'])
        else:
            print("**************ProxyMiddleware no pass************" + proxy['ip_port'])
            request.meta['proxy'] = to_bytes("http://%s" % proxy['ip_port'])