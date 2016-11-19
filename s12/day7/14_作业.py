#!/usr/bin/env python
#coding:utf8
#Author: willianflasky
import pickle
obj_list=[]

class Teacher(object):
    def __init__(self,name,type):
        self.name=name
        self.type=type

    def show(self):
        print(self.name)
        print(self.type)
        return 'teacher 内容'

class Course(object):
    def __init__(self,name,cost,teacher):
        self.name=name
        self.cost=cost
        self.teacher=teacher

    def show(self):
        print(self.name)
        print(self.cost)
        print("obj:---------------->",self.teacher)
        return 'course 内容'

class Student(object):
    def __init__(self,name,course):
        self.name=name
        self.course=course

    def show(self):
        print(self.name)
        print(self.course)
        return "student 内容"


class opertion(object):

    def read(self):
        f=open('14.db','rb')
        obj_list=pickle.load(f)
        f.close()

    def write(self):
        fp=open('14.db','wb')
        pickle.dump(obj_list,fp)
        fp.close()
    
if __name__ == '__main__':
    while 1:
        try:
            type_obj=input('增加(1.教师\t2.课程\t3.学生)')
            if type_obj == 'exit' or type_obj == 'quit':
                break

            elif type_obj == "1":
                while 1:
                    teacher_name=input('教师名字>')
                    teacher_type=input('教什么课程>')
                    if teacher_name == "" and teacher_type == "":
                        print("名字为空,请输入正确的值.")
                        continue
                    else:
                        temp=Teacher(teacher_name,teacher_type)
                        break

            elif type_obj == "2":
                while 1:
                    course_name=input("课程名字>")
                    course_cost=input("课程价格>")
                    course_teacher=input("课程教师>")
                    if course_name == "" and course_cost == "" and course_teacher == "":
                        print("名字为空,请输入正确的值.")
                        continue
                    else:
                        temp=Course(course_name,course_cost,course_teacher)
                        break


            elif type_obj == "3":
                while 1:
                    student_name=("学生名字>")
                    student_course=("学生的课程>")
                    if student_name == "" and student_course == "":
                        print("名字为空,请输入正确的值.")
                        continue
                    else:
                        temp=Student(student_name,student_course)
                        break
            else:
                print('只允许输入(1,2,3).')
                continue
        except Exception as ex:
            print('只允许输入(1,2,3)!')
            continue


    obj_list.append(temp)
    op=opertion()
    op.write()

    op.read()
    print(obj_list[0].name)