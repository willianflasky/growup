#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import os
BASE_DIR = os.path.normpath(os.path.join(__file__, os.pardir, os.pardir))

ADMIN_DB_DIR = os.path.join(BASE_DIR, 'db', 'admin')
SCHOOL_DB_DIR = os.path.join(BASE_DIR, 'db', 'school')
TEACHER_DB_DIR = os.path.join(BASE_DIR, 'db', 'teacher')
COURSE_DB_DIR = os.path.join(BASE_DIR, 'db', 'course')
COURSE_TO_TEACHER_DB_DIR = os.path.join(BASE_DIR, 'db', 'course_to_teacher')
CLASSES_DB_DIR = os.path.join(BASE_DIR, 'db', 'classes')
STUDENT_DB_DIR = os.path.join(BASE_DIR, 'db', 'student')
