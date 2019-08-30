#导入django的验证
from django.contrib.auth.models import User
#里面有的AbstractUser里面有django用户的字段 User直接跳过去就好

from django.db import models

# Create your models here.

class Asset(models.Model):
    """资产表 基础表"""
    asset_type_choices = (
        ('server','服务器'),
        ('networkdevice','网络设备'),
        ('storagedevice','安全设备'),
        ('idcdevice','机房设备'),
        ('accescories','备件'),
        ('software','软件资产'),
    )
    asset_type = models.CharField(choices=asset_type_choices,max_length=64,default='server')
    name = models.CharField(max_length=64,unique=True)
    sn = models.CharField('资产SN号',max_length=128,unique=True)
    manufactory = models.ForeignKey('Manufactory',verbose_name='制造商',null=True,blank=True)
    management_ip = models.GenericIPAddressField('管理IP',blank=True,null=True)
    contract = models.ForeignKey('Contract',verbose_name='合同',null=True,blank=True)
    trade_date = models.DateField('购买时间',null=True,blank=True)
    expire_date = models.DateField('过保修期',null=True,blank=True)
    price = models.FloatField('价格',null=True,blank=True)
    business_unit = models.ForeignKey('BusinessUnit',verbose_name='所属业务线',null=True,blank=True)
    tags = models.ManyToManyField('Tag',blank=True)
    admin = models.ForeignKey('UserProfile',verbose_name='资产管理员',null=True,blank=True)
    idc = models.ForeignKey('IDC',verbose_name='IDC机房',null=True,blank=True)

    status_choices = ((0,'在线'),
                      (1,'已下线'),
                      (2,'未知'),
                      (3,'故障'),
                      (4,'备用'),
                      )
    status = models.SmallIntegerField(choices=status_choices,default=0)

    memo = models.TextField('备注',null=True,blank=True)
    create_date = models.DateTimeField(blank=True,auto_now_add=True)
    update_date = models.DateTimeField(blank=True,auto_now=True)

    #auto_now_add 创建的时间
    #auto_now 创建时间 更新时间

    class Meta:
        verbose_name = '资产总表'
        verbose_name_plural = '资产总表'

    #verbose_name 模型类可读名字
    #verbose_name_plural 模型的复数形式

    def __str__(self):
        return '<id:%s name:%s>' %(self.id,self.name)

class Server(models.Model):
    """服务器表"""
    asset = models.OneToOneField('Asset')
    sub_asset_type_choices = (
        (0,'PC服务器'),
        (1,'刀片机'),
        (2,'小型机'),
    )
    created_by_chices = (
        ('auto','Auto'),
        ('manual','Manual'),
    )
    #创建有自动和手动的,自动认为是准确的不让更改的

    sub_asset_type = models.SmallIntegerField(choices=sub_asset_type_choices,verbose_name='服务器类型',default=0)
    created_by = models.CharField(choices=created_by_chices,max_length=32,default='auto')
    hosted_on = models.ForeignKey('self',related_name='hosted_on_server',blank=True,null=True)
    #虚拟机就是自关联
    model = models.CharField(verbose_name='型号',max_length=128,null=True,blank=True)
    raid_type = models.CharField('raid类型',max_length=512,blank=True,null=True)
    os_type = models.CharField('操作系统类型',max_length=64,blank=True,null=True)
    os_distribution = models.CharField('发型版本',max_length=64,blank=True,null=True)
    os_release = models.CharField('操作系统版本',max_length=64,blank=True,null=True)

    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = '服务器'

    def __str__(self):
        return "%s sn:%s" %(self.asset.name,self.asset.sn)

class SecurityDevice(models.Model):
    """安全设备"""
    asset = models.OneToOneField('Asset')
    sub_asset_type_choices = (
        (0,'防火墙'),
        (1,'入侵检测设备'),
        (2,'互联网网关'),
        (3,'运维审计系统'),
    )
    sub_asset_type = models.SmallIntegerField(choices=sub_asset_type_choices,verbose_name='服务器类型',default=0)

    def __str__(self):
        return  self.asset.id

class NetworkDevice(models.Model):
    """网络设备"""
    asset = models.OneToOneField('Asset')
    sub_asset_type_choices =(
        (0,'路由器'),
        (1,'交换机'),
        (2,'负载均衡'),
        (3,'VPN设备'),
    )
    sub_asset_type = models.SmallIntegerField(choices=sub_asset_type_choices,verbose_name='服务器类型',default=0)
    vlan_ip = models.GenericIPAddressField('VlanIP',blank=True,null=True)
    intranet_ip = models.GenericIPAddressField('内网IP',blank=True,null=True)
    model = models.CharField('型号',max_length=128,null=True,blank=True)
    firmware = models.ForeignKey('Software',blank=True,null=True)
    port_num = models.SmallIntegerField('端口个数',null=True,blank=True)
    device_detail = models.TextField('设置详细配置',null=True,blank=True)
    #类似背板带宽

    class Meta:
        verbose_name = '网络设备'
        verbose_name_plural = '网络设备'

class Software(models.Model):
    """公司所购买的软件"""
    sub_asset_type_choices = (
        (0,'OS'),
        (1,'办公\开发软件'),
        (2,'业务软件'),
    )
    sub_asset_type = models.SmallIntegerField(choices=sub_asset_type_choices,verbose_name='服务器类型',default=0)
    license_num = models.IntegerField(verbose_name="授权数")
    version = models.CharField('软件/系统版本',max_length=64,help_text='eg. CentOS release 6.5 (Final)',unique=True)

    class Meta:
        verbose_name = '软件/系统'
        verbose_name_plural = '软件/系统'

    def __str__(self):
        return self.version

class CPU(models.Model):
    """CPU组件"""
    asset = models.OneToOneField('Asset')
    cpu_model = models.CharField('CPU型号',max_length=128,blank=True)
    cpu_count = models.SmallIntegerField('物理cpu个数')
    cpu_core_count = models.SmallIntegerField('cpu核数')
    memo = models.TextField('备注',null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)

    class Meta:
        verbose_name = 'CPU部件'
        verbose_name_plural ='CPU部件'

    def __str__(self):
        return self.cpu_model

class RAM(models.Model):
    """内存组件"""
    asset = models.ForeignKey('Asset')
    sn = models.CharField('SN号',max_length=128,blank=True,null=True)
    model = models.CharField('内存型号',max_length=128)
    slot = models.CharField('插槽',max_length=64)
    capacity = models.IntegerField('内存大小(MB)')
    memo = models.CharField('备注',max_length=128,blank=True,null=True)
    create_date = models.DateTimeField(blank=True,auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)


    class Meta:
        verbose_name ='RAM'
        verbose_name_plural = 'RAM'
        unique_together = ("asset","slot")
        #联合唯一 对于内存来说 资产号和槽位

    def __str__(self):
        return '%s:%s:%s' %(self.asset_id,self.slot,self.capacity)

    auto_create_fileds = ['sn','slot','model','capacity']

class Disk(models.Model):
    """硬盘组件"""
    asset = models.ForeignKey('Asset')
    sn = models.CharField('SN号',max_length=128,blank=True,null=True)
    slot = models.CharField('插槽位',max_length=64)
    manufactory = models.CharField('制造商',max_length=128,blank=True,null=True)
    model = models.CharField('磁盘型号',max_length=128,blank=True,null=True)
    capacity = models.FloatField('磁盘容量GB')
    disk_iface_choice = (
        ('SATA','SATA'),
        ('SAS','SAS'),
        ('SCSI','SCSI'),
        ('SSD','SSD'),
    )
    iface_type = models.CharField('接口类型',max_length=64,choices=disk_iface_choice,default='SAS')
    memo = models.TextField('备注',blank=True,null=True)
    create_date = models.DateTimeField(blank=True,auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)

    class Meta:
        verbose_name = '硬盘'
        verbose_name_plural = '硬盘'
        unique_together = ('asset','slot')

    def __str__(self):
        return  "%s:slot:%s capacity:%s" %(self.asset_id,self.slot,self.capacity)

    auto_create_fields = ['sn','slot','manufactory','model','capacity','iface_type']

class NIC(models.Model):
    """网卡组件"""
    asset = models.ForeignKey('Asset')
    name = models.CharField('网卡名',max_length=64,blank=True,null=True)
    sn = models.CharField('SN号',max_length=128,blank=True,null=True)
    model = models.CharField('网卡型号',max_length=128,blank=True,null=True)
    macaddress = models.CharField('MAC',max_length=64,blank=True,null=True)
    ipaddress = models.GenericIPAddressField(max_length=64,blank=True,null=True)
    netmask = models.CharField(max_length=64,blank=True,null=True)
    bonding = models.CharField(max_length=64,blank=True,null=True)
    memo = models.CharField('备注',max_length=128,blank=True,null=True)
    create_date = models.DateTimeField(blank=True,auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)

    class Meta:
        verbose_name = '网卡'
        verbose_name_plural = '网卡'
        unique_together = ('asset','macaddress')

    def __str__(self):
        return '%s:%s' %(self.asset_id,self.macaddress)

    auto_create_fields = ['name','sn','model','macaddress','ipaddress','netmask','bonding']

class RaidAdaptor(models.Model):
    """Raid卡"""
    asset = models.ForeignKey('Asset')
    sn = models.CharField('SN号',max_length=128,blank=True,null=True)
    slot = models.CharField('插口',max_length=64)
    model = models.CharField('型号',max_length=64,blank=True,null=True)
    memo = models.TextField('备注',blank=True,null=True)
    create_date = models.DateTimeField(blank=True,auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)

    class Meta:
        unique_together = ('asset','slot')

    def __str__(self):
        return self.asset_id

class Manufactory(models.Model):
    """厂商"""
    manufactory = models.CharField('厂商名称',max_length=64,unique=True)
    support_num = models.CharField('支持电话',max_length=30,blank=True)
    memo = models.TextField('备注',max_length=128,blank=True)

    class Meta:
        verbose_name = '厂商'
        verbose_name_plural = '厂商'

    def __str__(self):
        return self.manufactory

class BusinessUnit(models.Model):
    """业务线"""
    #原理类比评论和子评论的递归的方式,导致一台机器没有办法属于2个业务,所以引入tag
    parent_unit = models.ForeignKey('self',related_name='parent_level',blank=True,null=True)
    name = models.CharField('业务线',max_length=64,unique=True)
    memo = models.TextField('备注',max_length=64,blank=True)

    class Meta:
        verbose_name = "业务线"
        verbose_name_plural = "业务线"

    def __str__(self):
        return self.name

class Contract(models.Model):
    """合同"""
    sn = models.CharField('合同号',max_length=128,unique=True)
    name = models.CharField('合同名称',max_length=64)
    memmo = models.TextField('备注',blank=True,null=True)
    price = models.IntegerField('合同金额')
    detail = models.TextField('合同详细',blank=True,null=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    license_num = models.IntegerField('license数量',blank=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    #合同这个地方的时间是必填的

    class Meta:
        verbose_name = '合同'
        verbose_name_plural = '合同'

    def __str__(self):
        return self.name

class IDC(models.Model):
    """机房"""
    name = models.CharField('机房名称',max_length=64,unique=True)
    memo = models.TextField('备注',max_length=128,blank=True,null=True)

    class Meta:
        verbose_name = '机房'
        verbose_name_plural = '机房'

    def __str__(self):
        return  self.name

class Tag(models.Model):
    """资产标签"""
    name = models.CharField('Tag name',max_length=32,unique=True)
    creator = models.ForeignKey('UserProfile')
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class EventLog(models.Model):
    """事件"""
    name = models.CharField('事件名称',max_length=100)
    event_type_choices = (
        (1,'硬件变更'),
        (2,'新增配件'),
        (3,'设备下线'),
        (4,'设备上线'),
        (5,'定期维护'),
        (6,'业务上线\更新\变更'),
        (7,'其它'),
    )
    event_type = models.SmallIntegerField('事件类型',choices=event_type_choices)
    asset = models.ForeignKey('Asset')
    component = models.CharField('事件子项',max_length=255,blank=True,null=True)
    detail = models.TextField('事件详情')
    date = models.DateTimeField('事件时间',auto_now_add=True)
    user = models.ForeignKey('UserProfile',verbose_name='事件源')
    memo = models.TextField('备注',blank=True,null=True)

    class Meta:
        verbose_name = '事件记录'
        verbose_name_plural = '事件记录'

    def colored_event_type(self):
        if self.event_type == 1:
            cell_html = '<span style="background: orange;">%s</span>'
        elif self.event_type == 2:
            cell_html = '<span style="background: yellowgreen;">%s</span>'
        else:
            cell_html = '<span>%s</span>'
        return cell_html % self.get_event_type_display()

    colored_event_type.allow_tags = True
    colored_event_type.short_description = '事件类型'

class NewAssetApprovalZone(models.Model):
    """新资产待审批区"""
    sn = models.CharField('资产SN号',max_length=128,unique=True)
    asset_type_choices = (
        ('server','服务器'),
        ('network','网络设备'),
        ('security','安全设备'),
        ('software','软件类'),
        ('others','其他类'),
    )
    asset_type = models.CharField(choices=asset_type_choices,max_length=64,blank=True,null=True)
    manufactory = models.CharField(max_length=64,blank=True,null=True)
    model = models.CharField(max_length=128,blank=True,null=True)
    ram_size = models.IntegerField(blank=True,null=True)
    cpu_model = models.CharField(max_length=128,blank=True,null=True)
    cpu_count = models.IntegerField(blank=True,null=True)
    cpu_core_count = models.IntegerField(blank=True,null=True)
    os_distribution = models.CharField(max_length=64,blank=True,null=True)
    os_type = models.CharField(max_length=64,blank=True,null=True)
    os_release = models.CharField(max_length=64,blank=True,null=True)
    data = models.TextField('资产数据')
    #录入表的数据,其他的字段只是为了让管理员看的比较方便
    date = models.DateTimeField('汇报日期',auto_now_add=True)
    approved = models.BooleanField('已批准',default=False)
    approved_by = models.ForeignKey('UserProfile',verbose_name='批准人',blank=True,null=True)
    approved_date = models.DateTimeField(u'批准日期', blank=True, null=True)

    def __str__(self):
        return self.sn

    class Meta:
        verbose_name = '新上线待批准资产'
        verbose_name_plural = "新上线待批准资产"

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #把django的user验证表1对1对过来,这样的目的是为了可以自己多添加一些djanggo认证中没有的字段
    name = models.CharField(max_length=32)
    phone = models.IntegerField()
    token = models.CharField(max_length=64,null=True,blank=True)

#
# 备注 :
# mysql要在setting中配置,
# 项目中init中要pymsql 然后加载mysqldb
# import pymysql
# pymysql.install_as_MySQLdb()
# mysql中创建数据库要设置字符集
# mysql> create database madking charset utf8;








