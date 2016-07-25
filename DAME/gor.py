#!/usr/bin/python
import time
import os,sys
import commands
import subprocess
#var
base_dir=os.path.dirname(os.path.abspath(__file__))
curr_time=time.strftime("%Y%m%d_%H%M%S",time.localtime())
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

if __name__=='__main__':
    try:
        if sys.argv[1] == "start":
            start()
        elif sys.argv[1] == 'stop':
            stop()
        else:
            print "\033[31;1m%s start|stop\033[0m"%sys.argv[0]
    except IndexError:
         print "\033[31;1m%s start|stop\033[0m"%sys.argv[0]
