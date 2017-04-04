

1.cnblogs
    http://www.cnblogs.com/weibiao/p/6636874.html
2.ansibleLike说明
    day10_ansibleLike/
    ├── bin
    │   ├── __init__.py
    │   ├── ansible.py      # 主文件
    │   └── manager.py      # 管理文件
    ├── conf
    │   ├── __init__.py
    │   └── settings.py     # 配置文件
    ├── core
    │   ├── __init__.py
    │   ├── command.py      # 远程执行命和上传文件处理
    │   ├── core.py         # 主程序文件
    │   ├── display.py      # 验证通过后,获取用户可管理的主机
    │   └── verify.py       # 主要处理用户名验证
    ├── create_table
    ├── lib
    │   ├── __init__.py
    │   ├── manage_helper.py    # 管理业务处理类
    │   ├── mysql_helper.py     # pymysql封装类
    │   └── ssh_helper.py       # paramiko ssh封装类
    └── requirements
    |__ data.sql                # 数据

3.ansible操作演示
    a.登录:请输入用户名:alex
           请输入密码:

      验证成功!

      管理主机地址:
            10.0.0.225
            10.0.0.226
    b.打命令:
        >>>ls
        anaconda-ks.cfg
        install.log
        install.log.syslog

        anaconda-ks.cfg
        install.log
        install.log.syslog
    c.上传
        >>>upload
        local_file>/Users/willian/m.py
        target_file>/tmp/m.py

     >>>ls /tmp/m.py -l
        -rw-r--r-- 1 root root 346 Mar 29 10:13 /tmp/m.py

        -rw-r--r-- 1 root root 346 Mar 29 10:13 /tmp/m.py

    d.查询用户
        1 查询用户
        2 查询主机
        3 查询用户的主机
        4 增加用户
        5 增加主机
        6 增加用户的主机
        ...还有未完成

        >>>1
        Id:1	Username:	willian
        Id:2	Username:	alex
        total:2

        >>>2
        id:1 ip:192.168.1.1
        id:2 ip:192.168.1.2
        id:3 ip:10.0.0.225
        id:4 ip:10.0.0.226
        total:4

        >>>3
        willian
            IP:192.168.1.1
            IP:192.168.1.2
            IP:10.0.0.225
            IP:10.0.0.226
        alex
            IP:10.0.0.225
            IP:10.0.0.226
        total:6
