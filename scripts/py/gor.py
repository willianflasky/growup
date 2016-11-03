#!/usr/bin/python
import time
import os,sys
import commands
import subprocess
#var
base_dir=os.path.dirname(os.path.abspath(__file__))
#curr_time=time.strftime("%Y%m%d_%H%M%S",time.localtime())
curr_time=time.strftime("%Y%m%d",time.localtime())
pid=os.getpid()
pid_file="run.pid"

#def start and stop
def start():
    ret_cmd=os.system("/usr/local/bin/gor --input-raw :80 --output-file %s/%s.gor & > /dev/null 2>&1"%(base_dir,curr_time))
    if ret_cmd == 0:
        print "\033[31;1m%s is running...\033[0m"%(sys.argv[0])
    else:
        print "\033[32;1mrun error.\033;0m"

def stop():
    ret=os.system('pkill gor')
    print ret
    if ret == 0:
        print "\033[31;1m kill done!\033[0m"
    else:
        print "\033[31;1m not found!\033[0m"

def sync():
    cmd=('gzip %s/%s.gor'%(base_dir,curr_time))
    ret=commands.getstatusoutput(cmd)
    if ret[0] == 0:
        ret_scp=commands.getstatusoutput('scp %s.gor.gz x.x.x.x:/root/vipkid/datafile'%curr_time)
        if ret_scp[0] == 0:
            commands.getstatusoutput('ssh x.x.x.x gunzip /root/vipkid/datafile/%s.gor.gz'%curr_time)
        else:
            print 'scp error!\n'
            print ret[0],ret[1]
    else:
        print 'gzip error!'
        print ret

if __name__=='__main__':
    try:
        if sys.argv[1] == "start":
            start()
        elif sys.argv[1] == 'stop':
            stop()
        elif sys.argv[1] == 'sync':
            sync()
        else:
            print "\033[31;1m%s start|stop\033[0m"%sys.argv[0]
    except IndexError:
         print "\033[31;1m%s start|stop\033[0m"%sys.argv[0]
