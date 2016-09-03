#!/usr/bin/env python
import os,sys

BASE_DIR=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
from myftp.conf import user
prog='myftp'
with open('{0}/{1}/conf/user.py'.format(BASE_DIR,prog),'r') as f:
    data=f.readlines()

