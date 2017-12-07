from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

# 基于类的写法CBV
# 第一步: 自写
# class AuthorList(APIView):
#     def get(self, request, format=None):
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = AuthorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class AuthorDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Author.objects.get(pk=pk)
#         except Author.DoesNotExist:
#             return Http404
#
#     def get(self, request, pk, format=None):
#         author = self.get_object(pk)
#         if author is Http404:
#             return Response("Not found")
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         author = self.get_object(pk)
#         serializer = AuthorSerializer(author, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         author = self.get_object(pk)
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# 使用Mixin(更简洁)
# 第二步
# from rest_framework import mixins
# from rest_framework import generics
#
#
# class AuthorList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class AuthorDetail(mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    generics.GenericAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# 第三步: 极致版
# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from .permissions import IsSuperUser
#
#
# class AuthorList(generics.ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     # permission_classes = (IsAuthenticated,)  # 单独增加权限控制
#
#
# class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     # permission_classes = (IsSuperUser,)  # 自定义权限只允许超级用户才可以访问


# 第四步： 终极版
from rest_framework import viewsets


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # permission_classes = ()


AuthorList = AuthorViewSet.as_view({
    'get': 'list',
    'post': "create",
})

AuthorDetail = AuthorViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partical_update',
    'delete': 'destroy',
})
