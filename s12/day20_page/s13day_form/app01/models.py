from django.db import models

# Create your models here.


class UserType(models.Model):
    caption=models.CharField(max_length=16)

class UserInfo(models.Model):
    username=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)
    user_type=models.ForeignKey('UserType')

"""
#多对多
    #第一种:
    class B2G(models.Model):
        b_id=models.ForeignKey('Boy')
        g_id=models.ForeignKey('Girl')

    class Boy(models.Model):
        username=models.CharField(max_length=16)

    class Girl(models.Model):
        name = models.CharField(max_length=16)

    #第二种:
    class Boy(models.Model):
        username=models.CharField(max_length=16)

    class Girl(models.Model):
        name = models.CharField(max_length=16)
        b =  models.ManyToManyField('Boy')

操作
    添加:
        正向操作:
        g1=models.Girl.objects.get(id=1)
        g1.b.add(models.Boy.objects.get(id=1)
        g1.b.add(1)

        bs=models.Boy.objects.all()
        g1.b.add(*bs)
        g1.b.add(*[1,2,3])

        ----
        反向操作:
        b1=models.Boy.objects.all()
        b1.girl_set.add(*b1)
        b1.girl_set.add(1)

    删除:
        g1=models.Girl.objects.get(id=1)
        g1.b.clear()

        g1.b.remove(2)
        g1.b.remove(*[1,2])

    查询:
        g1=models.Girl.objects.get(id=1)
        g1.b.all()
        g1.b.filter().count()

        b1=models.Boy.objects.get(id=1)
        b1.girl_set.all()

        models.Girl.objects.all().values('id','name','b__username')
        models.Boy.objects.all().values('id','username','girl__name')

    更新:
        原生SQL
    ORM:
        MySQLdb
        pymysql
    原生SQL:
        from django.db import connection
        cursor=connection.cursor()
        cursor.excute('''select * from tb where name=%s''',['Lenono'])
        row=cursor.fetchone()

"""
class Boy(models.Model):
    username=models.CharField(max_length=16)

class Girl(models.Model):
    name = models.CharField(max_length=16)
    b =  models.ManyToManyField('Boy')


class UserList(models.Model):
    username=models.CharField(max_length=32)
    age=models.IntegerField()

