#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from atm.core import auth
from atm.core.logger import logger
from atm.core import accounts
from atm.core import transaction
from atm.conf.settings import base_dir, LOG_TYPES

trans_logger = logger('transaction')
access_logger = logger('access')

# 临时帐号数据,保存在内存中的.
user_data = {
    'account_id': None,
    "is_authenticated": False,
    "account_data": None,
}


@auth.login_required
def account_info(acc_data):
    """
    获取的用户数据,展示出来.
    :param acc_data:
    :return: None
    """
    tmp_acc_data = acc_data
    tmp_account_data = tmp_acc_data.pop('account_data')
    tmp_account_data['password'] = "******"
    for k, v in tmp_acc_data.items():
        print("\033[33;1m{0}:{1}\033[0m".format(k, v))
    print("\033[33;1maccount_data:\033[0m")
    for a, b in tmp_account_data.items():
        print("\033[33;1m\t{0}:{1}\033[0m".format(a, b))


@auth.login_required
def repay(acc_data):
    """
    还款.
    :param acc_data:
    :return:
    """
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input("\033[33;1mInput repay amount:\033[0m").strip()
        if len(repay_amount) > 0 and repay_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger, account_data, 'repay', repay_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))
        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % repay_amount)
        if repay_amount == 'b':
            back_flag = True


@auth.login_required
def withdraw(acc_data):
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[33;1mInput withdraw amount:\033[0m").strip()
        if len(withdraw_amount) > 0 and withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger, account_data, 'withdraw', withdraw_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))
        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)

        if withdraw_amount == 'b':
            back_flag = True


@auth.login_required
def transfer(acc_data):
    dest_account = input("转到哪个帐号:").strip()
    transfer_amount = input("转多少钱:").strip()

    account_data_source = accounts.load_current_balance(acc_data['account_id'])
    account_data_dest = accounts.load_current_balance(dest_account)

    if dest_account == 'b' or transfer_amount == 'b':
        exit()

    if len(transfer_amount) > 0 and transfer_amount.isdigit():
        new_balance_source = transaction.make_transaction(trans_logger, account_data_source, 'withdraw', transfer_amount)
        new_balance_dest = transaction.make_transaction(trans_logger, account_data_dest, 'repay', transfer_amount)
        if new_balance_source:
                print('''\033[42;0mNew Balance:%s\033[0m''' % (new_balance_source['balance']))

    else:
        print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % transfer_amount)


@auth.login_required
def pay_check(acc_data):
    log_file = LOG_TYPES.get("transaction")
    with open("{0}/atm/log/{1}".format(base_dir, log_file), 'r') as f:
        log_data = f.readlines()

    for line in log_data:
        if acc_data["account_id"] in line:
            print(line, end="")


@auth.login_required
def consume(acc_data, total):
    if total > acc_data["account_data"]["balance"]:
        return "fail"

    new_balance = transaction.make_transaction(trans_logger, acc_data["account_data"], 'consume', total)
    if new_balance:
            print('''\033[32;1mNew Balance:%s\033[0m''' % (new_balance['balance']))
    else:
        print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % total)
    return True


def logout(acc_data):
    exit("see you again!")


def interactive(acc_data):
    menu = u'''
    ------- Oldboy Bank ---------
    \033[32;1m1.  账户信息
    2.  还款
    3.  取款
    4.  转账
    5.  账单
    6.  消费
    7.  退出
    \033[0m'''

    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        "6": consume,
        '7': logout,
    }

    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            menu_dic[user_option](acc_data)
        else:
            print("\033[31;1mOption does not exist!\033[0m")


def run():
    acc_data = auth.acc_login(user_data, access_logger)        # 读取的JSON文件 ,现在是个字典.
    if user_data["is_authenticated"]:
        user_data['account_data'] = acc_data    # 状态信息user_data和用户信息
        interactive(user_data)
