class Foo:
    def __init__(self,name):
        self.name=name

    def func(self):
        print('--------------.func')


print(hasattr(Foo,'func'))
f=Foo('egon')
print(hasattr(f,'x'))
f.x=1
print(getattr(f,'x'))
print(getattr(f,'func'))
if hasattr(f,'func'):
    aa=getattr(f,'func')
    aa()
print(getattr(f,'y',None))

# f.y=1 #f y 1
setattr(f,'y',1)
print(f.__dict__)

delattr(f,'y')
print(f.__dict__)


# print(Foo.__dict__)
# print(f.__dict__)