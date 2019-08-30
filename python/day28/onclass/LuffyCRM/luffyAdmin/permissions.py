from luffyAdmin import perm_custom_funcs
perm_dic= {
    'crm_table_index': ['app_index', 'GET', [], {}, ],  # 可以查看CRM APP里所有数据库表
    'crm_table_list': ['model_table_list', 'GET', [], {'source':1},perm_custom_funcs.only_view_own_customers],  # 可以查看每张表里所有的数据
    'crm_table_list_view': ['table_obj_change', 'GET', ['source','consultant'], {}],  # 可以访问表里每条数据的修改页
    'crm_table_list_change': ['table_obj_change', 'POST', ["source"], {}],  # 可以对表里的每条数据进行修改

}


