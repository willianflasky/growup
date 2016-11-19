#!/usr/bin/env python3

import os

from day5.dj.backend.db.sql_api import select

def home():
    print("wellcome to home page")
    q_data=select('user','ddd')
    print('quer res:',q_data)
def movie():
    print("wellcome to movie page")
def tv():
    print("wellcome to tv page")


