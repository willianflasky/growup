#!/usr/bin/env python
#coding:utf8

import pickle
from homework_teacher import Teacher
course_list=[]
f=open('user.db','rb')
t_list=pickle.load(f)
f.close()

class Course(object):
    def __init__(self,course_name,course_cost,teacher):
        self.course=course_name
        self.course_cost=course_cost
        self.teacher=teacher

    def study(self):
        print('studying')
        self.teacher.gain()



if __name__=='__main__':
    python=Course('python',3000,t_list[0])
    bigdata=Course('bigdata',4000,t_list[1])

    course_list.append(python)
    course_list.append(bigdata)

    op=open('cousre.db','wb')
    pickle.dump(course_list,op)
    op.close()


