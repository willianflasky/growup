# class Foo:
#     @staticmethod
#     def spam(x,y,z): #类中的一个函数，千万不要懵逼，self和x啥的没有不同都是参数名
#         print(x,y,z)
#     # spam=staticmethod(spam) #把spam函数做成静态方法
#
# Foo.spam(1,2,3)
#静态方法的应用：
import time
class Date:
    def __init__(self,year,mon,day):
        self.year=year
        self.mon=mon
        self.day=day

    @staticmethod
    def now():
        t=time.localtime()
        return Date(t.tm_year,t.tm_mon,t.tm_mday)

d=Date(1922,1,23)
d1=Date.now()


#类方法
# class A:
#     x=1
#     @classmethod
#     def test(cls):
#         print(cls,cls.x)
#
# A.test()

#类方法的应用场景
# class A:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     #
#     def __str__(self):
#         return 'name:%s age:%s' %(self.name,self.age)
#
# a=A('eghon',19)
# print(a)



#类方法的应用
# import time
# class Date:
#     def __init__(self,year,mon,day):
#         self.year=year
#         self.mon=mon
#         self.day=day
#
#     @classmethod
#     def now(cls):
#         t=time.localtime()
#         return cls(t.tm_year,t.tm_mon,t.tm_mday)
#
# d1=Date.now()
# print(d1.year,d1.mon,d1.day)


#类方法与静态方法的区别
import time
class Date:
    def __init__(self,year,mon,day):
        self.year=year
        self.mon=mon
        self.day=day

    @classmethod
    def now(cls):
        t=time.localtime()
        return cls(t.tm_year,t.tm_mon,t.tm_mday)
    # @staticmethod
    # def now():
    #     t=time.localtime()
    #     return Date(t.tm_year,t.tm_mon,t.tm_mday)

class EuroDate(Date):
    def __str__(self):
        return 'year:%s mon:%s day:%s' %(self.year,self.mon,self.day)

e=EuroDate.now()
print(e)