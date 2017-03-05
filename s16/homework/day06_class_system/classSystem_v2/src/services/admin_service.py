#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from src.models import Admin
from src.models import School
from src.models import Teacher
from src.models import Course
from src.models import Classes
from src.models import Course_to_teacher
from src.models import Student


def create_school():
    try:
        name = input("请输入学校名字: ").strip()
        addr = input("请输入学校地址: ").strip()
        school_name_list = [(obj.name, obj.addr) for obj in School.get_all_obj_list()]
        if (name, addr) in school_name_list:
            raise Exception('\033[43;1m[%s] [%s]校区 已经存在,不可重复创建\033[0m' % (name, addr))
        obj = School(name, addr)
        obj.save()
        status = True
        error = ""
        data = '\033[33;1m[%s] [%s]校区 创建成功\033[0m' % (obj.name,obj.addr)
    except Exception as e:
        status = False
        error = str(e)
        data = ""
    return {"status": status, "error": error, "data": data}


def show_school():
    for obj in School.get_all_obj_list():
        print('\033[45;1m学校[%s] 地址[%s] 创建日期[%s]\033[0m'.center(60, '-') % (obj.name, obj.addr, obj.create_time))


def create_teacher():
    try:
        name = input("请输入老师姓名: ").strip()
        level = input("请输入级别: ").strip()
        teacher_name_list = [obj.name for obj in Teacher.get_all_obj_list()]
        if name in teacher_name_list:
            raise Exception('\033[43;1m老师[%s] 已经存在,不可重复创建\033[0m' % name)
        obj = Teacher(name, level)
        obj.save()
        status = True
        error = ""
        data='\033[33;1m老师[%s] 级别[%s] 时间[%s]创建成功\033[0m' %(obj.name,obj.level,obj.create_time)
    except Exception as e:
        status = False
        error = str(e)
        data = ""
    return {"status": status, "error": error, "data": data}


def show_teacher():
    for obj in Teacher.get_all_obj_list():
        print('\033[33;1m老师[%s] 级别[%s] 创建时间[%s]\033[0m'.center(60, '-') % (obj.name, obj.level, obj.create_time))


def create_course():
    try:
        print("创建课程".center(60, "="))
        school_list = School.get_all_obj_list()
        for k, obj in enumerate(school_list):
            print(k, obj, obj.addr)
        sid = int(input("请选择学校: "))
        school_obj = school_list[sid]

        name = input('请输入课程名: ').strip()
        price = input('请输入课程价格: ').strip()
        period = input('请输入课程周期: ').strip()
        course_name_list = [(obj.name, obj.school_nid.uuid) for obj in Course.get_all_obj_list()]
        if (name, school_obj.nid.uuid) in course_name_list:
            raise Exception('\033[43;1m课程[%s] 已经存在,不可重复创建\033[0m' % name)
        obj = Course(name, price, period, school_obj.nid)
        obj.save()
        status = True
        error = ''
        data = '\033[33;1m课程[%s] 价格[%s] 周期[%s]创建成功\033[0m' % (obj.name, obj.price, obj.period)
    except Exception as e:
        status = False
        error = str(e)
        data = ""
    return {'status': status, 'error': error, 'data': data}


def show_course():
    for obj in Course.get_all_obj_list():
        print('\033[33;1m[%s] [%s]校区 [%s]课程 价格[%s] 周期[%s]\033[0m'.center(60, '-') %\
              (obj.school_nid.get_obj_by_uuid().name, obj.school_nid.get_obj_by_uuid().addr,\
               obj.name, obj.price, obj.period))


def create_course_to_teacher():
    try:
        school_list = School.get_all_obj_list()
        course_list = Course.get_all_obj_list()

        for k, school in enumerate(school_list):
            print(k, school.addr, school.name)
        sid = int(input("请输入你想关联的校区: ").strip())
        school_obj = school_list[sid]

        for k, course in enumerate(course_list):
            print(k, course.name)
        cid = int(input("请输入你想关联的课程: ").strip())
        course_obj = course_list[cid]

        course_to_teacher_list = [(obj.school_nid, obj.course_nid) for obj in Course_to_teacher.get_all_obj_list()]
        if (course_obj.nid, school_obj.nid) in course_to_teacher_list:
            raise Exception('\033[43;1m课程到老师 已经存在,不可重复创建\033[0m')

        obj = Course_to_teacher(course_obj.nid, school_obj.nid)
        obj.save()
        status = True
        error = ''
        data = '\033[33;1m课程ID[%s] 校区[%s]创建成功\033[0m' % (obj.course_nid, obj.school_nid)
    except Exception as e:
        status = False
        error = str(e)
        data = ""
    return {'status': status, 'error': error, 'data': data}


def show_course_to_teacher():
    course_to_teacher_list = [(obj.school_nid, obj.course_nid) for obj in Course_to_teacher.get_all_obj_list()]
    if len(course_to_teacher_list) == 0:
        print("not data!".center(60, '-'))

    for line in course_to_teacher_list:
        print("{0}{1} -- {2}".format(line[0].get_obj_by_uuid().addr, line[0].get_obj_by_uuid().name, line[1].get_obj_by_uuid().name))


def create_classes():
    try:
        school_list = School.get_all_obj_list()
        name = input("新班级名称: ").strip()
        tuition = input("学费: ").strip()

        for k, obj in enumerate(school_list):
            print(k, obj, obj.addr)

        sid = int(input("请选择学校: ").strip())
        school_obj = school_list[sid]
        course_to_teacher_list = Course_to_teacher.get_all_obj_list()

        obj = Classes(name, tuition, school_obj, course_to_teacher_list)
        obj.save()

        status = True
        error = ""
        data = '\033[33;1m班级名称[%s] 学费[%s] 校区[%s%s]创建成功\033[0m' % (obj.name, obj.tuition, obj.school_obj.addr, obj.school_obj.name)

    except Exception as e:
        status = False
        error = str(e)
        data = ""
    return {'status': status, 'error': error, 'data': data}


def show_classes():
    for obj in Classes.get_all_obj_list():
        print('\033[33;1m[%s]班级 [%s]学费 [%s%s]校区\033[0m' % (obj.name, obj.tuition, obj.school_obj.addr, obj.school_obj.name))


def create_student():
    try:
        classes_list = Classes.get_all_obj_list()
        name = input("学生名称: ").strip()
        age = input("年龄: ").strip()
        qq = input("QQ号: ").strip()

        for k, class_one in enumerate(classes_list):
            print(k, class_one.name)
        choice = int(input("请选择课程: ").strip())
        classes_obj = classes_list[choice]

        classes_tuple = [obj.qq for obj in Student.get_all_obj_list()]
        if qq in classes_tuple:
            raise Exception('\033[43;1m学生已经存在,不可重复创建\033[0m')

        obj = Student(name, age, qq, classes_obj)
        obj.save()
        status = True
        error = ""
        data = '\033[33;1m学生名称[%s] 班级[%s]创建成功\033[0m' % (obj.name, obj.classes_obj.name)

    except Exception as e:
        status = False
        error = str(e)
        data = ""
    return {'status': status, 'error': error, 'data': data}


def show_student():
    for obj in Student.get_all_obj_list():
        print("姓名:{0}\t年龄:{1}\t班级:{2}\t校区:{3}".format(obj.name, obj.age, obj.classes_obj.name, obj.classes_obj.school_obj.addr).center(60, '-'))


def show():
    msg = '''
        0:选项
        1:创建学校
        2:查看学校
        3:创建老师
        4:查看老师
        5:创建课程
        6:查看课程
        7:关联老师与课程
        8:查看关联老师与课程
        9:创建班级
        10:查看班级
        11:创建学生
        12:查看学生
        13:退出
    '''
    print(msg)


def main():
    choice_dic = {
        '0': show,
        '1': create_school,
        '2': show_school,
        '3': create_teacher,
        '4': show_teacher,
        '5': create_course,
        '6': show_course,
        '7': create_course_to_teacher,
        '8': show_course_to_teacher,
        '9': create_classes,
        '10': show_classes,
        '11': create_student,
        '12': show_student,
        '13': exit,
    }
    show()

    while True:
        choice = input("请输入选项: ").strip()
        if choice not in choice_dic:
            continue
        ret = choice_dic[choice]()
        if ret:
            if ret['status']:
                print(ret['data'].center(60, '-'))
            else:
                print(ret['error'].center(60, '-'))


def login():
    ret = Admin.login()
    if ret:
        if ret['status']:
            print(ret['data'].center(60, '-'))
        else:
            print(ret['error'].center(60, '-'))


if __name__ == '__main__':
    main()
