#!/usr/bin/env python3
import getpass,os,sys
dict_passwd = {
    'admin': 'admin',
    'tom': '123456'
}

counter=0
while counter < 3:
    while True:
        username=input("username>>>").strip()
        if username == "":
                continue
        elif username == "quit" or username=='exit':
            sys.exit()
        else:
            break

    password=getpass.getpass()

    if os.path.exists('%s.lock'%username):
        sys.exit("\033[31;5myour account locked by system! contact administrator.\033[0m")
    elif username in dict_passwd.keys() and dict_passwd.get(username) == password:
        print('\033[33;5mBingo!\033[0m')
        break

    else:
        print('\033[31;1merrors %s OR %s\033[0m'%(username,password))

    counter +=1

else:
    f=open('%s.lock'%username,'w')
    f.close()