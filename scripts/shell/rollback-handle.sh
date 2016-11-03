#!/bin/bash
#sh rollback-handler.sh appserver
set -x
case $1 in
appserver)
    hosts="10.0.0.1 10.0.0.2"
	;;
*)
    echo -e "\033[33;1m./$0 appserver\033[0m"
    exit 1
    ;;
esac

base=$(pwd)
client=rollback-client.sh

for host in $hosts;do
    scp ${base}/$client root@${host}:/opt/shell
    scp ${base}/appserver.sh root@${host}:/opt/shell

    ssh $host sh /opt/shell/$client appserver &
    #ssh $host ps aux|grep appserver
done
