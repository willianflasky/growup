from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from luffyAdmin import views as admin_views


@login_required(login_url='/login/')
def index(request):

    return render(request, 'index.html', locals())


def web_logout(request):
    logout(request)
    return redirect('/')


def web_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(request.GET.get('next') or '/')
    return render(request, 'login.htm')


def customer_list(request):
    app_name = 'crm'
    model_name = 'customer'
    view_data = admin_views.model_table_list(request, app_name, model_name, no_render=True)
    return render(request, 'crm/customer_list.html', view_data)


def customer_change(request, obj_id):
    app_name = 'crm'
    model_name = 'customer'

    view_data = admin_views.table_obj_change(request, app_name, model_name, object_id=obj_id, no_render=True)
    return render(request, 'crm/customer_change.html', view_data)


def customer_add(request):
    app_name = 'crm'
    model_name = 'customer'
    view_data = admin_views.table_obj_add(request, app_name, model_name, no_render=True)
    return render(request, 'crm/customer_add.html', view_data)


def need_followup(request):
    return HttpResponse('ok')
