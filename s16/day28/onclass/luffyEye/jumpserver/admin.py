from django.contrib import admin
from django import forms
# Register your models here.
from jumpserver import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


# 修改密码
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = models.Account
        fields = ('email', 'name', 'is_active', 'is_superuser')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# 修改密码
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = models.Account
        fields = ('email', 'password', 'name', 'is_active', 'is_superuser')

    def clean_password(self):
        return self.initial["password"]


class AccountAdmin(BaseUserAdmin):
    # 显示字段
    list_display = ('email', 'name', 'is_superuser')
    # 过滤字段
    list_filter = ('is_superuser',)
    # 每条数据详细. 蓝条分隔,定制每个字段
    fieldsets = (
        ('密码', {'fields': ('email', 'password')}),
        ('个人信息', {'fields': ('name',)}),
        ('权限', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Audit权限', {'fields': ('bind_host_users', 'host_groups')}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.   官方粘过来的
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2')}),
        )

    # 增加搜索条,按邮箱搜索
    search_fields = ('email',)
    # 用邮箱排序
    ordering = ('email',)
    # 对于多对多,选择
    filter_horizontal = ('user_permissions', 'groups', 'bind_host_users', 'host_groups')


class HostUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'auth_type', 'password']


admin.site.register(models.Account, AccountAdmin)
admin.site.register(models.Host)
admin.site.register(models.HostGroup)
admin.site.register(models.HostUser, HostUserAdmin)
admin.site.register(models.IDC)
admin.site.register(models.AuditLog)
admin.site.register(models.SessionLog)
admin.site.register(models.BindHostUser)

