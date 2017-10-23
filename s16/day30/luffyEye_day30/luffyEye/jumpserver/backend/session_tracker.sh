#!/bin/bash


echo $1

for i in $(seq 1 30);do
    echo $i
    process_id=`ps -ef |grep ssh|grep $1|grep -v sshpass|awk '{ print $2 }'` 
    #if [ -z $process_id ];then
    #	continue
    #fi 
    if [ ! -z $process_id ];then
    	echo "get process id $process_id"
        #basepath=$(dirname $(dirname $(cd `dirname $0`; pwd) ) )
	#echo $basepath 
        sudo strace -fp $process_id -tt -o /home/ago/luffyEye/log/audit/ssh_audit_$2.log
    	break 
    fi;
    sleep 0.5
done;


