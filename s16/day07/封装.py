# class Foo:
#     # print('======================>')
#     x=1
#     def __init__(self,name,money):
#         self.name=name
#         self.__money=money #self._Foo__money
#
#     def get_money(self):
#         print(self.__money)
#         self.__spam()
#
#     def __spam(self): #_Foo__spam
#         print('from spam')
#
# print(Foo.__dict__)
# Foo.__xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=1
# print(Foo.__dict__)
# f = Foo('egon', 1000)

# print(f.__dict__)
# f.__x=1
# print(f.__dict__)
# print(f.__x)




# f=Foo('alex',2000000)
#
# # print(f.__money)
# f.get_money()
# print(Foo.__dict__)
# print(f.__dict__)
# print(Foo.__dict__)
# f.__money
# print(f._Foo__money)

# print(Foo.__dict__)
# f.get_money()

# class Foo:
#     __x=1
#     def __init__(self,name,age,gender,money):
#         self.__name=name
#         self.__age=age
#         self.__gender=gender
#         self.__money=money
#     def tell_info(self):
#         print(self.__name)
#         print(self.__age)
#         print(self.__gender)
#         print(self.__money)
#
# f1=Foo('egon',19,'man',1888)
# f1.tell_info()

class A:
    def __spam(self): #_A__spam
        print('A.spam')

    def test(self):
        print('A.test')
        self.__spam() #self._A__spam
class B(A):
    def __spam(self): #_B__spam
        print('B.spam')

b1=B()
b1.test()