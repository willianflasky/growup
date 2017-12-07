##  django_rest
>   基于类(CBV)

#### 安装
> pip install djangorestframework

#### 注册app
```
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
]
```

#### 定义ModelSerializer
>   api/serializers.py

#### 分页和权限
```
REST_FRAMEWORK = {
    'PAGE_SIZE': 2,
     "DEFAULT_AUTHENTICATION_CLASSES": (
         # 'rest_framework.authentication.SessionAuthentication',
         'rest_framework.authentication.TokenAuthentication',
     ),
     'DEFAULT_PERMISSION_CLASSES': (
         'rest_framework.permissions.IsAuthenticated',
     )
}
```

#### 四种方式(简化从未停止)
>   api/views.py

#### 自定义权限

```
    api/permissions.py
    views.py
        permission_classes = (IsSuperUser,)  # 自定义权限只允许超级用户才可以访问
```

#### urls.py (两个版本)
```
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api/author/$', views.AuthorList.as_view(), name='api-author-list'),
    url(r'^api/author/$', views.AuthorList, name='api-author-list'),
    # url(r'^api/author/(?P<pk>[0-9]+)/$', views.AuthorDetail.as_view(), name='api-author-detail'),
    url(r'^api/author/(?P<pk>[0-9]+)/$', views.AuthorDetail, name='api-author-detail'),
]

```

#### 终极版
```
views.py

from rest_framework import viewsets
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # permission_classes = ()
```

```
urls.py

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views
router = DefaultRouter()
router.register(r'author', views.AuthorViewSet)
urlpatterns += [
    url(r'^', include(router.urls)),
]
```

