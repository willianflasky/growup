#!/usr/local/env python3

import pickle,json,sys,os

#pickle支持更多的格式
#json只支持kv

"""
f=open('user_acc.txt','wb')

f.write(b'test')    #只能写二进制和字符串
f.write(b'123')
f.close()
"""
f=open('user_acc.txt','w')

info={

    "alex":"123",
    "jack":"4444"
}
json.dump(info,f)
#f.write(json.dumps(info))
f.close()

