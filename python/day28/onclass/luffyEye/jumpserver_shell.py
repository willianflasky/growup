

import sys
import os

if __name__ == "__main__":
    # django环境变量, 加上下面三行,就能像python3 manage shell
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "luffyEye.settings")
    import django
    django.setup()  # load all the apps

    from jumpserver.backend import user_interface

    obj = user_interface.UserInteractive(sys.argv)
    obj.start()
