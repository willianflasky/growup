#!/usr/bin/env python3

"""
#一个参数
def single(user):
    print(user)

single('tom')

#两个参数
def double(a1,a2):
    print(a1,a2)
double(100,200)

#默认参数
def tom(a1=123,a2=999):
    print(a1,a2)
tom(123,456)

def show(a1=3,a2=1001):
    print(a1,a2)

show(a2=700,a1=123)
"""

#动态参数
#一个*必须放在前面,两个**必须放在后面,传参数数时,也必须一个星放在前面.

def show(*args,**kwargs):
    print(args,type(args))
    print(kwargs,type(kwargs))

#show(1,2,3,n1='tom',n2='tony')
l=[11,22,33]
k={'1':'tom','2':'tony'}
#show(*l,**k)


"""
#example    *
s1 ="{0} is {1}"
l=['alex','teacher']
#result=s1.format('alex','teacher')
result=s1.format(*l)
print(result)


#example    **
s1 = "{name} is {acter}"
d = {'name':'alex','acter':'teacher'}
#result= s1.format(name='alex',acter='teacher')
result=s1.format(**d)
print(result)


def func(a):
    a +=1
    return a
result=func(4)
print(result)

f= lambda a: a+1
ret = f(99)
print(ret)

print(bytearray('王',encoding='utf8'))
print(bytes('王',encoding='utf8'))
bool('')
all(["",None,{},[]])
f= lambda a: a+1
callable(f) #可调用,
chr(97)
ord('a')
#compile()

#enumerate
li=['alex','tom','lily']
for i,item in enumerate(li,1):
    print(i,item)

#eval
memory="6*8"
print(eval(memory))

#map
li=[11,22,33,44]
def func(x):
    return x + 100

new_li=map(func,li)
print(list(new_li))

#filter
li=[11,22,33,44]
def f(x):
    if x > 33:
        return True
    else:
        return False
n=filter(f,li)
print(list(n))

f= open('test.log','r',encoding='utf-8')
print(f.tell())
ret=f.read(2)
print(f.tell())
f.close()
print(ret)
"""
import json
s='{"k1":"v1"}'
dic=json.loads(s)
print(type(s))
print(type(dic))
print(s)
print(dic)