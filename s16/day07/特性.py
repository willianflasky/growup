#特性是用来提供接口的一种方式


# import math
# class Circle:
#     def __init__(self,radius): #圆的半径radius
#         self.__radius=radius
#     @property # area = property(area)
#     def area(self):
#         return math.pi * self.__radius**2 #计算面积
#     @property #perimeter=property(perimeter)
#     def perimeter(self):
#         return 2*math.pi*self.__radius #计算周长
#
# c=Circle(10)
# # print(c.area())
# # print(c.perimeter())
#
# print(c.area)
# print(c.perimeter)


class A:
    def __init__(self,name):
        self.__name=name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError('%s must be str' %value)
        self.__name=value

    @name.deleter
    def name(self):
        print('=====>')
        raise AttributeError('can not delete')
a=A('egon')
# print(a.name)
# a.name=2
# print(a.name)
# del  a.name

# a.name=123123213123123123
# print(a.name)

del a.name









