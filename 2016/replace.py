#!/usr/bin/env python

import argparse
from configobj import ConfigObj
parser=argparse.ArgumentParser()
parser.add_argument("-s","--src",default='src.conf',help="--src=src.conf",type=str)
parser.add_argument("-d","--dest",default='dest.conf',help="--src=dest.conf",type=str)
parser.add_argument("echo",help="eg: prog.py --src=src.conf --dest=dest.conf",type=str)
args=parser.parse_args()

src_file=ConfigObj(args.src)
dest_file=ConfigObj(args.dest)

src_file.merge(dest_file)
src_file.write()

#不要空格版
#with open('a.conf','w') as f:
#    for k in src_file:
#        f.write(k+"="+src_file[k]+"\n")
