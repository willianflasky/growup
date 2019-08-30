

import sys,os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "luffyEye.settings")
    import django
    django.setup()  # load all the apps
    from jumpserver.backend import user_interface

    obj = user_interface.UserInteractive(sys.argv)
    obj.start()