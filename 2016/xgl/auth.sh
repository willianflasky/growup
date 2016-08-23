#! /bin/bash

set -x
case $1 in
online)
	hosts="1.1.1.1 1.1.1.1"
    ;;
pre)
    hosts="2.2.2.2"
    ;;
*)
    echo $"Usage: $0 {online|pre}"
    exit 1
    ;;
esac

local_src_dir=/vip/deploy/code/microservice
cd $local_src_dir
[ -d ${local_src_dir} ] || exit 1
local_conf_dir=/vip/deploy/config/microservice
[ -d ${local_conf_dir} ] || exit 1

remote_dir=/opt/vipkid/auth

cd $local_src_dir
git checkout .
git pull

cp -f ${local_conf_dir}/jdbc.properties ${local_src_dir}/auth-server/src/main/resources/
cp -f ${local_conf_dir}/redis.properties ${local_src_dir}/auth-server/src/main/resources/
cp -f ${local_conf_dir}/rpc.properties ${local_src_dir}/auth-server/src/main/resources/

JDBC_HOST="1.1.1.1:3306"
#JDBC_HOST="10.0.0.1:3306"
JDBC_USER="vipabc"
JDBC_PASSWD="111"
JDBC_DB="vipkid"

REDIS_HOST=""
REDIS_PORT='6379'
REDIS_DB='1'

RPC_PORT=50052

sed -i "s/{{jdbc.url}}/${JDBC_HOST}/g" ${local_src_dir}/auth-server/src/main/resources/jdbc.properties
sed -i "s/{{jdbc.database}}/${JDBC_DB}/g" ${local_src_dir}/auth-server/src/main/resources/jdbc.properties
sed -i "s/{{jdbc.username}}/${JDBC_USER}/g" ${local_src_dir}/auth-server/src/main/resources/jdbc.properties
sed -i "s/{{jdbc.password}}/${JDBC_PASSWD}/g" ${local_src_dir}/auth-server/src/main/resources/jdbc.properties

sed -i "s/{{redis.host}}/${REDIS_HOST}/g" ${local_src_dir}/auth-server/src/main/resources/redis.properties
sed -i "s/{{redis.port}}/${REDIS_PORT}/g" ${local_src_dir}/auth-server/src/main/resources/redis.properties
sed -i "s/{{redis.db}}/${REDIS_DB}/g" ${local_src_dir}/auth-server/src/main/resources/redis.properties

sed -i "s/{{rpc.port}}/${RPC_PORT}/g" ${local_src_dir}/auth-server/src/main/resources/rpc.properties

war="auth-server.war"
/usr/local/maven/bin/mvn clean package -Dmaven.test.skip=true
[ $? == 0 ] || exit 1
git checkout .

for host in ${hosts}
do
	scp ${local_src_dir}/auth-server/target/${war} ec2-user@${host}:${remote_dir}/bin/
	[ $? == 0 ] || exit 1
	ssh ec2-user@${host} "sh ${remote_dir}/bin/deploy.sh $war"
	sleep 60
done
