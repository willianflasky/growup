#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
from conf.settings import *
from lib import mysql_helper


class Manage(object):
    conn = mysql_helper.MySQLHandler(db_host, db_port, db_user, db_pass, db_name)

    @classmethod
    def select_user(cls):
        result = cls.conn.select("select id,username from {0}", 'users')
        for line in result:
            print("\033[32;1mId:{0}\tUsername:\t{1}\033[0m".format(line['id'], line['username']))
        print("\033[34;1mtotal:{0}\n\033[0m".format(len(result)))

    @classmethod
    def select_host(cls):
        result = cls.conn.select("select id,ip from {0}", 'hosts')
        for line in result:
            print("\033[32;1mid:{0} ip:{1}\033[0m".format(line['id'], line['ip']))
        print("\033[34;1mtotal:{0}\n\033[0m".format(len(result)))

    @classmethod
    def select_user_host(cls):
        total = 0
        result_user_id = cls.conn.select("select id,username from {0}", 'users')
        for line in result_user_id:
            print("\033[32;1m{0}\033[0m".format(line['username']))
            result_host = cls.conn.select("select h.ip from hosts as h right join users2hosts as uh on h.id = uh.hosts_id where uh.users_id = {0};", line['id'])
            total += len(result_host)
            for host in result_host:
                print("\033[32;1m\tIP:{0}\033[0m".format(host['ip']))
        print("\033[34;1mtotal:{0}\n\033[0m".format(total))

    @classmethod
    def insert_user(cls):
        username = input("[username]").strip()
        password = input("[passowrd]").strip()
        cls.conn.insert('insert into users(username,password,usertype_id) values(%s, %s, 2)', username, password)

    @classmethod
    def insert_host(cls):
        ip = input("[ip]").strip()
        port = input('[port]').strip()
        username = input("[username]").strip()
        password = input("[passowrd]").strip()
        cls.conn.insert('insert into hosts(ip,port,username,password) values(%s, %s, %s, %s)', ip, port, username, password)

    @classmethod
    def insert_user_host(cls):
        user_id = input("[user_id]").strip()
        host_id = input("[host_id]").strip()
        cls.conn.insert('insert into users2hosts(users_id,hosts_id) values(%s, %s)', user_id, host_id)

    @classmethod
    def update_user(cls):
        username = input("[username]").strip()
        new_password = input("[new password]").strip()
        username = cls.conn.select("select id from users where username='{0}'", username)
        cls.conn.update("update users set password=%s where id=%s", new_password, username[0]['id'])

    @classmethod
    def update_host(cls):
        ip = input("[ip]").strip()
        new_password = input("[new ip]").strip()
        ip = cls.conn.select("select id from hosts where ip='{0}'", ip)
        cls.conn.update("update hosts set ip=%s where id=%s", new_password, ip[0]['id'])

    @classmethod
    def delete_user(cls):
        pass
        # username = input('[username]').strip()
        # username = cls.conn.select("select id from users where username='{0}'", username)
        # cls.conn.delete("delete from users where id = %s", username[0]['id'])

