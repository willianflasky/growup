class BaseAdmin(object):

    list_display = ()
    list_filter = ()
    list_per_page = 5
    search_fields = []
    filter_horizontal = []
    default_actions = ["delete_obj"]
    actions = []
    readonly_fields = []

    def delete_obj(self,request,queryset):
        print('default....')






class AdminSite(object):
    def __init__(self):
        self.registered_admins = {}

    def register(self, model_or_iterable, admin_class=BaseAdmin, **options):
        """
        负责把每个App下的表注册self.registered_admins集合里
        :param model_or_iterable:
        :param admin_class:
        :param options:
        :return:
        """

        admin_class = admin_class()
        #admin_class.actions += admin_class.default_actions #拼接默认action
        admin_class.model = model_or_iterable #把model装到了admin class,以供simple tags调用

        app_label = model_or_iterable._meta.app_label
        if app_label not in self.registered_admins:
            self.registered_admins[app_label] =  {}
        self.registered_admins[app_label][model_or_iterable._meta.model_name] = admin_class


site = AdminSite()