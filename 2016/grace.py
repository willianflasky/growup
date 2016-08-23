#!/usr/bin/env python
#2016-07-08
#by wei

import os,sys
import argparse
import commands

nginxs=["10.2.1.11","10.2.2.11"]
config_file="/etc/nginx/www.conf"
port="8080"

parser=argparse.ArgumentParser()
parser.add_argument("--active",help="eg:(on|off)")
parser.add_argument("--host",help="eg:10.0.3.11,10.0.3.12")
args=parser.parse_args()

if args.active == None or args.host == None:
    print("\033[31;1mexample:\033[0m")
    print("\033[31;1m\tpython %s --active=on|off --host=10.0.1.1,10.0.1.2\033[0m\n"%sys.argv[0])
    exit()

hosts=args.host.split(',')

def main(nginx):
    #eg:    on (#    server)
    #eg:    off(     server)
    if args.active=="on":
        for host in hosts:
            ret=commands.getstatusoutput('ssh %s sed -i "/%s:%s/s/^#*//g %s"'%(nginx,host,port,config_file))
            if ret[0] == 0:
                print("\033[32;1m%s\tok\033[0m"%host)
            else:
                print(host+"failure\n"+ret[1])

    elif args.active=='off':
        for host in hosts:
            ret=commands.getstatusoutput('ssh %s sed -i "/%s:%s/s/^/#/g" %s'%(nginx,host,port,config_file))
            if ret[0] == 0:
                print("\033[32;1m%s\tok\033[0m"%host)
            else:
                print(host+"failure\n"+ret[1])
    else:
        print("\033[31;1merror --active=on|off\033[0m")

def check(nginx):
    ret=commands.getstatusoutput('ssh %s nginx -t'%nginx)
    if ret[0] == 0:
        print("\033[33;1mngx:%s\tok\033[0m"%nginx)
        commands.getstatusoutput('ssh %s nginx -s reload'%nginx)
    else:
        print("\033[34;1m%s\tfailure\033[0m"%nginx)

if __name__ == '__main__':
    for nginx in nginxs:
        main(nginx)
        check(nginx)
