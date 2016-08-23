#!/bin/bash
set -x
case $1 in
appserver)
    shell_base=$(pwd)
    base="/home/vipkid/www/$1"
    target=${base}/webapps
    backBase=/backup
    backFile=ROOT.tar.gz
    user="ec2-user"
    ;;

*)
    echo -e "\033[33;1m./$0 appserver\033[0m"
    exit 1
    ;;
esac


if [ $# != 1 ];then
          echo -e "\033[33;1m\tone argvs!\033[0m"
          exit 1
fi


getpid() {
        pid=$(sudo -u ${user} /usr/local/java/bin/jps -v |grep $1 |awk '{print $1}')
}


killAPP() {
        getpid
        if [ "$pid" ];then
                kill $pid
        fi
        sleep 3
        gitpid
        if [ "$pid" ];then
                kill -9 $pid
        fi
}

clearROOT() {
    mv /$target/ROOT /tmp/ROOT-`date +%F_%H%M%S`
    cd $backBase
    tar -zxf $backFile -C $target
    [ -d "${target}/ROOT" ] || exit 1
    chown -R ec2-user.ec2-user ${target}/ROOT

}

if [ ! -d $backBase ]; then
        echo "not found $backBase"
        exit 1
fi

if [ ! -f $backBase/$backFile ]; then
        echo "not found $backBase/$backFile"
        exit 1
fi

/etc/init.d/appserver stop > /dev/null 2>&1
sleep 3s

killAPP

clearROOT

/etc/init.d/appserver start > /dev/null 2>&1
exit 0
