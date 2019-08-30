



from django.contrib.auth import authenticate
from jumpserver.backend import demo
from jumpserver import models
import random,string
import subprocess

class UserInteractive(object):
    """用户的shell 界面"""
    def __init__(self,sys_argv):
        self.sys_args = sys_argv
        self.user = None

    def auth(self):
        count = 0
        while count <3:
            username = input("Username:").strip()
            password = input("Password:").strip()
            user = authenticate(username=username,password=password)
            if user:
                #print("pass authentication")
                self.user = user
                return True
            else:
                print("Wrong username or password!")
                count += 1
        else:
            exit("Too many attempts !")


    def welcome_msg(self):
        msg = """Welcome logon Luffy JumpServer terminal""".center(80,'-')
        print(msg)

    def start(self):
        """登录交互入口"""
        if self.auth():
            self.welcome_msg()

            while True:
                host_groups =  self.user.host_groups.all()
                ungroupped_hostlist  =  self.user.bind_host_users.all()

                for index,group in enumerate(host_groups):
                    print(index,group)
                print(len(host_groups), "未分组主机")

                choice = input("select group >>:").strip()
                if choice.isdigit():
                    choice = int(choice)
                    if choice < len(host_groups) and choice >=0:
                        selected_group = host_groups[choice]
                        bind_host_user_list  = selected_group.bind_host_users.all()
                    if choice == len(host_groups):#未分组机器
                        bind_host_user_list = self.user.bind_host_users.all()

                    while True:
                        for index, host in enumerate(bind_host_user_list):
                            print("\t", index, host)
                        choice = input("select host >>:").strip()
                        if choice.isdigit():
                            choice = int(choice)
                            if choice < len(bind_host_user_list) and choice >= 0:
                                selected_host = bind_host_user_list[choice]  # 选中的主机
                                #start login
                                #demo.ssh_channel(self,selected_host,models)
                                #换成原生ssh
                                random_tag = ''.join(random.sample(string.ascii_lowercase + string.digits,8))
                                subprocess.Popen('strace....')
                                cmd = 'sshpass -p %s ssh %s@%s -p %s -Z %s' %(selected_host.host_user.password,
                                                                        selected_host.host_user.username,
                                                                        selected_host.host.ip_addr,selected_host.host.port,
                                                                        random_tag)
                                cmd_obj = subprocess.run(cmd,shell=True)
                                print('--------------------')

                        elif choice == 'b':
                            break
                        elif choice == 'exit':
                            exit("bye.")

                elif choice == 'exit':
                    exit("bye.")





