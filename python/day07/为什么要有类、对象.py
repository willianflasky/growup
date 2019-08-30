dang='guomindang'
class Chinese:
    # dang='gongchandang'
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        self.dang='111111'
    def talk(self):
        print('=-====>')

p1=Chinese('egon',18,'female')

print(p1.dang)