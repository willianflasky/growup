class Garen:
    camp='Demacia'
    def __init__(self,nickname,aggresivity,life_value):
        self.nickname=nickname #g1.nicknam=nickname
        self.aggrv=aggresivity
        self.life_value=life_value

    def attack(self,enemy):
        print('is attacking',self,enemy)

#类的第一个功能：实例化
g1=Garen('草丛伦',82,100) #Garen.__init__(g1,'草丛伦',82,100)
g2=Garen('草丛伦1',82,100) #Garen.__init__(g1,'草丛伦',82,100)
#类的第二个功能：属性引用，包含数据属性和函数属性
# print(Garen.camp)
# print(Garen.__init__)
# print(Garen.attack)
#
# #对于一个实例来说，只有一种功能：属性引用，实例本身只拥有数据属性
# print(g1.nickname)
# print(g1.aggrv)
# print(g1.life_value)

#
print(g1.camp,id(g1.camp))
print(g2.camp,id(g2.camp))
print(Garen.camp,id(Garen.camp))
# print(g1.attack,id(g1.attack))
# print(Garen.attack,id(Garen.attack))
#
# Garen.attack(1,2)
g1.attack('a')
Garen.attack(g2,'a') #g2.attack('a')

