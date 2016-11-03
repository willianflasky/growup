#!/bin/bash
set -x

base_dir=""
code_path=${base_dir}/dir
remote_base=/dir
remote_dir=${remote_base}/dir
hosts="1.1.1.1 1.1.1.2"

[ -d ${code_path} ] || exit 1
git checkout .
git pull

sed -i "s#a.js#aws/b.js#g" ${code_path}/index.html

deploy(){
	    local ip=$1
		ssh $ip cp -a ${remote_dir} ${remote_dir}.${curr_time}
		#ssh $ip find ${remote_base} -name "dir.*_*" -mtime +7 |xargs rm -rf
		echo "$ip backup done!"
		rsync -avpz --delete ${code_path}/WebContent/* $ip:${remote_dir}
		echo "$ip rsync done!"
	}
						
for host in $hosts
do
	deploy $host
	echo "$ip deploy done!"
done
