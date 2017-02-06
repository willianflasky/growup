
1.使用了class方式,但是前期规划的并不好,模块化和代码抽象不理想.
2.表名没有管理,可以随便写.
3.查询和显示数量:
    <1>mysql>select name,age from t1 where age > 22
            ['黄鑫', '23']
            ['nio', '27']
            ['nio', '28']
            count: 3
    <2>mysql>select * from t1 where dept = dev
            01,nio,22,18611044558,dev,新华电商,2016-11-23
            14,nio,27,13552791537,dev,eeo,2017-01-01
            15,nio,28,185009888004,dev,yunji,2018-01-01
            count: 3
    <3>mysql>select * from t1 where phone like 444
            12,李向阳,18,13622004447,运维,信工所,2015-11-23
            count: 1
4.加入新学员同时自增:
    mysql>insert tom 30 1383838438 dev tencent 2015-01-01
    #不过验证需要重新运行程序.
5.删除:
    mysql>delete 16
    #删除ID号为16的,同样验证需要重新运行程序.
6.更新:
    mysql>update t1 set name=NIO where dept = dev
    #有多少匹配则都会更新,同样验证需要重新运行程序看效果.

经验总结:
    1.公用变量放在__init__初始化.
    2.模块化程度.
    3.写前最好有设计规划,当然如果失败,建议重写一遍.
