from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin
)

# Create your models here.


class IDC(models.Model):
    name = models.CharField(max_length=64,unique=True)
    def __str__(self):
        return self.name

class Host(models.Model):
    """主机表"""
    hostname = models.CharField("主机唯一",unique=True,max_length=64)
    ip_addr = models.GenericIPAddressField(unique=True)
    idc = models.ForeignKey("IDC")
    port = models.IntegerField(default=22)
    enabled = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)
    #users = models.ManyToManyField("HostUser")

    def __str__(self):
        return self.hostname

class HostGroup(models.Model):
    """主机组"""
    name = models.CharField(max_length=64,unique=True)
    #hosts = models.ManyToManyField("Host")
    bind_host_users =  models.ManyToManyField("BindHostUser")

    def __str__(self):
        return self.name

class HostUser(models.Model):
    """主机用户"""
    username = models.CharField(max_length=64)
    auth_type_choices = ((0,'ssh-password'),(1,'ssh-key'))
    auth_type = models.SmallIntegerField(choices=auth_type_choices,default=0)
    password = models.CharField(max_length=128,blank=True,null=True)

    class Meta:
        unique_together  = ('username','password')

    def __str__(self):
        return "%s-%s-%s" %(self.username,self.get_auth_type_display(),self.password)
        #root `123
        # root

class BindHostUser(models.Model):
    """实现主机与主机用户的关联，最小粒度的权限"""
    host = models.ForeignKey("Host")
    host_user = models.ForeignKey("HostUser")

    class Meta:
        unique_together = ("host",'host_user')

    def __str__(self):
        return "%s-%s"%(self.host,self.host_user)


class Token(models.Model):
    bind_host_user = models.ForeignKey("BindHostUser")
    account = models.ForeignKey("Account")
    val = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s-%s-%s" %(self.bind_host_user,self.account,self.val)



class SessionLog(models.Model):
    account = models.ForeignKey("Account")
    bind_host_user = models.ForeignKey("BindHostUser")
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return "%s-%s" %(self.account,self.bind_host_user)



class AuditLog(models.Model):
    """审计日志"""
    session = models.ForeignKey("SessionLog")
    cmd = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s-%s" %(self.session,self.cmd)

class MyUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(
        'staff status',
        default=True,
        help_text='Designates whether the user can log into this admin site.',
    )

    bind_host_users =  models.ManyToManyField("BindHostUser",blank=True)
    host_groups = models.ManyToManyField("HostGroup",blank=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        # The user is identified by their email address
        return self.name

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email





