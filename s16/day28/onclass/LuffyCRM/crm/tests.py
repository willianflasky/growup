from django.test import TestCase

# Create your tests here.


class Base(object):
    list_per_page = 5
    actions = ['test']

class CustomerAdmin(Base):
    actions = ['enroll']


a1 = Base()
a1.actions += ['a1','a11']
a1.list_per_page =  10
a2 = Base()

print(a2.actions,a2.list_per_page)

