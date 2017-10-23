
import time,sys,os,json
import multiprocessing
import paramiko

def run_cmd(tasklog_obj_id,task_obj_id):
    print('-----------',tasklog_obj_id)

    import django
    django.setup()
    from jumpserver import models
    tasklog_obj = models.TaskLog.objects.get(id=tasklog_obj_id)
    #print("run bacth cmd...",host_obj_id,task_obj)

    try:

        bind_host_obj = tasklog_obj.bind_host
        print('bind host obj',bind_host_obj)

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(bind_host_obj.host.ip_addr, bind_host_obj.host.port,
                    bind_host_obj.host_user.username, bind_host_obj.host_user.password,
                    timeout=15)
        stdin,stdout, stderr = ssh.exec_command(tasklog_obj.task.content)
        result = stdout.read() + stderr.read()
        ssh.close()

        print("-----------%s----------"% bind_host_obj.host.ip_addr)
        print(result)

        tasklog_obj.result = result
        tasklog_obj.status = 0

        tasklog_obj.save()

    except Exception as e :
        tasklog_obj.result = str(e)
        tasklog_obj.status = 1
        tasklog_obj.save()


def file_transfer(tasklog_id,task_id):
    import django
    django.setup()
    from django.conf import settings
    from jumpserver import models
    tasklog_obj = models.TaskLog.objects.get(id=tasklog_id)

    try:
        t = paramiko.Transport((tasklog_obj.bind_host.host.ip_addr,tasklog_obj.bind_host.host.port))
        t.connect(username=tasklog_obj.bind_host.host_user.username,password=tasklog_obj.bind_host.host_user.password)
        sftp = paramiko.SFTPClient.from_transport(t)

        task_data =json.loads( tasklog_obj.task.content)
        log = ""
        if task_data.get('transfer_type') == 'send':
            print("send file to remote",task_data)
            local_dir = "%s/%s/%s" %(settings.UPLOADS_DIR,tasklog_obj.task.account_id,task_data.get('random_tag'))
            remote_path = task_data.get("remote_path")
            for filename in os.listdir(local_dir):
                sftp.put("%s/%s"%(local_dir,filename),"%s/%s"%(remote_path,filename) )
                log += "send file %s to remote [%s] done\n" %( filename,"%s/%s"%(remote_path,filename) )
        else:
            print("download file ",task_data)
            local_dir = "%s/%s" %(settings.DOWNLOADS_DIR,task_id)
            if not  os.path.isdir(local_dir):
                os.mkdir(local_dir)
            remote_path = task_data.get("remote_path")
            filename = remote_path.split("/")[-1]
            sftp.get(remote_path, "%s/%s.%s" %(local_dir,filename,tasklog_obj.bind_host.host.ip_addr) )
            log += "get remote file [%s] done"% remote_path

        t.close()
        tasklog_obj.result = log
        tasklog_obj.status =  0

    except Exception as e :
        print('error ',e)
        tasklog_obj.result = str(e)
        tasklog_obj.status = 1

    tasklog_obj.save()

if __name__ == "__main__":

    task_id = sys.argv[1]
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.append(base_dir)
    #print(base_dir)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "luffyEye.settings")
    import django
    django.setup()
    from jumpserver import models

    #1.get task obj from db
    #2.for i in task.bind_hosts.all()
    task_obj = models.Task.objects.get(id=task_id)
    print(task_obj)
    pool = multiprocessing.Pool(processes=10)
    if task_obj.task_type == 0:
        task_func = run_cmd
    else:
        task_func = file_transfer
    for tasklog_obj in task_obj.tasklog_set.all():
        pool.apply_async(task_func,args=[tasklog_obj.id,task_obj.id])
    pool.close()
    pool.join()
    print("------------done----------")