#!/usr/bin/env python

class Role(object):
    members=0

    def __init__(self,name,role,weapon,life_value):
        self.name=name
        self.role=role
        self.weapon=weapon
        self.life_value=life_value
        Role.members +=1

    def buy_weapon(self,weapon):
        print('%s is buying [%s]'%(self.name,weapon))
        self.weapon=weapon





p1=Role('ShanJiang','Police','B10',90)
t1=Role('ChunYun','Terrorist','B11',100)
print(Role.members)
"""
p1.buy_weapon('AK47')   #Role.buy_weapon(p1,'AK47')
t1.buy_weapon('B51')

p1.ac='china brand'
t1.ac='us brand'
print('P1:',p1.weapon,p1.ac)
print('T1:',t1.weapon,t1.ac)"""


