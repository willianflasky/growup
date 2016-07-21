#!/usr/bin/env python
"""
    2016.6.17
"""
import argparse
import os,sys
import requests
import commands
import time
import logging

#config
baseDir=os.path.dirname(os.path.abspath(__file__))  #/tmp
fileName=os.path.basename(__file__)
result=[]
mobiles=["13552791537"]
timeout=5

#logging code
logging.basicConfig(level=logging.DEBUG,
                format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
                datefmt="%a,%d %b %Y %H:%M:%S",
                filename="%s/%s.log"%(baseDir,fileName),
                filemode='a')


#argparse code
parser=argparse.ArgumentParser()
parser.add_argument("-c","--conf",help="--conf=ip.conf",type=str)
args=parser.parse_args()

#if code
if len(sys.argv) == 1:
    print "Give 1 parameter at least! \n"
    exit()
else:
    pass

try:
    with open(args.conf,'r') as f:
        file=f.readlines()
except Exception,e:
    print "not found config file %s.\n%s"%(args.conf,e)
    exit()

for line in file:
    if line.startswith('10'):
       result.append(line.strip())

if len(result)==0:
    sys.exit('list is null.')

#sms
def sms(mobile,ip,port):
    cmd_sms="/bin/sh %s/sendsms.sh %s Host:%s Port:%s"%(baseDir,mobile,ip,port)
    os.system(cmd_sms)

def mulit_sms(ip,port):
    for mobile in mobiles:
        sms(mobile,ip,port)

#main
def monit_tcp(ip,port):
    cmd="nc -v -w 5 -z %s %s"%(ip,port)
    ret=commands.getstatusoutput(cmd)
    if ret[0] != 0:
        time.sleep(timeout)
        retry=commands.getstatusoutput(cmd)
        if retry[0] != 0:
            mulit_sms(ip,port)
            logging.info("Host:%s Port:%s DOWN."%(ip,port))
        else:
            pass
    else:
        pass

if __name__=='__main__':
    while 1:
        time.sleep(30)
        for addr in result:
            ret=addr.split(':')
            monit_tcp(ret[0],ret[1])
