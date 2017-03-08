class A:
    def test(self):
        print('from A')

class B(A):
    # def test(self):
    #     print('from B')
    pass
class C(A):
    # def test(self):
    #     print('from C')
    pass
class D(B):
    # def test(self):
    #     print('from D')
    pass
class E(C):
    # def test(self):
    #     print('from E')
    pass
class F(D,E):
    # def test(self):
    #     print('from F')
    pass
f1=F()
f1.test()
print(F.mro()) #只有新式才有这个属性可以查看线性列表，经典类没有这个属性

#新式类继承顺序:F->D->B->E->C->A
#经典类继承顺序:F->D->B->A->E->C
#python3中统一都是新式类
#pyhon2中才分新式类与经典类

# 继承顺序