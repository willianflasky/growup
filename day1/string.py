#!/usr/bin/env python3

name=input("name:").strip()
sex=int(input("sex:").strip())
dep=input("deportment:").strip()


msg="""\033[30m
    information %s
    name:%s
    sex:%d
    dep:%s\033[0m
"""%(name,name,sex,dep)

print(msg)