#!/usr/bin/env python
#coding:utf8

class SchoolMember(object):
    member_nums=0
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def enroll(self):
        SchoolMember.member_nums += 1
        print('the [%s] School Member [%s] is enrolled!'%(self.member_nums,self.name))

    def tell(self):
        print('Hello my name is %s'%self.name)

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,course,salary):
        super(Teacher,self).__init__(name,age,sex)
        self.course=course
        self.salary=salary

    def teaching(self):
        print('Teacher [%s] is teaching [%s]'%(self.name,self.course))

class Student(SchoolMember):
    def __init__(self,name,age,sex,course,tuition):
        super(Student,self).__init__(name,age,sex)
        self.course=course
        self.tuition=tuition

    def pay_tuition(self):
        print('cao,student paying [%s] tuition %s'%(self.name,self.tuition))


t1=Teacher('alex',22,'F','py',1000)
t2=Teacher('tenglan',25,'F','py',900)

s1=Student('sanjing',24,'Fe','py',15000)
s2=Student('Baoan',23,'F','py',9000)

print(t1.name)
print(s1.name)

t1.tell()


