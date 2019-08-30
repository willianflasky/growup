#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import os
import sys

BASE_DIR = os.path.normpath(os.path.join(__file__, os.pardir, os.pardir))
sys.path.insert(0, BASE_DIR)

from core import core


def main():
    core.run()

if __name__ == '__main__':
    main()
