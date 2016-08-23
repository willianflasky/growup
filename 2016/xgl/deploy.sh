#! /bin/bash

[ $# != 1 ] && exit 1

user='ec2-user'

basedir=$(dirname $0)
basedir=$(cd "$basedir/.."; pwd)

pidfile=${basedir}/tomcat.pid
war=$1
echo "deploy ${war}"

sh ${basedir}/bin/run.sh stop
# 如果正常停止失败，则强制停止？？？
[ -s ${pidfile} ] || kill -9 `cat ${pidfile}`
rm -rf ${basedir}/webapps/ROOT/*
cp ${basedir}/bin/${war} ${basedir}/webapps/ROOT/
cd ${basedir}/webapps/ROOT
jar -xvf ${war}
rm -f ${war}
chown -R ${user}:${user} ${basedir}/webapps/ROOT
sh ${basedir}/bin/run.sh start
