#_*_coding:utf-8_*_
__author__ = 'Alex Li'

from plugins import plugin_api
import json, platform, sys


class InfoCollection(object):
    def __init__(self):
        pass

    def get_platform(self):
        os_platform = platform.system()
        return os_platform

    def collect(self):
        os_platform = self.get_platform()   # 获取平台
        try:
            func = getattr(self,os_platform)  # 继续用反射,支持Linux  and  Windows
            info_data = func()                # 获取数据
            formatted_data = self.build_report_data(info_data)  # 目前什么也没有,留下一接口,可以格式化.
            return formatted_data
        except AttributeError as e:
            sys.exit("Error:MadKing doens't support os [%s]! " % os_platform)

    def Linux(self):
        sys_info = plugin_api.LinuxSysInfo()     # 使用插件方式,留有接口,可以使用其它平台.
        return sys_info

    def Windows(self):
        """插件的方式调用"""
        sys_info = plugin_api.WindowsSysInfo()
        print(sys_info)
        # f = file('data_tmp.txt','wb')
        # f.write(json.dumps(sys_info))
        # f.close()
        return sys_info

    def build_report_data(self, data):
        # add token info in here before send
        return data
