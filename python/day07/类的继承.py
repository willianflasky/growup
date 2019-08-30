# class A:
#     pass
#
# class B(A):
#     pass
#
# print(B.__bases__)
# print(A.__bases__)

#新式的类
# class Animal:
#     start='earth'
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#
#     def run(self):
#         print('running')
#     def talk(self):
#         print('talking')
#
# class People(Animal):
#     def piao(self):
#         print('is piaoing')
#
# class Pig(Animal):
#     pass
#
# p1=People('alex',1000,'female')
# # pig1=Pig()
#
# print(p1.start)
# p1.run()
# p1.piao()
# print(p1.name)


#继承可以重用代码
class Hero:
    def __init__(self,nickname,aggresivity,life_value):
        self.nickname=nickname #g1.nicknam=nickname
        self.aggrv=aggresivity
        self.life_value=life_value
    def attack(self,enemy):
        print('is attacking',self,enemy)
        enemy.life_value-=self.aggrv #g1.life_value-=r1.aggrv

class Garen(Hero):
    camp='Demacia'
    def fly(self):
        print('is flying')
    def attack(self):
        print('attacking')

class Riven(Hero):
    camp='Noxus'

g1=Garen('草丛伦',30,10)
g1.fly()
g1.attack('xxxxsx')

# r1=Riven('xxx',230,30)
# r1.attack()