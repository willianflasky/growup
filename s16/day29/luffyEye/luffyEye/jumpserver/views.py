from django.shortcuts import render,redirect,HttpResponse
import json
from jumpserver import models
import random,string

from django.contrib.auth import authenticate,login,logout

# Create your views here.

def dashboard(request):
    return render(request,'index.html')



def acc_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect(request.GET.get('next') or '/')
        else:
            error = 'Wrong username or password!'
    return render(request,'login.html',locals())


def host_list(request):

    return render(request,'host_list.html')


def get_host_list(request):
    group_id  = request.GET.get('group_id')

    if group_id:
        group_id = int(group_id)
        if group_id == -1: #取这个用户未分组的主机
            host_list = list(request.user.bind_host_users.values('host__ip_addr', 'id', 'host__hostname', 'host__port',
                                          'host_user__username'))
        else:
            group_obj = request.user.host_groups.get(id=group_id)
            host_list =  list(group_obj.bind_host_users.values('host__ip_addr', 'id', 'host__hostname', 'host__port',
                                          'host_user__username') )

        return HttpResponse(json.dumps(host_list))



def get_token(request):
    bind_host_id = request.GET.get('bind_host_id')
    token_str = ''.join(random.sample(string.ascii_lowercase+string.digits,10))
    token_obj = models.Token.objects.create(account=request.user,bind_host_user_id=bind_host_id,val=token_str)
    return HttpResponse(json.dumps({'token':token_obj.val}))




def host_mgr(request):
    pass