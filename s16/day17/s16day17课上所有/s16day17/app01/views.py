from django.shortcuts import render,HttpResponse,redirect
from django.views import View

def index(request):
    print('.....')
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    return HttpResponse('....')

class User(View):
    def dispatch(self, request, *args, **kwargs):
        print('before')
        obj = super(User,self).dispatch(request, *args, **kwargs)
        print('after')
        return obj

    def get(self,request):
        print("get...")
        return HttpResponse('...')

    def post(self,request):
        print("post...")
        return HttpResponse('...')

    def put(self,request):
        print("post...")
        return HttpResponse('...')

    def delete(self,request):
        print("post...")
        return HttpResponse('...')


from app01 import models
def test(request):
    # models.DePart.objects.create(title='IT')
    # models.DePart.objects.create(title='咨询')
    # models.DePart.objects.create(title='公关')

    # models.UserInfo.objects.create(username='alex',password='123',dp_id=1)
    # models.UserInfo.objects.create(username='eric',password='123',dp_id=1)
    # models.UserInfo.objects.create(username='贺磊',password='123',dp_id=1)
    # models.UserInfo.objects.create(username='刘浩',password='123',dp_id=2)


    # 正向跨表
    # 1. 对象
    # q = models.UserInfo.objects.all()
    # queryset =  [obj(username,password,obj(id,title),dp_id),]
    # for row in q:
    #     print(row.username,row.password,row.dp_id,row.dp.id,row.dp.title)

    # 2. 字典
    # q = models.UserInfo.objects.values('username', 'password', "dp_id", "dp__title")\
    # # [{...},{}]
    # for row in q:
    #     print(row['username'],row['dp__title'])

    # 3. 元组
    # q = models.UserInfo.objects.values_list('username', 'password', "dp_id", "dp__title")
    # # [(),()]
    # for row in q:
    #     print(row[0],row[3])

    # 反向跨表
    # 1. 对象
    # v = models.DePart.objects.all()
    # queryset = [obj,obj,obj]
    # for row in v:
    #     print(row.id,row.title,row.userinfo_set.all())
    # 2. 字典
    # v = models.DePart.objects.values('id','title','userinfo__username','userinfo__password')
    # for row in v:
    #     print(row)
    # 3. 元组
    # v = models.DePart.objects.values_list('id','title','userinfo__username','userinfo__password')
    # for row in v:
    #     print(row)

    # 多对多
    # 1. 自己写第三张表
    #    第三张表列数无限制
    # models.U2G.objects.create(ui_id=1,ug_id=2)
    # models.U2G.objects.create(ui_id=2,ug_id=2)
    # models.U2G.objects.create(ui_id=3,ug_id=1)
    # q = models.U2G.objects.all()
    # for row in q:
    #     print(row.ug.caption,row.ui.username)
    # 2. Django自动根据ManyToManyField字段生成第三张表（列限制）
    obj = models.UserGroup.objects.filter(id=1).first()  # 2 B组
    # obj.m.add(1)  # 1 Alex
    # obj.m.add(1, 2, 3, 4)
    # obj.m.add(*[1,2])

    # obj.m.remove(1)
    # obj.m.remove(2,3)
    # obj.m.remove(*[4,])
    # obj.m.clear()

    # obj.m.set([3,1,2])

    # q = obj.m.all()
    # print(q)
    # 建立在上一次查询基础上，再次做二次筛选
    # q = obj.m.filter(id__gt=2)
    # print(q)
    return HttpResponse('...')


def ck(request):
    print(request.COOKIES)
    obj = render(request,'ck.html')
    # obj.set_cookie('nnn','123123')
    return obj

def login(request):
    if request.method == 'GET':
        return render(request,'login.html',{'msg':""})
    else:
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        ct = models.UserInfo.objects.filter(username=u,password=p).count()
        if ct:
            obj = redirect('/home/')
            # 生成随机字符串
            # 发给客户端
            # 保存在服务端
            # 并在服务端写：用户名和密码
            request.session['user'] = u
            request.session['pwd'] = p
            return obj
        else:
            return render(request, 'login.html',{'msg':'用户名或密码错误'})

def home(request):
    v = request.session.get('user')
    if v:
        return render(request,'home.html')
    else:
        return redirect('/login/')


def logout(request):
    request.session.clear()
    return redirect('/login/')


def aj(request):
    if request.method == 'GET':
        return render(request,'aj.html')
    elif request.method == "POST":
        user = request.POST.get('uuu')
        pwd = request.POST.get('ppp')
        obj = models.UserInfo.objects.filter(username=user,password=pwd).first()
        ret = {'status': True, 'error': None}
        import json
        if obj:
            # 登陆成功,跳转到后台管理
            request.session['user'] = user
            request.session['pwd'] = pwd
            return HttpResponse(json.dumps(ret))
        else:
            ret['status'] = False
            ret['error'] = "用户名或密码错误"
            # 登陆失败，页面显示错误信息
            return HttpResponse(json.dumps(ret))











