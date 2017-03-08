#多态:同一种事物的不同形态，如序列类型包含字符串，列表，元组


# s='xxx'
# l=[1,2,3]
# t=(4,5,6)
#
# #多态性
# def func(obj):
#     print(obj.__len__())
#
# func(s)
# func(l)
# func(t)


class Animal:
    def talk(self):
        pass

class People(Animal):
    def talk(self):
        print('say hello')
class Pig(Animal):
    def talk(self):
        print('say aoao')

class Dog(Animal):
    def talk(self):
        print('say wangwang')

class Cat(Animal):
    def talk(self):
        print('cat talking')

p1=People()
pig1=Pig()
D1=Dog()
c=Cat()

















def func(obj):
    obj.talk()


#
# func(p1)
# func(pig1)
# func(D1)
# func(c)




