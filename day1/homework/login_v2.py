#!/usr/bin/env python3
import getpass,os,sys
configFile="login_userpass"
counter = 0
#open file get data
with open(configFile,'r') as f:
    data=f.readlines()

#verfy user and password
def checkUserPass(user,passwd):
    for i in data:
        us,pw,lk=i.split('\t')[0],i.split('\t')[1],i.split('\t')[2]
        if user == us and passwd==pw:
            if lk.strip() == '0':

                return 0
            else:
                return 2
    else:
        return 1

def checkExistUser(user):
    result=[]
    for i in data:
        result.append(i.split('\t')[0])
    if user in result:
        return 0
    else:
        return 1

def writeBack():
    writeBack_temp=""
    with open('login_userpass1','w') as f:
        for i in data:
            writeBack_temp=writeBack_temp+i
        f.write(writeBack_temp)


if __name__ == '__main__':
    while True:
        while True:
            user = input("Input username:").strip()
            if user == '':
                continue
            elif user == 'quit' or user=='exit':
                sys.exit()
            elif checkExistUser(user) == 1:
                print('\033[31;1mUsername is not exist!\033[0m')
                continue
            else:
                break
        passwd= getpass.getpass(prompt='password:')
        if checkUserPass(user,passwd) == 1:
            print('\033[31;1merror username or password !!\033[0m')
        elif checkUserPass(user,passwd) == 2:
            print('\033[31;1mYour account is locked!\033[0m')
        else:
            print('\033[32;5mWelcome to you!\033[0m')
            break
