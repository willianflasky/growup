from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    """为帐号表提供创建普通用户和创建超级用户的方法"""

    def create_user(self, email, name, password=None):  # 把name加进来， 生日去掉
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,  # 把name加进来， 生日去掉
        )

        user.set_password(password)
        user.is_active = True  # 增加一个普通用户默认激活
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):  # 把name加进来， 生日去掉
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,  # 把name加进来， 生日去掉
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    """帐号表"""
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=32)  # 增加name字段
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()  # 关联创建用户的方法

    USERNAME_FIELD = 'email'  # email当作登录用户名
    REQUIRED_FIELDS = ['name']  # 指定必须填写项目, 让name字段为必填

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin