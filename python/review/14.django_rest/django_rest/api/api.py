#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2017/12/6 下午3:56
__author__ = "willian"

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import *


# 1. 为了返回JSON数据更方便。 2. 修改content_type = application/json
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# 查询和增加
@csrf_exempt
def author_list(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)  # 将数据转换成JSON
        return JSONResponse(serializer.data)        # 返回JSON数据给用户

    elif request.method == 'POST':
        data = JSONParser().parse(request)  # 解析、清洗数据
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    return JSONResponse("Request method not support")


# 更新和删除
@csrf_exempt
def author_detail(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return JSONResponse("Not Found", status=404)

    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(author, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        author.delete()
        return JSONResponse('done', status=204)
