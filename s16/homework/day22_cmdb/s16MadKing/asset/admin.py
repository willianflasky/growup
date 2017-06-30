from django.contrib import admin
from asset import models
from asset import core


# class ServerInline(admin.TabularInline):
#     model = models.Server
#     exclude = ('memo',)
#     #readonly_fields = ['create_date']
#
# class CPUInline(admin.TabularInline):
#     model = models.CPU
#     exclude = ('memo',)
#     readonly_fields = ['create_date']
#
# class NICInline(admin.TabularInline):
#     model = models.NIC
#     exclude = ('memo',)
#     readonly_fields = ['create_date']
#
# class RAMInline(admin.TabularInline):
#     model = models.RAM
#     exclude = ('memo',)
#     readonly_fields = ['create_date']
#
# class DiskInline(admin.TabularInline):
#     model = models.Disk
#     exclude = ('memo',)
#     readonly_fields = ['create_date']
#
#
# class NicAdmin(admin.ModelAdmin):
#     list_display = ('name','macaddress','ipaddress','netmask','bonding')
#     search_fields = ('macaddress','ipaddress')
#

# 定义这个表个性显示
class AssetApprovalAdmin(admin.ModelAdmin):
    # 显示这些字段
    list_display = ('sn', 'asset_type', 'manufactory', 'model', 'cpu_model', 'os_type', 'os_release', 'approved','date')
    # 增加两个过滤条件
    list_filter = ('asset_type', 'os_type')
    # 增加搜索字段
    search_fields = ('sn', 'os_type')
    # 已批准,服务器类型这两个字段可以修改
    list_editable = ('asset_type', 'approved')
    # 定义一个功能
    actions = ['asset_approval', ]
    # 定义一个功能: 批量批准

    def asset_approval(self, request, querysets):
        print("--------asset approval.....", self, request, querysets)
        for obj in querysets:
            asset_handler = core.Asset(request)
            if asset_handler.data_is_valid_without_id(obj):
                asset_handler.data_inject()     # 注射
                obj.approved = True
                obj.save()
                print(asset_handler.response)
    # 定义一个功能: 修改名字
    asset_approval.short_description = "新资产审批"


admin.site.register(models.UserProfile)
admin.site.register(models.Asset)
admin.site.register(models.Server)
admin.site.register(models.NetworkDevice)
admin.site.register(models.IDC)
admin.site.register(models.BusinessUnit)
admin.site.register(models.Contract)
admin.site.register(models.CPU)
admin.site.register(models.Disk)
admin.site.register(models.NIC)
admin.site.register(models.RAM)
admin.site.register(models.Manufactory)
admin.site.register(models.Tag)
admin.site.register(models.Software)
admin.site.register(models.EventLog)
admin.site.register(models.NewAssetApprovalZone, AssetApprovalAdmin)
