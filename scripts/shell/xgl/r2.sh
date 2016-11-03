#!/bin/bash
set -x

parent_rest=""
mobile=""
app_proxy="a"
auth="

case $1 in
online_331)
	hosts='10.0.x.x'
    ;;
online_431)
	hosts="10.0.x.x"
	;;
pre)
	hosts=""
	parent_rest=""
	mobile=""
	app_proxy=""
	auth=""
	;;
*)
    echo $"Usage: $0 {online_331|onile_431|pre}"
	exit 1
    ;;
esac

user="ec2-user"
local_src_dir=/vipkid/deploy/code/r2
cd $local_src_dir
git pull
[ -d ${local_src_dir} ] || exit 1
local_conf_dir=/vipkid/deploy/config/r2

[ -d ${local_conf_dir} ] || exit 1
remote_dir=/opt/vipkid/r2
local_venv_dir=/opt/vipkid/r2
[ -d ${local_venv_dir} ] || exit 1

configDir=/opt/vipkid/r2/bin
configFile=${configDir}/env.sh

init_venv(){
    cd ${local_venv_dir}
    cp -rf ${local_src_dir}/requirements.txt .
    [ -d ${local_venv_dir}/venv ] || virtualenv venv
    source $local_venv_dir/venv/bin/activate
	[ $? == 0 ] || exit 1
	pip install --trusted-host=pypi.vipkid.com.cn --index-url=http://pypi.vipkid.com.cn/vipkid/dev -U pip
	[ $? == 0 ] || exit 1
    pip install --trusted-host=pypi.vipkid.com.cn -r requirements.txt
}

cp -rf ${local_conf_dir}/* ${configDir}/
sed -i "s/{{mobile}}/${mobile}/g" ${configFile}
sed -i "s/{{app_proxy}}/${app_proxy}/g" ${configFile}
sed -i "s/{{auth}}/${auth}/g" ${configFile}
sed -i "s/{{parent_rest}}/${parent_rest}/g" ${configFile}
sed -i "s/{{parent_rest}}/${parent_rest}/g" ${configFile}

deploy(){
    echo 'deploy start'
    local ip=$1
    local remote_url=${user}@${ip}:${remote_dir}
    echo "deploying $ip"
    rsync -avpz --delete ${configDir}/* $remote_url/bin/
    rsync -avpz --delete ${local_src_dir}/* $remote_url/src/ --exclude={"apitests","hooks","benchmark","data","scripts","tests"}
    rsync -avpz --delete ${local_venv_dir}/venv $remote_url/
    echo 'deploy end'
	}

echo "init r2d2 venv ..."
init_venv

for host in $hosts
do
    echo $host
    deploy $host
    ssh ${user}@$host "sh /opt/vipkid/r2d2/bin/r2d2.sh restart"
	ssh ${user}@${hosts} "ps auxf |grep python"
done
