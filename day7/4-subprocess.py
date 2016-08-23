#!/usr/bin/env python
#coding:utf8

#import subprocess
"""
#获取状态码的
ret=subprocess.call('ls -l',shell=True)
ret=subprocess.check_call('ls -l',shell=True)

#获取内容
ret=subprocess.check_output('ls -l',shell=True)


obj = subprocess.Popen("ls -l", shell=True, cwd='.',)
"""

import subprocess

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
obj.stdin.write("print(1)\n")
obj.stdin.write("print('2')")
obj.stdin.close()

cmd_out = obj.stdout.read()
obj.stdout.close()
cmd_error = obj.stderr.read()
obj.stderr.close()

print(cmd_out)
print(cmd_error)