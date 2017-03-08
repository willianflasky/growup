class Teacher:
    def __init__(self,name,bitrh,course):
        self.name=name
        self.birth=bitrh
        self.course=course

class Course:
    def __init__(self,name,price,period):
        self.name=name
        self.price=price
        self.period=period

class Date:
    def __init__(self,year,mon,day):
        self.year=year
        self.mon=mon
        self.day=day

t=Teacher('egon',Date(1999,1,25),Course('python',11000,'4mons'))
print(t.birth.year)