#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
from lib import ssh_helper


def worker(arg, cmd):
    obj = ssh_helper.SshHelper(arg['ip'], arg['port'], arg['username'], arg['password'])
    obj.connect()
    obj.cmd(cmd)


class cmdHandler(object):
    @staticmethod
    def upload(arg, local, target):
        obj = ssh_helper.SshHelper(arg['ip'], arg['port'], arg['username'], arg['password'])
        obj.connect()
        obj.upload(local, target)
