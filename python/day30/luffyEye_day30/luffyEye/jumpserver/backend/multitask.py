
import time,sys,os
import multiprocessing


def run_cmd(host_obj_id,task_obj_id):
    print('-----------',host_obj_id)

    import django
    django.setup()
    from jumpserver import models
    tasklog_obj = models.TaskLog.objects.get(id=host_obj_id,task_id=task_obj_id)
    #print("run bacth cmd...",host_obj_id,task_obj)

    try:
        import paramiko
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


def file_transfer():
    pass


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

    for host_obj in task_obj.tasklog_set.all():
        pool.apply_async(run_cmd,args=[host_obj.id,task_obj.id])
    pool.close()
    pool.join()
    print("------------done----------")