#!/usr/bin/env python3
# -*-coding:utf8-*-
# __author__ = "willian"

import os
import sys

def main():
    """this is main def."""
    arg = sys.argv[1:]
    arg_len = len(arg)
    if arg_len != 3:
        print("\033[31;1m需要3个参数,你只给{0}个({1} old_string new_string file.txt)\033[0m".format(arg_len, sys.argv[0]))
        exit()
    else:
        if os.path.exists(sys.argv[-1]):
            f1 = open(sys.argv[-1], 'r+')
            f2 = open("{0}.temp".format(sys.argv[3]), 'w')
            for line in f1:
                line = line.replace(sys.argv[1], sys.argv[2])
                f2.write(line)
                f2.flush()
            f1.close()
            f2.close()

            f1_size = os.path.getsize(sys.argv[-1])
            f2_size = os.path.getsize("{0}.temp".format(sys.argv[-1]))
            if f1_size == f2_size:
                os.remove(sys.argv[-1])
                os.renames("{0}.temp".format(sys.argv[-1]), sys.argv[-1])
            else:
                print("\033[31;1m文件替换出错!\033[0m")
                exit()
        else:
            print("\033[31;1m[{0}]\033[0m文件不存在.".format(sys.argv[-1]))

if __name__ == '__main__':
    main()