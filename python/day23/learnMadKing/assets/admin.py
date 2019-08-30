from django.contrib import admin
from assets import models
from assets import core

# django的用户管理
admin.site.register(models.UserProfile)


# 显示字段
class AssetApprovalAdmin(admin.ModelAdmin):
    list_display = ('sn', 'asset_type', 'manufactory', 'model', 'cpu_model', 'os_type', 'os_release', 'approved')

# 过滤
    list_filter = ('sn', 'os_type')
# 查找
    search_fields = ('os_type', 'manufactory')
# 编辑 能被编辑的一定是可以显示的
    list_editable = ('asset_type', 'approved')
# action
    actions = ['asset_approval', ]

    def asset_approval(self, request, querysets):
        print("action 配置")
        # 审批
        for obj in querysets:
            asset_handler = core.Asset(request)
            # 检查字段合法性
            if asset_handler.data_is_valid_without_id(obj):
                # 存入
                asset_handler.data_inject()
                obj.approved = True
                obj.save()

    asset_approval.short_description = "新资产审批"
    # 换个名字
    # 这个函数的3个参数
    # 1、类本身
    # 2、request
    # 3、你所选中的数据

# 其他的表结构
admin.site.register(models.Asset)
admin.site.register(models.Server)
admin.site.register(models.NetworkDevice)
admin.site.register(models.SecurityDevice)
admin.site.register(models.Software)
admin.site.register(models.CPU)
admin.site.register(models.RAM)
admin.site.register(models.NIC)
admin.site.register(models.Disk)
admin.site.register(models.BusinessUnit)
admin.site.register(models.Manufactory)
admin.site.register(models.Tag)
admin.site.register(models.Contract)
admin.site.register(models.EventLog)
admin.site.register(models.IDC)

# 关联上面的显示
admin.site.register(models.NewAssetApprovalZone, AssetApprovalAdmin)
