
1.cnblogs
    http://www.cnblogs.com/weibiao/p/6664553.html
2.流程图
    python16_day11_MQ.png
3.主程序
    ├── agent
    │   └── agent.py            # agent: python3 agent.py -h
    └── ansible
        ├── bin
        │   └── ansible.py      # 入口文件
        ├── conf
        │   └── settings.py     # 配置文件
        └── lib
            ├── __init__.py
            ├── base.py         # 基类
            ├── recv.py         # 子类
            └── send.py         # 子类
4.使用说明
    目前只完成基本功能,控制端通过MQ远程执行命令并返回结果.使用MQ关键字发布订阅功能,
    将执命发问出去并携带UUID,agent端收到信息后,本地执行结果并使用UUID发送出去.控制端再拿着UUID去订阅结果.
    a.安装rabbitMQ并启动
    b.启动agent: ./agent.py -i localhost -n ansible
    c.启动控制端: ./ansible.py
        >>>ls
        host1:
            agent.py

        host2:
            agent.py

        >>>pwd
        host1:
            /Users/willian/PycharmProjects/growup/s16/homework/day11_MQ/agent

        host2:
            /Users/willian/PycharmProjects/growup/s16/homework/day11_MQ/agent
