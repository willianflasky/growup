#!/bin/sh
# this script is  nginx logs split
LOGS_PATH=/var/log/nginx
DATE=`date +%Y%m%d`
PID=/var/run/nginx.pid

#root
if [ $UID -ne 0 ];then
        echo "you must is root"
        exit 1
fi

#backup
for  file  in `ls $LOGS_PATH/*.log`;do
        mv $file $file.$DATE
done

# reload config file
if [ $? -eq 0 ];then
        kill -USR1 `cat $PID`
else
        exit 1
fi

#compress
for gzfile in `ls $LOGS_PATH/* |grep "$DATE"`;do
        gzip $gzfile
done

# del old file
find $LOGS_PATH -type f -mtime +30 -name "*.gz" -exec rm -f {} \;
