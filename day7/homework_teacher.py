#!/usr/bin/env python
#coding:utf8
import pickle
teacher_list=[]
class Teacher(object):
    def __init__(self,favor,name,age):
        self.favor=favor
        self.name=name
        self.age=age
        self.asset=0

    def down(self):
        self.asset = self.asset - 1

    def gain(self,value):
        self.asset = self.asset + 5


tom=Teacher('reading','tom',28)
alex=Teacher('speak','alex',29)

teacher_list.append(tom)
teacher_list.append(alex)



if __name__=='__main__':
    while 1:
        ret=input('请输入新增加老师的信息(Y/N):')
        if ret == '':
            continue
        elif ret == 'Y' or ret == 'y':
            favor=input('爱好:')
            name=input('名字:')
            age=input('年龄:')
            break
        else:
            exit(1)

    name=Teacher(favor,name,age)
    teacher_list.append(name)

    f=open('user.db','wb')
    pickle.dump(teacher_list,f)
    f.close()