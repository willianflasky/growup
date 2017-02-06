#!/usr/bin/python
# -*-coding:utf8-*-
# psutil support python2.7+
# log_dir: /var/log/sys.argv[0]
# echo "content" |mail -s "heartbeatFO" biao.wei@eeoa.com

__author__ = 'weibiao'

import os
import sys
import re
import time
import logging
import commands
import signal

# variables
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = sys.argv[0].split('.')[0]
LOCKFILE = "%s/%s.lock"%(BASE_DIR,FILENAME)
VIP = ['10.0.0.18','10.0.0.19']
SERVICE = ['nginx','http','openresty']
TIMEOUT = 2
MOUNT_DIR = "/data/web/upload"
LOGFILE = "%s/%s.log"%(BASE_DIR,FILENAME)
MAILS = ['biao.wei@eeoa.com',]
PID = "%s/%s.pid"%(BASE_DIR,FILENAME)

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=LOGFILE,
                filemode='a')

def sendMail(MAILS,STATUS):
	for mail in MAILS:
		print("send mail done!")
	#	ret=os.popen('echo "stop heartbeat,FO %s!" |mail -s "heartbeat:FO" %s'%(STATUS,mail)).read()
	#	if ret:
	#		logging.warning('sendMail failed!')

class checkResource(object):
	def checkAddress(self,address):
		reip=re.compile(address)
		ipaddr=os.popen('ip addr').read()
		data=reip.findall(ipaddr)
		if data:
			return data
		else:
			return None

	def checkService(self,name):
		re_name=re.compile(name)
		p=os.popen('ps aux').read()	
		data=re_name.findall(p)
		if data:
			return data
		else:
			return None
	def checkNFS(self,path):
		return os.path.ismount(path)
	
	def stopHB(self):
		ret=commands.getstatusoutput('/etc/init.d/heartbeat stop')
		if ret[0] == 0:
			logging.warning("stop heartbeat,FO success.")
			sendMail(MAILS,'success')
			print("send mail!") 
		else:
			sendMail(MAILS,'failed')
			logging.warning("stop heartbeat,FO failed")

def main():
	while True:
		obj=checkResource()
		for ip in VIP:
			ret=obj.checkAddress(ip)
			if ret==None:
				logging.warning("%s lost"%ip)
				obj.stopHB()
			else:
				pass
				#print(ip,'ok')
		
		for name in SERVICE:
			ret=obj.checkService(name)
			if ret==None:
				logging.warning("%s stoped"%name)
				obj.stopHB()
			else:
				pass
				#print(name,'ok')
	
		ret=obj.checkNFS(MOUNT_DIR)
		if ret:
			pass
			#print(MOUNT_DIR,'ok')
		else:
			logging.warning("%s lost"%MOUNT_DIR)
			obj.stopHB()
		time.sleep(TIMEOUT)


def running():
	# create - fork 1
	try:
		if os.fork() > 0:os._exit(0) # exit father…
	except OSError, error:
		print 'fork #1 failed: %d (%s)' % (error.errno, error.strerror)
		os._exit(1)
    	# it separates the son from the father
	os.chdir('/')
	os.setsid()
	os.umask(0)
	# create - fork 2
	try:
		pid = os.fork()
		if pid > 0:
			print 'Daemon PID %d' % pid
			with open(PID,'w') as f:
				f.write(str(pid))
			os._exit(0)
	except OSError, error:
		print 'fork #2 failed: %d (%s)' % (error.errno, error.strerror)
		os._exit(1)
	main()


if __name__=='__main__':
	r1=run(PID)
