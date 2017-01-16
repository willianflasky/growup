#!/usr/bin/env python3

__author__ = "willian"

import getpass
import os
import sys

lockFile='lock.txt'
currDir=os.path.dirname(os.path.abspath(__file__))

passwd={
        'alex':'abc123',
        'tom':'abc123',
        'willian':'abc123'
        }

def checkLock(user):
    if os.path.exists(os.path.join(currDir,lockFile)):
        with open(os.path.join(currDir,lockFile),'r') as f:
            #read file and string
            data=f.read()
            data=data.split(' ')
        if user.strip() in data:
            return True
        else:
            return False
    else:
        return False

def Lock(user):
    if os.path.exists(os.path.join(currDir,lockFile)):
        with open(lockFile,'a') as f:
            f.write(" "+user)
    else:
        with open(lockFile,'w') as f:
            f.write(user)

cowsay="""
( 要惊喜，不要惊吓！ )
 -----------------
        o   ^__^
         o  (oO)\_______
            (__)\       )\/\
                
                ||----w||
                ||     ||
"""

if __name__=='__main__':
    counter=0
    while counter < 3:
        try:
            _user=input("请输入用户名:").strip()
            _pass=getpass.getpass("请输入密码:").strip()
        except KeyboardInterrupt as e:
            exit("\033[31;1m]\nBye!\n\033[0m]")

        ret=checkLock(_user)
        if ret:
            exit("\033[31;1m你的帐号被系统锁定，请联系管理员!\033[0m")
        elif len(_user) == 0  or len(_pass) == 0:
            print("用户密码不能为空!")
            continue
        else:
            if _user in passwd.keys() and _pass == passwd.get(_user):
                print("\033[34;5m\n%s\n\033[5m"%cowsay)
                exit()
            else:
                counter +=1
                continue
    else:
        Lock(_user)
        exit("\033[31;1m尝试超过3次，现在锁定你的帐号,剑人!")
        

        
