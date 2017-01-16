#!/bin/bash
#/etc/nginx/* --> /etc/nginx/*
hosts="10.2.2.11"
nginx -t >/dev/null 2>&1
if [ $? == 0 ];then
        echo -e "\033[32;1mlocal check ok!\033[0m"
else
        echo -e "\033[31;1mlocal check failure!\033[0m"
        exit 1
fi
sync_file(){
        echo -e "\033[32;1mstart sync_file to $1\033[0m"
        local ip=$1
        rsync -avpz --delete /etc/nginx/ $1:/etc/nginx/ > /dev/null 2>&1
        ssh $1 nginx -t >/dev/null 2>&1
        if [ $? == 0 ];then
                echo -e "\033[32;1msync ok!\033[0m"
                ssh $1 nginx -s reload
        else
                echo -e "\033[31;1mnginx -t check failure,please check $1 reson.\033[0m"
                exit 1
        fi
}
for host in $hosts;do
        sync_file $host
done
