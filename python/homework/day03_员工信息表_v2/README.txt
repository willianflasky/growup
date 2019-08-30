说明:
1.使用了class方式.
2.表名没有管理,可以随便写.
3.查询和显示数量:
    <1>mysql>select name,age from t1 where age > 21
            +---------+-----+
            |   name  | age |
            +---------+-----+
            | willian |  22 |
            |   nio   |  22 |
            +---------+-----+
            count: 2

    <2>mysql>select * from t1 where dept = dev
            +----------+---------+-----+-------------+------+----------+-------------+
            | stuff_id |   name  | age |    phone    | dept | company  | enroll_date |
            +----------+---------+-----+-------------+------+----------+-------------+
            |    01    | willian |  22 | 18611044558 | dev  | 新华电商  |  2016-11-23 |
            |    13    |   nio   |  22 | 13552791537 | dev  |   eeo    |   2016-1-1  |
            +----------+---------+-----+-------------+------+----------+-------------+
            count: 2
    <3>mysql>select * from t1 where phone like 444
            +----------+--------+-----+-------------+------+---------+-------------+
            | stuff_id |  name  | age |    phone    | dept | company | enroll_date |
            +----------+--------+-----+-------------+------+---------+-------------+
            |    12    | 李向阳 |  18 | 13622004447 | 运维 |  信工所    |  2015-11-23 |
            +----------+--------+-----+-------------+------+---------+-------------+
            count: 1

4.加入新学员同时自增:
    mysql>insert tom 30 1383838438 dev tencent 2015-01-01
    主健冲突!
    mysql>insert tom 30 18500988004 dev tencent 2015-01-01
    验证:mysql>showme

5.删除:
    mysql>delete 15
          not found!
    mysql>delete 14
    验证:mysql>showme

6.更新:
    mysql>update t1 set name=NIO where dept = dev
    验证:mysql>showme
7.cnblog:
    http://www.cnblogs.com/weibiao/p/6340178.html

经验总结:
    1.公用变量放在__init__初始化.
    2.模块化程度.
    3.写前最好有设计规划,当然如果失败,建议重写一遍.

