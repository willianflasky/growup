
import json
import subprocess
from jumpserver import models
from django import conf
from django.db.transaction import atomic
import os

class Task(object):
    """发起批量任务、包括文件和命令"""

    def __init__(self,request):
        self.request = request
        self.errors = []
        self.task_data = None


    def is_valid(self):
        raw_data = self.request.POST.get('task_data')
        if raw_data:
            data  = json.loads(raw_data)
            if not data.get('selected_host_ids'):
                self.errors.append({'invalid_argument':"host list is empty or not provided"})
            if data.get('task_type') == 'cmd':
                if not data.get('cmd'):
                    self.errors.append({'invalid_argument':"cmd  is empty or not provided"})
            else:
                #判断远程路径是否已填写，还有random tag
                pass
        else:
            self.errors.append({'invalid_task_data': "task data argument is not exist."})

        if not self.errors:
            self.task_data = data
            return  True

    def run(self):
        print('---------sdfsfsdf')
        # 1 . 生成task id
        # 2. 根据任务类型，启动独立进程执行对应的批量任务
        # 3. 返回Task id到前端

        task_func = getattr(self, self.task_data.get('task_type'))
        res = task_func()
        return res

    @atomic
    def cmd(self):
        """批量命令"""

        task_obj = models.Task.objects.create(
            task_type = 0 ,
            account = self.request.user,
            content = self.task_data.get('cmd'),
            pid=0
        )
        #task_obj.bind_hosts.add(*self.task_data.get('selected_host_ids'))

        tasklog_objs = []

        for host_id in self.task_data.get('selected_host_ids'):
            tasklog_objs.append(models.TaskLog(
                task_id=task_obj.id,
                bind_host_id=host_id,
                result = 'init....',
                status = 2,

            ))

        models.TaskLog.objects.bulk_create(tasklog_objs,batch_size=100)


        # start 批量任务的进程了

        multitask_process = subprocess.Popen("%s %s" %(conf.settings.MULTITASK_SCRIPT,task_obj.id) ,
                                             shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                                             preexec_fn=os.setsid)

        #print((multitask_process.stdout.read() + multitask_process.stderr.read()).decode('gbk'))
        print('task pid ',multitask_process.pid )
        task_obj.pid = multitask_process.pid
        task_obj.save()
        return task_obj

    @atomic
    def file_transfer(self):
        """
        1. 生成任务记录
        2. 触发任务脚本
        3. 返回任务id

        :return:
        """
        task_obj = models.Task.objects.create(
            task_type = 1 ,
            account = self.request.user,
            content = json.dumps(self.task_data),
            pid=0
        )
        #task_obj.bind_hosts.add(*self.task_data.get('selected_host_ids'))

        tasklog_objs = []

        for host_id in self.task_data.get('selected_host_ids'):
            tasklog_objs.append(models.TaskLog(
                task_id=task_obj.id,
                bind_host_id=host_id,
                result = 'init....',
                status = 2,

            ))

        models.TaskLog.objects.bulk_create(tasklog_objs,batch_size=100)
        multitask_process = subprocess.Popen("%s %s" %(conf.settings.MULTITASK_SCRIPT,task_obj.id) ,
                                             shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                                             #preexec_fn=os.setsid)

        #print((multitask_process.stdout.read() + multitask_process.stderr.read()).decode('gbk'))
        print('task pid ',multitask_process.pid )
        task_obj.pid = multitask_process.pid
        task_obj.save()
        return task_obj