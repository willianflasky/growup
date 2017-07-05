#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by Wendy

import json
from django.core.exceptions import ObjectDoesNotExist
from assets import models
from django.utils import timezone


class Asset(object):
    def __init__(self, request):
        self.request = request
        # 请求
        self.mandatory_fields = ['sn', 'asset_id', 'asset_type']  # 数据必须有 'sn' , 'asset_id' and 'asset_type'
        # 强制要求sn  asset_id  asset_type 下面要进行合法性认证
        self.field_sets = {
            'asset': ['manufactory'],
            'server': ['model', 'cpu_count', 'cpu_core_count', 'cpu_model', 'raid_type', 'os_type', 'os_distribution',
                       'os_release'],
            'networkdevice': []
        }
        # 错误存入字典
        self.response = {
            'error': [],
            'info': [],
            'warning': []
        }

    def response_msg(self, msg_type, key, msg):
        if msg_type in self.response:
            self.response[msg_type].append({key: msg})
            # 把所有的错都放在一个列表中
        else:
            raise ValueError

    def mandatory_check(self, data, only_check_sn=False):
        # 默认是False 就是默认就是新的资产
        for field in self.mandatory_fields:
            # 循环['sn', 'asset_id', 'asset_type']
            if field not in data:
                # 如果有不在data里面的
                self.response_msg('error', 'MandatoryCheckFailed',
                                  "The field [%s] is mandatory and not provided in your reporting data" % field)
                # 会出很多个错 一次性放在一个列表里面返回
        else:
            if self.response['error']:
                return False
            # 合法性检测没有通过

        try:
            # 合法性检测通过
            # only_check_sn这个参数
            if not only_check_sn:
                # 就是True就是已经有了资产编号的资产
                self.asset_obj = models.Asset.objects.get(id=int(data['asset_id']), sn=data['sn'])
            else:
                # False 就是第一次来的 没有资产编号的资产则是新资产
                self.asset_obj = models.Asset.objects.get(sn=data['sn'])
            return True
            # 有这个资产的情况才会True
        except ObjectDoesNotExist as e:
            # 如果上面的没有找到资产 就会到审批区
            self.response_msg('error', 'AssetDataInvalid',
                              "Cannot find asset object in DB by using asset id [%s] and SN [%s] " % (
                                  data['asset_id'], data['sn']))
            self.waiting_approval = True
            # 到审批区了
            return False
            # 合法性检测没有通过

    # 根据sn拿资产编号
    def get_asset_id_by_sn(self):
        ''' When the client first time reports it's data to Server,it doesn't know it's asset id yet,
        so it will come to the server asks for the asset id first,then report the data again  '''
        # 现在还不知道资产id,拿到资产id再去汇报,根据sn号拿资产id
        data = self.request.POST.get("asset_data")
        # 拿到数据
        response = {}
        if data:
            try:
                data = json.loads(data)
                # 反序列化
                if self.mandatory_check(data, only_check_sn=True):
                    # the asset is already exist in DB,just return it's asset id to client
                    # 合法性检测必须要有指定字段mandatory_fields
                    response = {'asset_id': self.asset_obj.id}  # 将资产编号记录返回给client
                else:
                    # 合法性验证没有通过就到了审批区,缺字段和审批区都会走到这
                    # 这个字段 waiting_approval 是True 但是合法性验证没有通过就是数据库中没有
                    if hasattr(self, 'waiting_approval'):
                        response = {
                            'needs_aproval': "this is a new asset,needs IT admin's approval to create the new asset id."
                            }
                        self.clean_data = data      # 把数据存到对象中
                        self.save_new_asset_to_approval_zone()  # 将数据存入审批表中
                        print(response)
                    else:
                        # 对象waiting_approval的 为false
                        response = self.response
            except ValueError as e:
                # 存入数据返回错误
                self.response_msg('error', 'AssetDataInvalid', str(e))
                response = self.response

        else:
            # 未收到数据,返回错误
            self.response_msg('error', 'AssetDataInvalid', "The reported asset data is not valid or provided")
            response = self.response
        return response

    def save_new_asset_to_approval_zone(self):
        '''When find out it is a new asset, will save the data into approval zone to waiting for IT admin's approvals'''
        asset_sn = self.clean_data.get('sn')        # 去提交的数据里拿SN
        # 查看表NewAssetApprovalZone     data = models.TextField('资产数据')
        # 有则返回对象 没有则创建
        asset_already_in_approval_zone = models.NewAssetApprovalZone.objects.get_or_create(sn=asset_sn,
                                                                                           data=json.dumps(
                                                                                               self.clean_data),
                                                                                           manufactory=self.clean_data.get(
                                                                                               'manufactory'),
                                                                                           model=self.clean_data.get(
                                                                                               'model'),
                                                                                           asset_type=self.clean_data.get(
                                                                                               'asset_type'),
                                                                                           ram_size=self.clean_data.get(
                                                                                               'ram_size'),
                                                                                           cpu_model=self.clean_data.get(
                                                                                               'cpu_model'),
                                                                                           cpu_count=self.clean_data.get(
                                                                                               'cpu_count'),
                                                                                           cpu_core_count=self.clean_data.get(
                                                                                               'cpu_core_count'),
                                                                                           os_distribution=self.clean_data.get(
                                                                                               'os_distribution'),
                                                                                           os_release=self.clean_data.get(
                                                                                               'os_release'),
                                                                                           os_type=self.clean_data.get(
                                                                                               'os_type'),

                                                                                           )
        return True

    def data_is_valid(self):
        data = self.request.POST.get("asset_data")
        if data:
            try:
                data = json.loads(data)
                self.mandatory_check(data)
                self.clean_data = data
                if not self.response['error']:
                    return True
            except ValueError as e:
                self.response_msg('error', 'AssetDataInvalid', str(e))
        else:
            self.response_msg('error', 'AssetDataInvalid', "The reported asset data is not valid or provided")

    def __is_new_asset(self):
        # 必要字段认证,asset_type是表名,(排除资产的)其他表 比如server表里面是否有这个数据记录
        # 自动装机的那种情况
        if not hasattr(self.asset_obj, self.clean_data['asset_type']):  # new asset
            return True
        else:
            return False

    # 插入数据
    # 每张表写一个函数,然后调函数就可以 资产的创建和更新都走这个函数
    def data_inject(self):
        '''save data into DB,the data_is_valid() must returns True before call this function'''

        # self.reformat_components('slot',self.clean_data.get('ram'))
        # self.reformat_components('name',self.clean_data.get('nic'))
        if self.__is_new_asset():
            # 区别新旧资产
            print('\033[32;1m---new asset,going to create----\033[0m')
            self.create_asset()
        else:  # asset already already exist , just update it
            print('\033[33;1m---asset already exist ,going to update----\033[0m')

            self.update_asset()
            # 更新资产

    def data_is_valid_without_id(self, db_obj=None):
        '''when there's no asset id in reporting data ,goes through this function fisrt'''
        if db_obj:
            data = db_obj.data
        else:
            data = self.request.POST.get("asset_data")
        if data:
            try:
                data = json.loads(data)
                # 先创建资产记录, 这样别的表才可以关联
                asset_obj = models.Asset.objects.get_or_create(sn=data.get('sn'), name=data.get(
                    'sn'))  # push asset id into reporting data before doing the mandatory check
                # get_create 创建第一个是id
                data['asset_id'] = asset_obj[0].id
                # 拿到资产id
                self.mandatory_check(data)
                self.clean_data = data
                if not self.response['error']:
                    return True
            except ValueError as e:
                self.response_msg('error', 'AssetDataInvalid', str(e))
        else:
            self.response_msg('error', 'AssetDataInvalid', "The reported asset data is not valid or provided")

    def reformat_components(self, identify_field, data_set):
        '''This function is used as workround for some components's data structor is big dict ,yet
        the standard structor is list,e.g:
        standard: [{
            "slot": "1I:1:1",
            "capacity": 300,
            "sn": "",
            "model": "",
            "enclosure": "0",
            "iface_type": "SAS"
        },
        {
            "slot": "1I:1:2",
            "capacity": 300,
            "sn": "",
            "model": "",
            "enclosure": "0",
            "iface_type": "SAS"
        }]
        but for some components such as ram:
        {"PROC 2 DIMM 1": {
            "model": "<OUT OF SPEC>",
            "capacity": 0,
            "sn": "Not Specified",
            "manufactory": "UNKNOWN"
        },}

        it uses key as identified field, the key is actually equals slot field in db model field, this unstandard
        data source should be dprecated in the future, now I will just reformat it as workround
        '''
        for k, data in data_set.items():
            data[identify_field] = k

    def __verify_field(self, data_set, field_key, data_type, required=True):
        # __verify_field(self.clean_data, 'model', str)  下面调用
        # 在创建数据的时候出错要提前检查是否合法
        field_val = data_set.get(field_key)
        if field_val:
            try:
                # 强转并且赋值
                data_set[field_key] = data_type(field_val)
            except ValueError as e:
                self.response_msg('error', 'InvalidField',
                                  "The field [%s]'s data type is invalid, the correct data type should be [%s] " % (
                                      field_key, data_type))

        elif required == True:
            self.response_msg('error', 'LackOfField',
                              "The field [%s] has no value provided in your reporting data [%s]" % (
                                  field_key, data_set))

    def create_asset(self):
        '''
        invoke asset create function according to it's asset type
        :return:
        '''
        func = getattr(self, '_create_%s' % self.clean_data['asset_type'])
        create_obj = func()
        # 去各个表插入数据

    def update_asset(self):
        func = getattr(self, '_update_%s' % self.clean_data['asset_type'])
        # 利用反射到更新的资产类型
        create_obj = func()

    # 因为需要更新的资产类型有很多,所以这里提取了一个公共的库
    def _update_server(self):
        nic = self.__update_asset_component(data_source=self.clean_data['nic'],
                                            fk='nic_set',
                                            update_fields=['name', 'sn', 'model', 'macaddress', 'ipaddress', 'netmask',
                                                           'bonding'],
                                            identify_field='macaddress'
                                            )
        disk = self.__update_asset_component(data_source=self.clean_data['physical_disk_driver'],
                                             fk='disk_set',
                                             update_fields=['slot', 'sn', 'model', 'manufactory', 'capacity',
                                                            'iface_type'],
                                             identify_field='slot'
                                             )
        ram = self.__update_asset_component(data_source=self.clean_data['ram'],
                                            fk='ram_set',
                                            update_fields=['slot', 'sn', 'model', 'capacity'],
                                            identify_field='slot'
                                            )
        cpu = self.__update_cpu_component()
        manufactory = self.__update_manufactory_component()

        server = self.__update_server_component()

    def _create_server(self):
        self.__create_server_info()
        self.__create_or_update_manufactory()

        self.__create_cpu_component()
        self.__create_disk_component()
        self.__create_nic_component()
        self.__create_ram_component()

        log_msg = "Asset [<a href='/admin/assets/asset/%s/' target='_blank'>%s</a>] has been created!" % (
            self.asset_obj.id, self.asset_obj)
        self.response_msg('info', 'NewAssetOnline', log_msg)

    def __create_server_info(self, ignore_errs=False):
        try:
            self.__verify_field(self.clean_data, 'model', str)

            if not len(self.response['error']) or ignore_errs == True:  # no processing when there's no error happend
                data_set = {
                    'asset_id': self.asset_obj.id,
                    'raid_type': self.clean_data.get('raid_type'),
                    'model':self.clean_data.get('model'),
                    'os_type': self.clean_data.get('os_type'),
                    'os_distribution': self.clean_data.get('os_distribution'),
                    'os_release': self.clean_data.get('os_release'),
                }

                obj = models.Server(**data_set)
                obj.asset.model = self.clean_data.get('model')
                obj.save()
                return obj
        except Exception as e:
            self.response_msg('error', 'ObjectCreationException', 'Object [server] %s' % str(e))

    def __create_or_update_manufactory(self, ignore_errs=False):
        try:
            self.__verify_field(self.clean_data, 'manufactory', str)
            #每个字段检查然后强转
            manufactory = self.clean_data.get('manufactory')
            if not len(self.response['error']) or ignore_errs == True:  # no processing when there's no error happend
                obj_exist = models.Manufactory.objects.filter(manufactory=manufactory)
                if obj_exist:
                    obj = obj_exist[0]
                else:  # create a new one
                    obj = models.Manufactory(manufactory=manufactory)
                    obj.save()
                self.asset_obj.manufactory = obj
                self.asset_obj.save()
        except Exception as e:
            self.response_msg('error', 'ObjectCreationException', 'Object [manufactory] %s' % str(e))

    def __create_cpu_component(self, ignore_errs=False):
        try:
            self.__verify_field(self.clean_data, 'model', str)
            self.__verify_field(self.clean_data, 'cpu_count', int)
            self.__verify_field(self.clean_data, 'cpu_core_count', int)
            #检查的字段强转,并赋值
            if not len(self.response['error']) or ignore_errs == True:  # no processing when there's no error happend
                data_set = {
                    'asset_id': self.asset_obj.id,
                    'cpu_model': self.clean_data.get('cpu_model'),
                    'cpu_count': self.clean_data.get('cpu_count'),
                    'cpu_core_count': self.clean_data.get('cpu_core_count'),
                }

                obj = models.CPU(**data_set)
                obj.save()
                log_msg = "Asset[%s] --> has added new [cpu] component with data [%s]" % (self.asset_obj, data_set)
                self.response_msg('info', 'NewComponentAdded', log_msg)
                return obj
        except Exception as e:
            self.response_msg('error', 'ObjectCreationException', 'Object [cpu] %s' % str(e))

    def __create_disk_component(self):
        #硬盘有好几块需要循环的创建
        disk_info = self.clean_data.get('physical_disk_driver')
        if disk_info:
            for disk_item in disk_info:
                #每个盘检查
                try:
                    self.__verify_field(disk_item, 'slot', str)
                    self.__verify_field(disk_item, 'capacity', float)
                    self.__verify_field(disk_item, 'iface_type', str)
                    self.__verify_field(disk_item, 'model', str)
                    if not len(self.response['error']):  # no processing when there's no error happend
                        data_set = {
                            'asset_id': self.asset_obj.id,
                            'sn': disk_item.get('sn'),
                            'slot': disk_item.get('slot'),
                            'capacity': disk_item.get('capacity'),
                            'model': disk_item.get('model'),
                            'iface_type': disk_item.get('iface_type'),
                            'manufactory': disk_item.get('manufactory'),
                        }

                        obj = models.Disk(**data_set)
                        obj.save()

                except Exception as e:
                    self.response_msg('error', 'ObjectCreationException', 'Object [disk] %s' % str(e))
        else:
            self.response_msg('error', 'LackOfData', 'Disk info is not provied in your reporting data')

    def __create_nic_component(self):
        nic_info = self.clean_data.get('nic')
        if nic_info:
            for nic_item in nic_info:
                #网卡循环创建
                try:
                    self.__verify_field(nic_item, 'macaddress', str)
                    if not len(self.response['error']):  # no processing when there's no error happend
                        data_set = {
                            'asset_id': self.asset_obj.id,
                            'name': nic_item.get('name'),
                            'sn': nic_item.get('sn'),
                            'macaddress': nic_item.get('macaddress'),
                            'ipaddress': nic_item.get('ipaddress'),
                            'bonding': nic_item.get('bonding'),
                            'model': nic_item.get('model'),
                            'netmask': nic_item.get('netmask'),
                        }

                        obj = models.NIC(**data_set)
                        obj.save()

                except Exception as e:
                    self.response_msg('error', 'ObjectCreationException', 'Object [nic] %s' % str(e))
        else:
            self.response_msg('error', 'LackOfData', 'NIC info is not provied in your reporting data')

    def __create_ram_component(self):
        ram_info = self.clean_data.get('ram')
        #内存循环创建
        if ram_info:
            for ram_item in ram_info:
                try:
                    self.__verify_field(ram_item, 'capacity', int)
                    if not len(self.response['error']):  # no processing when there's no error happend
                        data_set = {
                            'asset_id': self.asset_obj.id,
                            'slot': ram_item.get("slot"),
                            'sn': ram_item.get('sn'),
                            'capacity': ram_item.get('capacity'),
                            'model': ram_item.get('model'),
                        }

                        obj = models.RAM(**data_set)
                        obj.save()

                except Exception as e:
                    self.response_msg('error', 'ObjectCreationException', 'Object [ram] %s' % str(e))
        else:
            self.response_msg('error', 'LackOfData', 'RAM info is not provied in your reporting data')

    def __update_server_component(self):
        update_fields = ['model', 'raid_type', 'os_type', 'os_distribution', 'os_release']
        if hasattr(self.asset_obj, 'server'):
            self.__compare_componet(model_obj=self.asset_obj.server,
                                    fields_from_db=update_fields,
                                    data_source=self.clean_data)
        else:
            self.__create_server_info(ignore_errs=True)

    def __update_manufactory_component(self):
        self.__create_or_update_manufactory(ignore_errs=True)

    def __update_cpu_component(self):
        update_fields = ['cpu_model', 'cpu_count', 'cpu_core_count']
        if hasattr(self.asset_obj, 'cpu'):
            self.__compare_componet(model_obj=self.asset_obj.cpu,
                                    fields_from_db=update_fields,
                                    data_source=self.clean_data)
        else:
            self.__create_cpu_component(ignore_errs=True)

    def __update_asset_component(self, data_source, fk, update_fields, identify_field=None):
        '''

        self.clean_data['nic'],fk='nic_set',update_fields=['name', 'sn', 'model', 'macaddress', 'ipaddress', 'netmask',
                                                           'bonding'],
                                            identify_field='macaddress')

        data_source: 客户端上报数据 the data source of this component from reporting data
        fk: 根据表_set (nic_set)找到资产的obj   which key to use to find the connection between main Asset obj and each asset component
        update_fields: 需要更新的字段  what fields in DB will be compared and updated
        identify_field: 用于区分具体是哪一条数据的唯一值 例如mac地址等 use this field to identify each component of an Asset , if set to None,means only use asset id to identify
         '''
        print(data_source, update_fields, identify_field)
        try:
            """
            s = models.Asset.objects.last()
            s.nic_set.all() 拿到所有的nic对象


            m1 = s.nic_set.all()[0] 拿到某一个nic的记录
            m1.macaddress  可以拿到nic某个字段的记录
            getattr(m1,'macaddress') 利用反射可以直接拿到 某条nic的值
            """
            component_obj = getattr(self.asset_obj, fk)
            # 这个资产编号所有的nic   资产表反向查找了nic那个表
            # s = models.Asset.objects.last()
            # s.nic_set
            # component_obj是否有select_related字段
            if hasattr(component_obj, 'select_related'):  # this component is reverse m2m relation with Asset model
                objects_from_db = component_obj.select_related()
                # nic的记录 有这个资产编号的
                # s = models.Asset.objects.last()
                # s.nic_set.all() 拿到所有的nic对象
                for obj in objects_from_db:
                    key_field_data = getattr(obj, identify_field)
                    # m1.macaddress  可以拿到nic某个字段的记录 其实就是拿到了的那个macaddress的值
                    # 这个地方的反射用的非常巧妙
                    # use this key_field_data to find the relative data source from reporting data
                    if type(data_source) is list:
                        # data_source 客户端上报数据
                        for source_data_item in data_source:  # 到客户端的数据 源里去找到跟 服务器数据库中key_field_data对应的条目
                            # 上报数据循环
                            key_field_data_from_source_data = source_data_item.get(identify_field)
                            # 客户端上报数据的的macaddress找到 如果值存在
                            if key_field_data_from_source_data:
                                if key_field_data == key_field_data_from_source_data:
                                    # find the matched source data for this component,then should compare each field
                                    # in this component to see if there's any changes since last update
                                    # 客户端和服务器端的mac地址对上
                                    self.__compare_componet(model_obj=obj, fields_from_db=update_fields,
                                                            data_source=source_data_item)
                                    # __compare_componet(nic对象数据库, 更新的字段,
                                    #                        客户端某一个nic的所有的信息)

                                    break  # 已经根据identify_field找到客户端中对应的数据条目，且对比完了，后面的loop没必要继续了
                            else:  # key field data from source data cannot be none
                                #  如果客户端上报的macaddress没有
                                self.response_msg('warning', 'AssetUpdateWarning',
                                                  "Asset component [%s]'s key field [%s] is not provided in reporting data " % (
                                                      fk, identify_field))


                        else:  # couldn't find any matches, the asset component must be broken or changed manually
                            print(
                                '\033[33;1mError:cannot find any matches in source data by using key field val [%s],component data is missing in reporting data!\033[0m' % (
                                    key_field_data))
                            self.response_msg("error", "AssetUpdateWarning",
                                              "Cannot find any matches in source data by using key field val [%s],component data is missing in reporting data!" % (
                                                  key_field_data))

                    elif type(data_source) is dict: #deprecated  废弃 因为当时客户端的上报数据有字典的也有列表的所以以后两个地方要商量好了来好处理
                        for key, source_data_item in data_source.items():
                            key_field_data_from_source_data = source_data_item.get(identify_field)
                            if key_field_data_from_source_data:
                                if key_field_data == key_field_data_from_source_data:  # find the matched source data for this component,then should compare each field in this component to see if there's any changes since last update
                                    self.__compare_componet(model_obj=obj, fields_from_db=update_fields,
                                                            data_source=source_data_item)
                                    #对字段进行更新
                                    break  # must break ast last ,then if the loop is finished , logic will goes for ..else part,then you will know that no source data is matched for by using this key_field_data, that means , this item is lacked from source data, it makes sense when the hardware info got changed. e.g: one of the RAM is broken, sb takes it away,then this data will not be reported in reporting data
                                    #一旦找到执行完操作 就不再继续循环了 直接跳出循环
                            else:  # key field data from source data cannot be none
                                self.response_msg('warning', 'AssetUpdateWarning',
                                                  "Asset component [%s]'s key field [%s] is not provided in reporting data " % (
                                                      fk, identify_field))

                        else:  # couldn't find any matches, the asset component must be broken or changed manually
                            print(
                                '\033[33;1mWarning:cannot find any matches in source data by using key field val [%s],component data is missing in reporting data!\033[0m' % (
                                    key_field_data))
                    else:
                        print('\033[31;1mMust be sth wrong,logic should goes to here at all.\033[0m')
                # compare all the components from DB with the data source from reporting data
                # 这个是看到有客户端有值但是数据表里面没有 就新增一条数据
                # 看到数据表里面有值但是客户端没有值 就删除这条数据
                # 这里用的是集合的方式
                """
                s1 = {1,2,3,4}
                s2 = {2,3,5,6}
                s1 - s2 客户端 - 服务端
                s2 - s1 服务端 - 客户端


                # s = models.Asset.objects.last()
                # s.nic_set.all() 拿到所有的nic对象
                m1 = s.nic_set.all()[0] 拿到某一个nic的记录

                m1._meta.model #'asset.models.NIC'
                m1._meta.model.objects
                m1._meta.model.objects.create
                """
                self.__filter_add_or_deleted_components(model_obj_name=component_obj.model._meta.object_name,
                                                        data_from_db=objects_from_db, data_source=data_source,
                                                        identify_field=identify_field)

                """"
                __filter_add_or_deleted_components(表名=component_obj.model._meta.object_name,
                                                        已经在数据库中找到的数据, 客户端上报数据=data_source,
                                                        唯一标识 例如macaddress=identify_field)
                """

            else:  # this component is reverse fk relation with Asset model
                pass
        except ValueError as e:
            print('\033[41;1m%s\033[0m' % str(e))

    def __filter_add_or_deleted_components(self, model_obj_name, data_from_db, data_source, identify_field):
        '''This function is filter out all  component data in db but missing in reporting data, and all the data in reporting data but not in DB'''
        """
        model_obj_name = 表名
        data_from_db 数据库中的数据
        data_source 客户端数据
        identify_field 唯一标识的字段 key
        """
        print(data_from_db, data_source, identify_field)
        data_source_key_list = []  # save all the identified keys from client data,e.g: [macaddress1,macaddress2]
        if type(data_source) is list:
            for data in data_source:
                data_source_key_list.append(data.get(identify_field))
                #[mac1,mac2,mac3] 客户端数据

        elif type(data_source) is dict: #dprecated 废弃
            for key, data in data_source.items():
                if data.get(identify_field):
                    data_source_key_list.append(data.get(identify_field))
                else:  # workround for some component uses key as identified field e.g: ram
                    data_source_key_list.append(key)
        print('-->identify field [%s] from db  :', data_source_key_list)
        print('-->identify[%s] from data source:', [getattr(obj, identify_field) for obj in data_from_db])

        data_source_key_list = set(data_source_key_list)
        #客户端数据mac 集合
        data_identify_val_from_db = set([getattr(obj, identify_field) for obj in data_from_db])
        #服务器端数据mac 集合 [mac1,mac3]
        data_only_in_db = data_identify_val_from_db - data_source_key_list  # delete all this from db
        #只在数据库中有但是客户端没有 这个就是要删掉的数据
        data_only_in_data_source = data_source_key_list - data_identify_val_from_db  # add into db
        #只在客户端有服务端没有的 就是要添加的数据
        print('\033[31;1mdata_only_in_db:\033[0m', data_only_in_db)
        print('\033[31;1mdata_only_in_data source:\033[0m', data_only_in_data_source)
        self.__delete_components(all_components=data_from_db, delete_list=data_only_in_db,
                                 identify_field=identify_field)
        #要删除的 服务端数据  删除的列表  唯一标识
        #服务端数据  删除的数据集合差  唯一标识mac
        if data_only_in_data_source:
            #如果数据只在客户端有添加
            self.__add_components(model_obj_name=model_obj_name, all_components=data_source,
                                  add_list=data_only_in_data_source, identify_field=identify_field)
            #表名 客户端网卡的一条记录数据  只在客户端的数据 唯一标识


    def __add_components(self, model_obj_name, all_components, add_list, identify_field):
        """
        model_obj_name  表名
        all_componets  客户端网卡的一条记录数据
        add_list 只在客户端的数据
        identify_field 唯一标识
        """
        model_class = getattr(models, model_obj_name)
        #modles.表名
        will_be_creating_list = []
        print('--add component list:', add_list)
        if type(all_components) is list:
            for data in all_components:
                if data[identify_field] in add_list:
                    # print data
                    will_be_creating_list.append(data)
                    #需要添加的记录
        elif type(all_components) is dict: #deprecated
            for k, data in all_components.items():
                # workround for some components uses key as identified field ,e.g ram
                if data.get(identify_field):
                    if data[identify_field] in add_list:
                        # print k,data
                        will_be_creating_list.append(data)
                else:  # if the identified field cannot be found from data set,then try to compare the dict key
                    if k in add_list:
                        data[
                            identify_field] = k  # add this key into dict , because this dict will be used to create new component item in DB
                        will_be_creating_list.append(data)

        # creating components
        try:
            for component in will_be_creating_list:
                data_set = {}
                for field in model_class.auto_create_fields:
                    #在表中 定义的 必须要创建一条的数据的字段
                    data_set[field] = component.get(field)
                    #data_set 字典 拿一条记录改有的数据
                data_set['asset_id'] = self.asset_obj.id
                #设置asset_id
                obj = model_class(**data_set)
                #插入数据
                obj.save()
                print('\033[32;1mCreated component with data:\033[0m', data_set)
                log_msg = "Asset[%s] --> component[%s] has justed added a new item [%s]" % (
                    self.asset_obj, model_obj_name, data_set)
                self.response_msg('info', 'NewComponentAdded', log_msg)
                log_handler(self.asset_obj, 'NewComponentAdded', self.request.user, log_msg, model_obj_name)

        except Exception as e:
            print("\033[31;1m %s \033[0m" % e)
            log_msg = "Asset[%s] --> component[%s] has error: %s" % (self.asset_obj, model_obj_name, str(e))
            self.response_msg('error', "AddingComponentException", log_msg)

    def __delete_components(self, all_components, delete_list, identify_field):
        '''All the objects in delete list will be deleted from DB'''
        #服务端数据  删除的列表  唯一标识
        deleting_obj_list = []
        print('--deleting components', delete_list, identify_field)
        for obj in all_components:
            #循环服务端 所有的关于 nic的记录 data_from_db
            val = getattr(obj, identify_field)
            #拿到所有的mac的地址的列表
            if val in delete_list:
                #如果在删除列表里面
                deleting_obj_list.append(obj)

        for i in deleting_obj_list:
            log_msg = "Asset[%s] --> component[%s] --> is lacking from reporting source data, assume it has been removed or replaced,will also delete it from DB" % (
                self.asset_obj, i)
            self.response_msg('info', 'HardwareChanges', log_msg)
            log_handler(self.asset_obj, 'HardwareChanges', self.request.user, log_msg, i)
            #request.user 登录用户
            i.delete()
            #删除

    def __compare_componet(self, model_obj, fields_from_db, data_source):
        """
        model_obj == 数据库里这条网卡记录对象
        fields_from_db == 要对比的字段
        data_source == 客户端的这条网卡数据
        :param model_obj:
        :param fields_from_db:
        :param data_source:
        :return:
        """
        print('---going to compare:[%s]' % model_obj, fields_from_db)
        print('---source data:', data_source)
        for field in fields_from_db:
            """
            1、取出双方的字段值
            2、统一数据类型
            3、对比
            4、根据对比结果,确定是否更新数据库
            """
            val_from_db = getattr(model_obj, field)
            # 数据库取出字段
            val_from_data_source = data_source.get(field)
            # 客户源中取出字段
            if val_from_data_source:
                # 统一数据类型 让客户端和服务器的数据类型一致 然后再比较
                # if type(val_from_db) is unicode:val_from_data_source = unicode(val_from_data_source)#no unicode in py3
                # if type(val_from_db) in (int,long):val_from_data_source = int(val_from_data_source) #no long in py3
                if type(val_from_db) in (int,):
                    val_from_data_source = int(val_from_data_source)
                elif type(val_from_db) is float:
                    val_from_data_source = float(val_from_data_source)
                elif type(val_from_db) is str:
                    val_from_data_source = str(val_from_data_source).strip()
                if val_from_db == val_from_data_source:  # this field haven't changed since last update
                    pass
                    # 如果比较以后数据端和客户端上报数据是一致的时候 就不需要做任何操作
                    # print '\033[32;1m val_from_db[%s]  == val_from_data_source[%s]\033[0m'
                    # %(val_from_db,val_from_data_source)
                else:
                    # 如果比较以后不一样
                    print('\033[34;1m val_from_db[%s]  != val_from_data_source[%s]\033[0m' % (
                        val_from_db, val_from_data_source), type(val_from_db), type(val_from_data_source), field)
                    '''
                    s = models.Asset.objects.last()
                    s.nic_set.all() 拿到所有的nic对象
                    m1 = s.nic_set.all()[0] 拿到某一个nic的记录 其实就是循环中的obj
                    m1._meta 其中有很多方法
                    字段obj = m1._meta.get_field(字段)  #获取某个字段的对象
                    字段obj.save_form_data(m1,字段的值) #就可以更新这个字段了
                    '''
                    db_field = model_obj._meta.get_field(field)
                    db_field.save_form_data(model_obj, val_from_data_source)

                    model_obj.update_date = timezone.now()
                    model_obj.save()

                    log_msg = "Asset[%s] --> component[%s] --> field[%s] has changed from [%s] to [%s]" % (
                        self.asset_obj, model_obj, field, val_from_db, val_from_data_source)
                    self.response_msg('info', 'FieldChanged', log_msg)
                    log_handler(self.asset_obj, 'FieldChanged', self.request.user, log_msg, model_obj)
            else:
                self.response_msg('warning', 'AssetUpdateWarning',
                                  "Asset component [%s]'s field [%s] is not provided in reporting data " % (
                                      model_obj, field))

        model_obj.save()


def log_handler(asset_obj, event_name, user, detail, component=None):
    '''    (1,u'硬件变更'),
        (2,u'新增配件'),
        (3,u'设备下线'),
        (4,u'设备上线'),'''
    log_catelog = {
        1: ['FieldChanged', 'HardwareChanges'],
        2: ['NewComponentAdded'],
    }
    if not user.id:
        user = models.UserProfile.objects.last()
        # user = models.UserProfile.objects.filter(is_admin=True).last()
        #这个地方是个坑,需要在User表里面创建一条数据 和 Django的UserProfile表里面的数据对应起来不然User表为空
    event_type = None
    for k, v in log_catelog.items():
        if event_name in v:
            event_type = k
            break
    log_obj = models.EventLog(
        name=event_name,
        event_type=event_type,
        asset_id=asset_obj.id,
        component=component,
        detail=detail,
        user_id=user.id
    )

    log_obj.save()
