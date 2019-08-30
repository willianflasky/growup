

import os
import sys

BASE_DIR = os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir, os.pardir))
sys.path.append(BASE_DIR)

from core import main

if __name__ == "__main__":
    try:
        main.ArvgHandler()
    except KeyboardInterrupt as e:
        print(e, "\n \033[31;1m stop done!\033[0m")



