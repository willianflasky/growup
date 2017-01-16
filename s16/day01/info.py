#!/usr/bin/env python3

__author__='willian'

username=input("Username:")
password=input("Password:")
age=input("Age:")

info='''\033[33;1m
        ----Personal infomation----
        username: %s
        password: %s
        age:%s
\033[0m'''%(username,password,age)

if __name__=='__main__':
    print(info)
