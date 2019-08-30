#_*_coding:utf-8_*_
__author__ = 'Alex Li'

from plugins.linux import sysinfo


def LinuxSysInfo():
    # print __file__
    return sysinfo.collect()


def WindowsSysInfo():
    from plugins.windows import sysinfo as win_sysinfo
    return win_sysinfo.collect()
