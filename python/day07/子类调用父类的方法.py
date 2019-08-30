class People:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def test(self):
        print('from A.test')

class Teacher(People):
    def __init__(self,name,age,gender,level):
        # People.__init__(self,name,age,gender)
        super().__init__(name,age,gender)
        self.level=level



t=Teacher('egon',18,'female','高级讲师')
print(t.level)