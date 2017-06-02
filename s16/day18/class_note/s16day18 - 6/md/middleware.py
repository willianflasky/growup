from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
class M1(MiddlewareMixin):

    def process_request(self,request):
        print("m1.process_request")

        # return HttpResponse('.....')

    def process_response(self,request,response):
        print("m1.process_response")
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('m1.process_view')

    def process_exception(self, request, exception):
        print('m1.process_exception')

class M2(MiddlewareMixin):

    def process_request(self,request):
        print("m2.process_request")

