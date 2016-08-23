#!/usr/bin/env python
#coding:utf8
import pickle

from homework_teacher import Teacher
from homework_course import Course

class Student(object):
    def __init__(self,name,age,sex,course):
        self.name=name
        self.age=age
        self.sex=sex
        self.course=course

    def optionCourse(self):
        print("今天学习课程:%s\t"%(self.course.course))


    def tostudy(self):
        print('on classing 老师:%s \t cost:%s'%(self.course.teacher.name,self.course.course_cost))



f=open('cousre.db','rb')
student_list=pickle.load(f)
f.close()

weibiao=Student('weibiao',28,'man',student_list[0])

weibiao.optionCourse()
weibiao.tostudy()

