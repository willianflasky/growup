### django rest_framework

>	基于函数

#### 安装
>	pip3 install djangorestframework


#### 添加项目
```
INSTALLED_APPS = [
    'api.apps.ApiConfig',
    'rest_framework',
]

```

#### 定义serializers.ModelSerializer
>  api/serializers.py

#### 定义JSONResponse和写业务
>	api/api.py

#### django_rest/urls.py
