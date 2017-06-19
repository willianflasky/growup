#!/usr/bin/env python
#coding:utf8
#Author: willianflasky


import threadpool

import memcache
"""
mc=memcache.Client(['192.168.1.1:11211'],debugy=True)
mc.set('foo','bar')
#mc.set_multi({'k1','v1','k2','v2'})
#mc.add('k','v') #重复添加,失败
#mc.replace('k','vv') #替换,不存在异常
#mc.delete
#mc.delete_multi
#mc.get
#mc.get_multi(['k1','k2'])

#k1='v1'
#mc.append('k1','after')
#k1='v1after'
#mc.preapend('k1','before')
#k1='beforev1after'

#mc.incr('k1') #自增,原来123,现124
#mc.incr('k1',10)  #自增,原来123,现133
#mc.decr('k1')
#mc.decr('k1',10)

#mc.gets #增加锁
#mc.cas  #增加锁

ret=mc.get('foo')
print(ret)
"""

#天生集群
#基本操作
#gets,cas


import redis

r = redis.Redis(host='10.211.55.4', port=6379)
r.set('k1','v1')
print(r.get('k1'))


"""
set(name, value, ex=None, px=None, nx=False, xx=False)
setnx(name,value) #只有name不存在时增加
setex(name,value,time)
psetex(name,time_ms,value)
mset(*args,**kwargs)
    #mset('k1'='v1','k2'='v2')
    #mget({'k1': 'v1', 'k2': 'v2'})
getset(name,value) #设置新值并获取原来的值.
getrange(key,start,end)
setrange(name,offset,value)
setbit(name,offset,value)
getbit(name,offset,value)
bitcount(name,start,end)#二进制中的1有多少个
bitop(operation,dest,*keys)
    #bitop('AND','new_name','n1','n2','n3') #将n1,2,3的值运算后保存到new_name
strlen(name)
incr(name,amount=1)
incrbyfloat(name,amount=1.0)
decr(name,amount=1)
append(key,value)
hset(name,key,value)
hmset(name,mapping)
hget(name,key)
hmget(name,keys,*args)
hgetall(name)
hlen(name)
hkeys(name)
hexists(name,key)
hdel(name,keys*)
hincrby(name,key,amount=1)
hincrbyfloat(name,key,amount=1)
hscan(name,cursor=0,match=,count=)
hscan_iter(name,match,count)

#list
lpush(name,values)
rpush
lpushx(name,values)
rpushx
llen(name)
linsert(name,after,'tom','cat')
r.lset(name,index,value)
r.lrem(name,index,value)
lpop(name)
rpop(name)
lindex(name,index)
lrange(name,start,end)


delete(*names)
exists(name)
keys(h?llo)
expire(name,time)
rename(src,dst)
move(name,db)
randomkey()
type(name)

connection pool
pool = redis.ConnectionPool(host='10.211.55.4', port=6379)
r.redis.Reds(connection_pool=pool)

pipe=r.pipeline(transaction=True)
r.set('k1','v1')
r.set('k2','v2')
pipe.execute()

"""


#homework
#1.线程池
    #自己实现
    #第三方模块  - 注释
    #老师写的模块 - 注释
#2.博客
    #多线程
    #redis
#3.预习
    #rabbitMQ
    #mysql
    #sqlAlchemy



