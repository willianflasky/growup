#!/usr/bin/env python
#decoding=utf8
"""
content:
1.yum,epel
2.iptables
3.sysctl.conf
4.ulimit
5.selinux
6.history

support:CentOS_6.5,CentOS_7.2
version:0.2
"""
msg="""
#sysctl.conf tuning arguments.
net.ipv4.ip_forward = 0
net.ipv4.conf.default.rp_filter = 1
net.ipv4.conf.default.accept_source_route = 0
kernel.sysrq = 0
kernel.core_uses_pid = 1
net.ipv4.tcp_syncookies = 1
kernel.msgmnb = 65536
kernel.msgmax = 65536
kernel.shmmax = 68719476736
kernel.shmall = 4294967296
net.ipv4.tcp_max_tw_buckets = 20000
net.ipv4.tcp_sack = 1
net.ipv4.tcp_window_scaling = 1
net.ipv4.tcp_rmem = 4096 87380 4194304
net.ipv4.tcp_wmem = 4096 16384 4194304
net.core.wmem_default = 8388608
net.core.rmem_default = 8388608
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.core.netdev_max_backlog = 262144
net.core.somaxconn = 65535
net.ipv4.tcp_max_orphans = 3276800
net.ipv4.tcp_max_syn_backlog = 262144
net.ipv4.tcp_timestamps = 0
net.ipv4.tcp_synack_retries = 1
net.ipv4.tcp_syn_retries = 1
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_mem = 94500000 915000000 927000000
net.ipv4.tcp_fin_timeout = 20
net.ipv4.tcp_keepalive_time = 60
net.ipv4.ip_local_port_range = 1024 65000
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.icmp_echo_ignore_broadcasts = 1
"""
limit_msg="""
*               soft    nofile          65535
*               hard    nofile          65535
*               soft    nproc           65535
*               hard    nproc           65535
"""
import os,sys,time
import subprocess
import re
import hashlib

#install wget
if not os.path.exists('/usr/bin/wget'):
	ret=subprocess.Popen('yum install wget -y',shell=True,stderr=subprocess.PIPE)
	if ret.stderr.read():
		print("安装wget失败.")
		exit()
	else:
		print("wget安装成功.")
else:
	pass	

#base class.
class Init(object):
	"""
	this is init system scripts,use OOP.
	"""
	def __init__(self):
		self.BaseDir=os.path.dirname(os.path.abspath(__file__))
		self.NewYum="CentOS6-Base-163.repo"
		self.OldYum="CentOS-Base.repo"
		self.CurrTime=time.strftime("%Y%m%d_%H%M%S",time.localtime())
	
	@property
	def InitYum(self):
		p=subprocess.Popen('wget http://mirrors.163.com/.help/%s -O %s/%s'%(self.NewYum,self.BaseDir,self.NewYum),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		time.sleep(2)
		if os.path.exists("%s/%s"%(self.BaseDir,self.NewYum)):
			r=os.stat('%s/%s'%(self.BaseDir,self.NewYum))
			if r.st_size != 0:
				print("\033[32;1mdownload success!\033[0m")
			else:
				sys.exit("\033[31;1m download error,size 0\033[0m")
		else:
			sys.exit("\033[31;1mdownload failure!\033[0m")
		
		if os.path.exists('/etc/yum.repos.d/%s'%self.OldYum):
				try:
					os.renames("/etc/yum.repos.d/%s"%self.OldYum,'/etc/yum.repos.d/%s.%s'%(self.OldYum,self.CurrTime))
					os.renames('%s/%s'%(self.BaseDir,self.NewYum),'/etc/yum.repos.d/%s'%self.NewYum)
				except Exception as e:
					print("\033[32;1mRenamesError:\033[0m",e)
	
		else:
			if os.path.exists('/etc/yum.repos.d/%s'%self.NewYum):
				print("\033[32;1m[%s] already exists!\033[0m"%self.NewYum)
			else:
				try:
					os.renames("%s/%s"%(self.BaseDir,self.NewYum),"/etc/yum.repos.d/%s"%self.NewYum)
				except Exception as e:
					print("\033[32;1mRenamesError1:\033[0m",e)
			
	def InitIptables(self,os_version):
		if os_version == 7:
			p=subprocess.Popen('systemctl disable firewalld.service;systemctl stop firewalld.service',shell=True,stderr=subprocess.PIPE)
		elif os_version == 6:
			p=subprocess.Popen('service iptables stop;service ip6tables stop;chkconfig iptables off;chkconfig ip6tables off;',shell=True,stderr=subprocess.PIPE)
		if p.stderr.read():
			print("\033[31;1miptables error [CentOS %s]!\033[0m"%os_version)
		else:
			print("\033[32;1miptables stop success [CentOS %s]!\033[0m"%os_version)
	@property
	def InitSysctl(self):
		MD5Value="cdc3a773f222fa7a7dd0bde925c3da87"
		def MD5Check(file):
			try:
       		 		f=open(file,'rb')
			except Exception as e:
				print("\033[31;1mMD5 /etc/sysctl.conf Error:\033[0m",e)
       	 		md5=hashlib.md5()
       	 		md5.update(f.read())
       	 		ret=md5.hexdigest()
			f.close()
			return ret

		result=MD5Check("/etc/sysctl.conf")
		if result == MD5Value:
			print("\033[32;1malready changed.\033[0m")
		else:
			try:
				os.renames("/etc/sysctl.conf","sysctl.conf_%s"%self.CurrTime)
				with open('/etc/sysctl.conf','w') as f:
					f.write(msg)
			except Exception as e:
				print("\033[31;1mRenames /etc/sysctl.conf Error:",e)
				exit()
			print("\033[32;1msysctl backup success!\033[0m")

	@property
	def InitUlimit(self):
		try:
			f=open('/etc/security/limits.conf','r')
		except Exception as e:
			print("\033[31;1mNot found limits.conf,open error!\033[0m",e)

		data=f.readlines()
		temp=[]
		p=re.compile(r'^\*')
		for i in data:
			if p.findall(i):
				temp.append(i)
			else:
				pass

		if len(temp) == 0:
			print("\033[32;1mdefault ulimit,change success!\033[0m")
			data.append(limit_msg)
			try:
				os.renames("/etc/security/limits.conf","/etc/security/limits.conf_%s"%self.CurrTime)
				f=open('/etc/security/limits.conf','w')
				f.writelines(data)
			except Exception as e:
				print("\033[31;1m Renames /etc/security/limits.conf Error:\033[0m",e)
				exit()
			print("\033[32;1m/etc/security/limits.conf success.")


		elif len(temp) >= 4:
			print("\033[32;1malready tuning!\033[0m")
		else:
			print("\033[31;1mlimits.conf set a part,check it please!\033[0m")
	@property
	def InitSelinux(self):
		p=subprocess.Popen("sed -i '7d' /etc/sysconfig/selinux && sed  -i '/disabled/a SELINUX=disabled' /etc/sysconfig/selinux",shell=True,stderr=subprocess.PIPE)
		if p.stderr.read():
			print("\033[31;1mselinux change error!\033[0m")
		else:
			print("\033[32;1mselinux success!\033[0m")

	@property
	def InitHistory(self):
		if not os.path.exists('/etc/profile.d/history.sh'):
			with open('/etc/profile.d/history.sh','w') as f:
				f.write('export HISTTIMEFORMAT="%F %T `whoami` "')
		else:
			print("\033[32;1m/etc/profile.d/history.sh already exists!\033[0m")
	@property
	def InitInstall(self):
		p=suprocess.Popen('yum install gcc openssl openssl-devel cmake sysstat mlocate lrzsz ntp nethogs iftop htop iotop -y',shell=True,stderr=subprocess.PIPE)
		if p.stderr.read():
			print("\033[31;1m install iftop htop iotop ....\033[0m")
		else:
			print("\033[32;1m install success!\033[0m")

	def __str__(self):
		return " :) www.classin.com"

if __name__ =='__main__':
	if len(sys.argv) <=1:
		print("\033[31;1musage: %s [-h] [-v VERSION]\n\033[0m"%sys.argv[0])
		exit()
	import argparse
	parser=argparse.ArgumentParser()
	parser.add_argument('-v',"--version",help="--version=7",type=int)
	args=parser.parse_args()

	if args.version == 7:
		eeo=Init()
		eeo.InitYum
		eeo.InitIptables(7)
		eeo.InitSysctl
		eeo.InitUlimit
		eeo.InitSelinux
		eeo.InitHistory
	
	elif args.version == 6:
		eeo=Init()
                eeo.InitYum
                eeo.InitIptables(6)
                eeo.InitSysctl
                eeo.InitUlimit
                eeo.InitSelinux
                eeo.InitHistory

	else:
		print("\033[31;1mNot support other OS Version!\033[0m")
		
