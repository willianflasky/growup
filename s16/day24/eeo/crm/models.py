from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
    # BaseUserManager email规范设置和密码基本设置规则
    # AbstractBaseUser   真正的用户名 密码 验证
)

# ################如果用User model
# 1、必须有一个唯一的字段可被用于识别目的
# 2、full 和 short的名字
# 继承AbstractBaseUser 这个是核心
# 有了这个还必须要有一个自定管理器
# 如果和User字段和默认的一致的话,直接使用UserManager就可以了,如果user定义了不同的字段
# 需要自定义一个管理器,它继承BaseUserManager 并提供2个额外的方法:


class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email, name and password.
        """
        '''email是唯一标识，没有会报错'''
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),  # 检查email规则
            name=name,
        )
        # AbstractBaseUser set_password == > make_password == > 加盐 hash
        user.set_password(password)     # 检测密码合理性
        user.save(using=self._db)       # 保存密码
        return user

    def create_superuser(self, email, name, password):
        """
        Creates and saves a superuser with the given email, name and password.
        """
        user = self.create_user(email,
            password=password,
            name=name
        )
        user.is_admin = True    # 比创建用户多的一个字段
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserProfileManager()        # 会用到 get_by_natural_key 不然会报

    USERNAME_FIELD = 'email'          # 默认的用户名,对于自定义的用户模型,用USERNAME_FIELD 标识
    REQUIRED_FIELDS = ['name']        # 通过createsuperuser管理命令创建一个用户时,用于提示的一个字段名称列表

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    '''django自带后台权限控制，对哪些表有查看权限等'''
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    '''用户是否有权限看到app'''
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):     # 用户管理网站权限
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin