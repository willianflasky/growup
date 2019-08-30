#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import subprocess

res = subprocess.Popen("pwd", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd="/")
print(res.stdout.read())

# res.poll()
# res.terminate()
# res.wait()

subprocess.getstatusoutput("ls")

