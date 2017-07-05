# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('asset_type', models.CharField(max_length=64, default='server', choices=[('server', '服务器'), ('networkdevice', '网络设备'), ('storagedevice', '安全设备'), ('idcdevice', '机房设备'), ('accescories', '备件'), ('software', '软件资产')])),
                ('name', models.CharField(max_length=64, unique=True)),
                ('sn', models.CharField(verbose_name='资产SN号', max_length=128, unique=True)),
                ('management_ip', models.GenericIPAddressField(verbose_name='管理IP', blank=True, null=True)),
                ('trade_date', models.DateField(verbose_name='购买时间', blank=True, null=True)),
                ('expire_date', models.DateField(verbose_name='过保修期', blank=True, null=True)),
                ('price', models.FloatField(verbose_name='价格', blank=True, null=True)),
                ('status', models.SmallIntegerField(default=0, choices=[(0, '在线'), (1, '已下线'), (2, '未知'), (3, '故障'), (4, '备用')])),
                ('memo', models.TextField(verbose_name='备注', blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '资产总表',
                'verbose_name_plural': '资产总表',
            },
        ),
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='业务线', max_length=64, unique=True)),
                ('memo', models.TextField(verbose_name='备注', max_length=64, blank=True)),
                ('parent_unit', models.ForeignKey(blank=True, null=True, related_name='parent_level', to='assets.BusinessUnit')),
            ],
            options={
                'verbose_name': '业务线',
                'verbose_name_plural': '业务线',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sn', models.CharField(verbose_name='合同号', max_length=128, unique=True)),
                ('name', models.CharField(verbose_name='合同名称', max_length=64)),
                ('memmo', models.TextField(verbose_name='备注', blank=True, null=True)),
                ('price', models.IntegerField(verbose_name='合同金额')),
                ('detail', models.TextField(verbose_name='合同详细', blank=True, null=True)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('license_num', models.IntegerField(verbose_name='license数量', blank=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': '合同',
                'verbose_name_plural': '合同',
            },
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('cpu_model', models.CharField(verbose_name='CPU型号', max_length=128, blank=True)),
                ('cpu_count', models.SmallIntegerField(verbose_name='物理cpu个数')),
                ('cpu_core_count', models.SmallIntegerField(verbose_name='cpu核数')),
                ('memo', models.TextField(verbose_name='备注', blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('asset', models.OneToOneField(to='assets.Asset')),
            ],
            options={
                'verbose_name': 'CPU部件',
                'verbose_name_plural': 'CPU部件',
            },
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sn', models.CharField(verbose_name='SN号', max_length=128, blank=True, null=True)),
                ('slot', models.CharField(verbose_name='插槽位', max_length=64)),
                ('manufactory', models.CharField(verbose_name='制造商', max_length=128, blank=True, null=True)),
                ('model', models.CharField(verbose_name='磁盘型号', max_length=128, blank=True, null=True)),
                ('capacity', models.FloatField(verbose_name='磁盘容量GB')),
                ('iface_type', models.CharField(verbose_name='接口类型', max_length=64, default='SAS', choices=[('SATA', 'SATA'), ('SAS', 'SAS'), ('SCSI', 'SCSI'), ('SSD', 'SSD')])),
                ('memo', models.TextField(verbose_name='备注', blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('asset', models.ForeignKey(to='assets.Asset')),
            ],
            options={
                'verbose_name': '硬盘',
                'verbose_name_plural': '硬盘',
            },
        ),
        migrations.CreateModel(
            name='EventLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='事件名称', max_length=100)),
                ('event_type', models.SmallIntegerField(verbose_name='事件类型', choices=[(1, '硬件变更'), (2, '新增配件'), (3, '设备下线'), (4, '设备上线'), (5, '定期维护'), (6, '业务上线\\更新\\变更'), (7, '其它')])),
                ('component', models.CharField(verbose_name='事件子项', max_length=255, blank=True, null=True)),
                ('detail', models.TextField(verbose_name='事件详情')),
                ('date', models.DateTimeField(verbose_name='事件时间', auto_now_add=True)),
                ('memo', models.TextField(verbose_name='备注', blank=True, null=True)),
                ('asset', models.ForeignKey(to='assets.Asset')),
            ],
            options={
                'verbose_name': '事件记录',
                'verbose_name_plural': '事件记录',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='机房名称', max_length=64, unique=True)),
                ('memo', models.TextField(verbose_name='备注', max_length=128, blank=True, null=True)),
            ],
            options={
                'verbose_name': '机房',
                'verbose_name_plural': '机房',
            },
        ),
        migrations.CreateModel(
            name='Manufactory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('manufactory', models.CharField(verbose_name='厂商名称', max_length=64, unique=True)),
                ('support_num', models.CharField(verbose_name='支持电话', max_length=30, blank=True)),
                ('memo', models.TextField(verbose_name='备注', max_length=128, blank=True)),
            ],
            options={
                'verbose_name': '厂商',
                'verbose_name_plural': '厂商',
            },
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sub_asset_type', models.SmallIntegerField(verbose_name='服务器类型', default=0, choices=[(0, '路由器'), (1, '交换机'), (2, '负载均衡'), (3, 'VPN设备')])),
                ('vlan_ip', models.GenericIPAddressField(verbose_name='VlanIP', blank=True, null=True)),
                ('intranet_ip', models.GenericIPAddressField(verbose_name='内网IP', blank=True, null=True)),
                ('model', models.CharField(verbose_name='型号', max_length=128, blank=True, null=True)),
                ('port_num', models.SmallIntegerField(verbose_name='端口个数', blank=True, null=True)),
                ('device_detail', models.TextField(verbose_name='设置详细配置', blank=True, null=True)),
                ('asset', models.OneToOneField(to='assets.Asset')),
            ],
            options={
                'verbose_name': '网络设备',
                'verbose_name_plural': '网络设备',
            },
        ),
        migrations.CreateModel(
            name='NewAssetApprovalZone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sn', models.CharField(verbose_name='资产SN号', max_length=128, unique=True)),
                ('asset_type', models.CharField(max_length=64, blank=True, null=True, choices=[('server', '服务器'), ('network', '网络设备'), ('security', '安全设备'), ('software', '软件类'), ('others', '其他类')])),
                ('manufactory', models.CharField(max_length=64, blank=True, null=True)),
                ('model', models.CharField(max_length=128, blank=True, null=True)),
                ('ram_size', models.IntegerField(blank=True, null=True)),
                ('cpu_model', models.CharField(max_length=128, blank=True, null=True)),
                ('cpu_count', models.IntegerField(blank=True, null=True)),
                ('cpu_core_count', models.IntegerField(blank=True, null=True)),
                ('os_distribution', models.CharField(max_length=64, blank=True, null=True)),
                ('os_type', models.CharField(max_length=64, blank=True, null=True)),
                ('os_release', models.CharField(max_length=64, blank=True, null=True)),
                ('data', models.TextField(verbose_name='资产数据')),
                ('date', models.DateTimeField(verbose_name='汇报日期', auto_now_add=True)),
                ('approved', models.BooleanField(verbose_name='已批准', default=False)),
                ('approved_date', models.DateTimeField(verbose_name='批准日期', blank=True, null=True)),
            ],
            options={
                'verbose_name': '新上线待批准资产',
                'verbose_name_plural': '新上线待批准资产',
            },
        ),
        migrations.CreateModel(
            name='NIC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='网卡名', max_length=64, blank=True, null=True)),
                ('sn', models.CharField(verbose_name='SN号', max_length=128, blank=True, null=True)),
                ('model', models.CharField(verbose_name='网卡型号', max_length=128, blank=True, null=True)),
                ('macaddress', models.CharField(verbose_name='MAC', max_length=64, blank=True, null=True)),
                ('ipaddress', models.GenericIPAddressField(blank=True, null=True)),
                ('netmask', models.CharField(max_length=64, blank=True, null=True)),
                ('bonding', models.CharField(max_length=64, blank=True, null=True)),
                ('memo', models.CharField(verbose_name='备注', max_length=128, blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('asset', models.ForeignKey(to='assets.Asset')),
            ],
            options={
                'verbose_name': '网卡',
                'verbose_name_plural': '网卡',
            },
        ),
        migrations.CreateModel(
            name='RaidAdaptor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sn', models.CharField(verbose_name='SN号', max_length=128, blank=True, null=True)),
                ('slot', models.CharField(verbose_name='插口', max_length=64)),
                ('model', models.CharField(verbose_name='型号', max_length=64, blank=True, null=True)),
                ('memo', models.TextField(verbose_name='备注', blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('asset', models.ForeignKey(to='assets.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sn', models.CharField(verbose_name='SN号', max_length=128, blank=True, null=True)),
                ('model', models.CharField(verbose_name='内存型号', max_length=128)),
                ('slot', models.CharField(verbose_name='插槽', max_length=64)),
                ('capacity', models.IntegerField(verbose_name='内存大小(MB)')),
                ('memo', models.CharField(verbose_name='备注', max_length=128, blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('asset', models.ForeignKey(to='assets.Asset')),
            ],
            options={
                'verbose_name': 'RAM',
                'verbose_name_plural': 'RAM',
            },
        ),
        migrations.CreateModel(
            name='SecurityDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sub_asset_type', models.SmallIntegerField(verbose_name='服务器类型', default=0, choices=[(0, '防火墙'), (1, '入侵检测设备'), (2, '互联网网关'), (3, '运维审计系统')])),
                ('asset', models.OneToOneField(to='assets.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sub_asset_type', models.SmallIntegerField(verbose_name='服务器类型', default=0, choices=[(0, 'PC服务器'), (1, '刀片机'), (2, '小型机')])),
                ('created_by', models.CharField(max_length=32, default='auto', choices=[('auto', 'Auto'), ('manual', 'Manual')])),
                ('model', models.CharField(verbose_name='型号', max_length=128, blank=True, null=True)),
                ('raid_type', models.CharField(verbose_name='raid类型', max_length=512, blank=True, null=True)),
                ('os_type', models.CharField(verbose_name='操作系统类型', max_length=64, blank=True, null=True)),
                ('os_distribution', models.CharField(verbose_name='发型版本', max_length=64, blank=True, null=True)),
                ('os_release', models.CharField(verbose_name='操作系统版本', max_length=64, blank=True, null=True)),
                ('asset', models.OneToOneField(to='assets.Asset')),
                ('hosted_on', models.ForeignKey(blank=True, null=True, related_name='hosted_on_server', to='assets.Server')),
            ],
            options={
                'verbose_name': '服务器',
                'verbose_name_plural': '服务器',
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sub_asset_type', models.SmallIntegerField(verbose_name='服务器类型', default=0, choices=[(0, 'OS'), (1, '办公\\开发软件'), (2, '业务软件')])),
                ('license_num', models.IntegerField(verbose_name='授权数')),
                ('version', models.CharField(verbose_name='软件/系统版本', max_length=64, unique=True, help_text='eg. CentOS release 6.5 (Final)')),
            ],
            options={
                'verbose_name': '软件/系统',
                'verbose_name_plural': '软件/系统',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Tag name', max_length=32, unique=True)),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=32)),
                ('phone', models.IntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tag',
            name='creator',
            field=models.ForeignKey(to='assets.UserProfile'),
        ),
        migrations.AddField(
            model_name='newassetapprovalzone',
            name='approved_by',
            field=models.ForeignKey(verbose_name='批准人', blank=True, null=True, to='assets.UserProfile'),
        ),
        migrations.AddField(
            model_name='networkdevice',
            name='firmware',
            field=models.ForeignKey(blank=True, null=True, to='assets.Software'),
        ),
        migrations.AddField(
            model_name='eventlog',
            name='user',
            field=models.ForeignKey(verbose_name='事件源', to='assets.UserProfile'),
        ),
        migrations.AddField(
            model_name='asset',
            name='admin',
            field=models.ForeignKey(verbose_name='资产管理员', blank=True, null=True, to='assets.UserProfile'),
        ),
        migrations.AddField(
            model_name='asset',
            name='business_unit',
            field=models.ForeignKey(verbose_name='所属业务线', blank=True, null=True, to='assets.BusinessUnit'),
        ),
        migrations.AddField(
            model_name='asset',
            name='contract',
            field=models.ForeignKey(verbose_name='合同', blank=True, null=True, to='assets.Contract'),
        ),
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(verbose_name='IDC机房', blank=True, null=True, to='assets.IDC'),
        ),
        migrations.AddField(
            model_name='asset',
            name='manufactory',
            field=models.ForeignKey(verbose_name='制造商', blank=True, null=True, to='assets.Manufactory'),
        ),
        migrations.AddField(
            model_name='asset',
            name='tags',
            field=models.ManyToManyField(blank=True, to='assets.Tag'),
        ),
        migrations.AlterUniqueTogether(
            name='ram',
            unique_together=set([('asset', 'slot')]),
        ),
        migrations.AlterUniqueTogether(
            name='raidadaptor',
            unique_together=set([('asset', 'slot')]),
        ),
        migrations.AlterUniqueTogether(
            name='nic',
            unique_together=set([('asset', 'macaddress')]),
        ),
        migrations.AlterUniqueTogether(
            name='disk',
            unique_together=set([('asset', 'slot')]),
        ),
    ]
