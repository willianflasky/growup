
class AllFile: #接口类
    def read(self): #接口函数
        pass
    def write(self):
        pass

class Text(AllFile):
    def read(self):
        print('text read')
    def write(self):
        print('text write')


class Sata(AllFile):
    def read(self):
        print('sata read')
    def write(self):
        print('sata write')

t=Text()
s=Sata()

t.read()
t.write()
s.read()
s.write()