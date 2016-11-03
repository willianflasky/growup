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

support:CentOS_6.5
version:20161103
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
vm.overcommit_memory=1
"""
limit_msg="""
*               soft    nofile          65535
*               hard    nofile          65535
*               soft    nproc           10240
*               hard    nproc           10240
"""
import os,sys,time
import subprocess
import re
import hashlib

#check OS version.
os_version="CentOS release 6.5 (Final)\n"

def diff(n):
	ret=hashlib.new('md5')
	ret.update(n)
	return ret.hexdigest()

try:
	with open('/etc/redhat-release') as f:
		data=f.read()
	
	old=diff(os_version)
	new=diff(data)
	if old == new:
		print("\033[33;1mit greet! support your OS!\t%s\033[0m"%os_version)
	else:
		print("\033[31;1mCaution:only support CentOS_6.5!\033[0m")
		sys.exit()
except Exception as e:
	print("\033[31;1mYou may not be CentOS!\tonly support CentOS_6.5\033[0m")
	sys.exit()

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
			print("\033[32;1mdownload success!\033[0m")
		else:
			sys.exit("\033[31;1mdownload failure!\033[0m")
		
		if os.path.exists('/etc/yum.repos.d/%s'%self.OldYum):
				R1=subprocess.Popen('mv /etc/yum.repos.d/%s /etc/yum.repos.d/%s.%s'%(self.OldYum,self.OldYum,self.CurrTime),shell=True,stderr=subprocess.PIPE)
				R2=subprocess.Popen('mv %s/%s /etc/yum.repos.d/%s'%(self.BaseDir,self.NewYum,self.NewYum),shell=True,stderr=subprocess.PIPE)
				if len(R1.stderr.read()) == 0 and len(R2.stderr.read()) == 0:
					print('\033[32;1myum success!\033[0m')
				else:
					print("\033[31;1mmv error!\033[0m")
		else:
			if os.path.exists('/etc/yum.repos.d/%s'%self.NewYum):
				print("\033[32;1m%s exists!\033[0m"%self.NewYum)
			else:
				R3=subprocess.Popen('mv %s/%s /etc/yum.repos.d/%s'%(self.BaseDir,self.NewYum,self.NewYum),shell=True,stderr=subprocess.PIPE)
				if len(R3.stderr.read()) == 0:
        	        		print('\033[32;1myum success!\033[0m')
        			else:
                			print("\033[31;1mmv error 2!\033[0m")
		

		if not os.path.exists('/etc/yum.repos.d/epel.repo'):
			p=subprocess.Popen('rpm -ivh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm',shell=True,stderr=subprocess.PIPE)
			if p.stderr.read():
				print("\033[31;1mrpm install epel error!\033[0m")
			else:
				print("\033[32;1minstall epel success!\033[0m")
		else:
			print('\033[32;1malready exists epel!\033[0m')
	@property
	def InitIptables(self):
		p=subprocess.Popen('chkconfig iptables off;chkconfig ip6tables off;service iptables stop; service ip6tables stop;',shell=True,stderr=subprocess.PIPE)
		if p.stderr.read():
			print("\033[31;1miptables error!\033[0m")
		else:
			print("\033[32;1miptables stop success!\033[0m")
	@property
	def InitSysctl(self):
		r1=subprocess.Popen('mv /etc/sysctl.conf /etc/sysctl.conf_%s'%self.CurrTime,shell=True,stderr=subprocess.PIPE)
		if r1.stderr.read():
			sys.exit("\033[31;1msysctl.conf backup error!\033[0m")
		else:
			try:
				with open('/etc/sysctl.conf','w') as f:
					f.write(msg)
			except Exception as e:
				print("\033[31;1mNot found sysctl.conf,open error1")
				print(e)
				sys.exit()
			print("\033[32;1msysctl backup success!\033[0m")

	@property
	def InitUlimit(self):
		try:
			f=open('/etc/security/limits.conf','r')
		except Exception as e:
			print("\033[31;1mNot found limits.conf,open error!\033[0m")
			print(e)
			sys.exit()

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
			r1=subprocess.Popen("mv /etc/security/limits.conf /etc/security/limits.conf_%s"%self.CurrTime,shell=True,stderr=subprocess.PIPE)
			if not r1.stderr.read():
				f=open('/etc/security/limits.conf','w')
				f.writelines(data)
			else:
				print("\033[31;1mlimits.conf backup error!\033[0m")

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
			p=subprocess.Popen('source /etc/profile',shell=True,stderr=subprocess.PIPE)
			if p.stderr.read():
				print("\033[31;1msource /etc/proflie error!\033[0m")
			else:
				print("\033[32;1mhistory success!\033[0m")
		else:
			print("\033[32;1m/etc/profile.d/history.sh already exists!\033[0m")

	def __str__(self):
		return "__str__: Object for Init Class!"

if __name__ =='__main__':
	eeo=Init()
	eeo.InitYum
	eeo.InitIptables
	eeo.InitSysctl
	eeo.InitSelinux
	eeo.InitUlimit
	eeo.InitHistory
