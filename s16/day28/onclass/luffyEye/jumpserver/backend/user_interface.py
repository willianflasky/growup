from django.contrib.auth import authenticate
from jumpserver.backend import demo
from jumpserver import models


class UserInteractive(object):
    """用户的shell 界面"""
    def __init__(self, sys_argv):
        self.sys_args = sys_argv
        self.user = None

    def auth(self):
        count = 0
        while count < 3:
            username = input("Username:").strip()
            password = input("Password:").strip()
            # 用户名密码验证
            user = authenticate(username=username, password=password)          # django自带的验证功能
            if user:
                self.user = user            # 验证成功了,把用户存下来.
                print(self.user.host_groups.all())
                return True
            else:
                print("Wrong username or password!")
                count += 1
        else:
            exit("Too many attempts !")

    def welcome_msg(self):
        msg = """Welcome logon Luffy JumpServer terminal""".center(80, '-')
        print(msg)

    def start(self):
        """登录交互入口"""
        if self.auth():
            self.welcome_msg()

            while True:
                # 拿到这个用户所有关联组,HostGroup表的数据
                host_groups = self.user.host_groups.all()
                # 拿到这个用户所有关联权限,BindHostUser表的数据
                ungroupped_hostlist = self.user.bind_host_users.all()

                # 循环组的数据
                for index, group in enumerate(host_groups):
                    print(index, group)

                choice = input("\033[31;1mselect group >>:\033[0m").strip()
                if choice.isdigit():
                    choice = int(choice)

                    if choice < len(host_groups) and choice >= 0:
                        # 拿到想要的组对象
                        selected_group = host_groups[choice]
                        # 通过组对象去拿 BindHostUser权限数据
                        bind_host_user_list = selected_group.bind_host_users.all()
                    if choice == len(host_groups):          # 去拿未分组机器
                        # bind_host_user_list = self.user.bind_host_users.all()
                        bind_host_user_list = ungroupped_hostlist
                    # 上面如果选择(choice)到group就取组对应的权限数据
                    # 如果超出组的选择,就去未分配的组中取权限数据
                    elif choice > len(host_groups):
                        print("请输入范围内")
                        continue

                    while True:
                        # 循环分组的权限数据,或者去未分组循环权限数据
                        for index, host in enumerate(bind_host_user_list):
                            print("\t", index, host)
                        choice = input("\033[31;1mselect host >>:\033[0m").strip()
                        if choice.isdigit():
                            choice = int(choice)
                            if choice < len(bind_host_user_list) and choice >= 0:
                                selected_host = bind_host_user_list[choice]  # 选中的主机
                                # start login 1.传入主机对象, 2.传入表models
                                demo.ssh_channel(self, selected_host, models)       # self里面存有self.user

                        elif choice == 'b':
                            break
                        elif choice == 'exit':
                            exit("bye.")

                elif choice == 'exit':
                    exit("bye.")





