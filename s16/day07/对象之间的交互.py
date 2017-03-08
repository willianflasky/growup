class Garen:
    camp='Demacia'
    def __init__(self,nickname,aggresivity,life_value):
        self.nickname=nickname #g1.nicknam=nickname
        self.aggrv=aggresivity
        self.life_value=life_value

    def attack(self,enemy):
        print('is attacking',self,enemy)

class Riven:
    camp='Noxus'
    def __init__(self,nickname,aggresivity,life_value):
        self.nickname=nickname #g1.nicknam=nickname
        self.aggrv=aggresivity
        self.life_value=life_value

    def attack(self,enemy):
        print('is attacking',self,enemy)
        enemy.life_value-=self.aggrv #g1.life_value-=r1.aggrv

g1=Garen('草丛伦',82,100)
r1=Riven('锐雯雯',50,200)

print(g1.life_value)
#
r1.attack(g1)
print(g1.life_value)

