### auth
```
1. 认证登录 views.py
2. models.py (UserProfile, MyUserManager)自定义用户表
3. admin.py (UserProfileAdmin, UserChangeForm, UserCreationForm)在admin中注册和管理UserProfile表
4. 官方网址  https://docs.djangoproject.com/en/1.11/topics/auth/
5. username: root@163.com
	password: root!@#$%^
```


### 信号
>   signals.py

>   apps.py调用

```
    def ready(self):
        from . import signals
```