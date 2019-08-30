from django.shortcuts import render,redirect
from luffyAdmin import views as admin_views
# Create your views here.





def customer_list(request):
    app_name = 'crm'
    model_name = 'customer'

    view_data = admin_views.model_table_list(request,app_name,model_name,no_render=True)
    print("view data",view_data)
    return render(request,'crm/customer_list.html',view_data)


def customer_change(request,obj_id):
    app_name = 'crm'
    model_name = 'customer'
    view_data = admin_views.table_obj_change(request,app_name,model_name,object_id=obj_id,no_render=True)

    return render(request,'crm/customer_change.html',view_data)
