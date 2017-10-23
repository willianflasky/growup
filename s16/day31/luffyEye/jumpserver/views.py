from django.shortcuts import render,redirect,HttpResponse
import json,time
from jumpserver import models
import random,string
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from jumpserver import task_handler
from django.contrib.auth import authenticate,login,logout
import os,signal
import zipfile
from wsgiref.util import FileWrapper #from django.core.servers.basehttp import FileWrapper
from django.conf import settings
# Create your views here.

@login_required
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

@login_required
def host_list(request):

    return render(request,'host_list.html')

@login_required
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


@login_required
def get_token(request):
    bind_host_id = request.GET.get('bind_host_id')
    token_str = ''.join(random.sample(string.ascii_lowercase+string.digits,10))
    token_obj = models.Token.objects.create(account=request.user,bind_host_user_id=bind_host_id,val=token_str)
    return HttpResponse(json.dumps({'token':token_obj.val}))


@login_required
def multi_cmd(request):
    return render(request,'multitask_cmd.html')

@login_required
def multi_file(request):
    random_tag = ''.join(random.sample(string.ascii_lowercase + string.digits, 10))
    return render(request,'multitask_file.html',locals())


@login_required
def multitask(request):

    task_obj = task_handler.Task(request)
    if task_obj.is_valid():
        res = task_obj.run()

        return HttpResponse(json.dumps({"task_id": res.id,'timeout':res.timeout} ))
    else:
        return HttpResponse(json.dumps(task_obj.errors))


@login_required
def terminate_task(request):
    task_id = request.POST.get('task_id')
    task_obj = models.Task.objects.get(id=task_id)
    os.killpg(task_obj.pid , signal.SIGTERM)

    return HttpResponse(json.dumps({'status':0,'msg':'task got killed'}))

@csrf_exempt
def file_upload(request):
    print(request.FILES)
    random_tag = request.GET.get('random_tag')
    upload_dir = "uploads/%s/%s" %(request.user.id,random_tag)
    if not os.path.isdir(upload_dir):
        os.makedirs(upload_dir,exist_ok=True)

    file_obj = request.FILES.get('file')
    new_file = open("%s/%s"%(upload_dir,file_obj.name),'wb')
    for trunk in file_obj.chunks():
        new_file.write(trunk)
    new_file.close()
    return HttpResponse(json.dumps({'status':0}))



def date_handler(value):
    #print('sdfsfsf',value)


    return time.strftime("%Y-%m-%d %H:%M:%S", value.timetuple())

@login_required
def multitask_result(request):
    task_id = request.GET.get('task_id')
    if task_id:

        # [ {
        #     'id':122,
        #     'hostname':localhost
        #     'ipaddr':10.12,
        #     'result':'df result',
        #     'status':0
        #     'date':19:33
        # },{}  ]
        task_obj = models.Task.objects.get(id=task_id)
        task_result = list(task_obj.tasklog_set.values('id','status','bind_host__host__ip_addr',
                                                  'bind_host__host__hostname','result','date'))
        return HttpResponse(json.dumps(task_result,default=date_handler))


def send_zipfile(request,task_id,file_path):
    """
    Create a ZIP file on disk and transmit it in chunks of 8KB,
    without loading the whole file into memory. A similar approach can
    be used for large dynamic PDF files.
    """
    zip_file_name = 'task_id_%s_files' % task_id
    archive = zipfile.ZipFile(zip_file_name , 'w', zipfile.ZIP_DEFLATED)
    file_list = os.listdir(file_path)
    for filename in file_list:
        archive.write('%s/%s' %(file_path,filename),arcname=filename)
    archive.close()
    wrapper = FileWrapper(open(zip_file_name,'rb'))
    response = HttpResponse(wrapper, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=%s.zip' % zip_file_name
    response['Content-Length'] = os.path.getsize(zip_file_name)
    #temp.seek(0)
    return response


def download_task_file(request):
    task_id = request.GET.get('task_id')
    filepath = "%s/%s"%(settings.DOWNLOADS_DIR,task_id)
    return send_zipfile(request, task_id, filepath)


def host_mgr(request):
    pass