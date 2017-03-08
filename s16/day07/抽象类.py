import abc
class AllFile(metaclass=abc.ABCMeta): #抽象类
    def test(self):
        print('testing')
    @abc.abstractmethod
    def read(self):
        pass
    @abc.abstractmethod
    def write(self):
        pass

class Text(AllFile):
    def read(self):
        print('text read')
    def write(self):
        pass

t=Text()
t.test()
# a=AllFile()
# a.test()


class Text:
    def read(self):
        print('asdf')

    def xie(self):
        print('asdf')
t=Text()
t.read()
t.xie()



class Sata:
    def du(self):
        pass

    def xxxxxx(self):
        pass


s=Sata()
s.du()
s.xxxxxx()




class P:
    def talk(self):
        pass