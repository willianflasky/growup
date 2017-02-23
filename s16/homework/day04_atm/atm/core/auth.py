#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import time
from atm.core import db_handler


def login_required(func):       # 装饰器验证是否登录过.
    def wrapper(*args, **kwargs):
        if args[0].get("is_authenticated"):
            return func(*args, **kwargs)
        else:
            exit("User is not authticated!")
    return wrapper


def acc_auth2(account, password):
    """
    拿着用户名和密码.通过db_handler.db_handler认证.
    :param account:
    :param password:
    :return:
    """
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where account=%s" % account)
    if data['password'] == password:
        exp_time_stamp = time.mktime(time.strptime(data['expire_date'], "%Y-%m-%d"))
        if time.time() > exp_time_stamp:
            print("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)
        else:
            return data
    else:
        print("\033[31;1mAccount ID or password is incorrect!\033[0m")


def acc_login(user_data, log_obj):
    """
    认证,拿到user_data默认字典,和日志对象.认证成功后把,user_data改成认证成功并返回json取出的用户数据.
    :param user_data:
    :param log_obj:
    :return:
    """
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3:
        account = input("account:").strip()
        password = input("password:").strip()
        auth = acc_auth2(account, password)         # 1234.json 字典
        if auth:
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            return auth
        retry_count += 1
    else:
        log_obj.error("account [%s] too many login attempts" % account)
        exit()

