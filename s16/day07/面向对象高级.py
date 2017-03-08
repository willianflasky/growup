#
# class Foo:
#     def __init__(self,name):
#         self.name=name
#     def __call__(self, *args, **kwargs):
#         print('====>')
# f=Foo('egon')
# f()

# class Foo:
#     def __init__(self,name):
#         self.name=name
#     def __getitem__(self,item):
#         print('getitem',self.__dict__)
#         return self.__dict__[item]
#     def __setitem__(self, key, value):
#         print('setimtem')
#         self.__dict__[key]=value
#     def __delitem__(self, key):
#         print('del obj[key]时,我执行')
#         self.__dict__.pop(key)
# f=Foo('egon')
# # print(f['name']) #f.name
# f['x']=1
# # print(f.__dict__)
# del f['x']
# print(f.__dict__)

# f1=Foo('sb')
# f1['age']=18
# f1['age1']=19
# del f1.age1
# del f1['age']
# f1['name']='alex'
# print(f1.__dict__)