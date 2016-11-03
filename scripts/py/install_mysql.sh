#!/bin/bash
user=mysql
mysqltar="mysql-5.6.24-linux-glibc2.5-x86_64"
data="/data/db"
filepath=$(cd "$(dirname "$0")"; pwd)


compress(){
	tar -zxvf mysql-5.6.24-linux-glibc2.5-x86_64.tar.gz >/dev/null
        if [ $? == 0 ];then
                echo -e "\033[32;1mtar success!\033[0m"
        fi
}

read -p "select install file[mysql-5.6.24-linux-glibc2.5-x86_64.tar.gz]>Y/n" selected

if [ $selected = "y" ] || [ $selected = "Y" ];then
	compress
else
	echo "\003[31;1mnot support other!\033[0m"
	exit 1;
fi


id $user >/dev/null
if [ $? -ne 0 ]; then
	useradd mysql -r -s /sbin/nologin
fi

if [ -d "mysql" ];then
	echo -e "\033[31;1m mysql directory exist!\033[0m"
	exit 1;

else
	if [ -d ${mysqltar} ];then
		mv ${mysqltar} mysql
	else
		compress
	fi
fi

#chown
cd mysql
chown root:mysql . -R

if [ -d ${data} ];then
	echo -e "\033[31;1m${data} is exist!\033[0m"
	exit 1;
else
	mkdir -p ${data}
	chown mysql.mysql ${data}
	if [ $? -ne 0 ];then
		echo "\033[32;1m$data  create ok!\033[0m"
	fi
fi


#init
cat >>${filepath}/mysql/my.cnf<<EOF
#mysql 5.6.24 config file.
[client]
socket				=/tmp/mysql.sock
port				=3306
default-character-set		=utf8

[mysqld]
character-set-server		=utf8
collation-server		=utf8_general_ci
socket				=/tmp/mysql.sock
port				=3306
user				=mysql
basedir				=/usr/local/mysql
datadir				=/data/db
default-storage-engine		=innodb
symbolic-links			=0
back_log 			=30
max_connections 		=1000
max_connect_errors 		=99999
open_files_limit 		=65535
table_open_cache 		=4096
max_allowed_packet 		=64M
max_heap_table_size 		=64M
read_buffer_size 		=4M
read_rnd_buffer_size 		=16M
sort_buffer_size 		=16M
join_buffer_size 		=16M
thread_cache_size 		=16
query_cache_size 		=128M
query_cache_limit 		=4M
key_buffer_size 		=64M
transaction_isolation 		=REPEATABLE-READ
tmp_table_size 			=64M
read_rnd_buffer_size 		=64M
innodb_log_file_size 		=512M
innodb_log_files_in_group 	=3
innodb_lock_wait_timeout 	=120
innodb_file_per_table 		=on
skip-name-resolve
expire_logs_days 		=30
innodb_buffer_pool_size		=1G
log_error			=/usr/local/mysql/data/mysql.log
explicit_defaults_for_timestamp	=true
EOF

cd ${filepath}/mysql
scripts/mysql_install_db --user=mysql --defaults-file=${filepath}/mysql/my.cnf

if [ $? -ne 0 ];then
	echo -e "\033[31;1m install failure!\033[0m"
else
	echo -e "\033[32;1m install success!\033[0m"
fi

