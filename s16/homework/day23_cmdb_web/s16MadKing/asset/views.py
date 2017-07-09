from django.shortcuts import render, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from asset import core
from asset import utils
from asset.models import *
import datetime

# Create your views here.


@csrf_exempt
def asset_with_no_asset_id(request):
    if request.method == 'POST':
        ass_handler = core.Asset(request)
        res = ass_handler.get_asset_id_by_sn()
        # return render(request,'assets/acquire_asset_id_test.html',{'response':res})
        return HttpResponse(json.dumps(res))


@csrf_exempt
@utils.token_required
def asset_report(request):
    if request.method == "POST":
        ass_handler = core.Asset(request)
        if ass_handler.data_is_valid():
            ass_handler.data_inject()
        return HttpResponse(json.dumps(ass_handler.response))


def login(request):
    pass


def index(request):
    return render(request, 'index.html', locals())


def asset(request):
    from asset.page import PageInfo
    all_count = Asset.objects.all().count()
    page_info = PageInfo(request.GET.get('p'), 20, all_count, request.path_info, page_range=3)
    objs = Asset.objects.all()[page_info.start():page_info.end()]

    # result = []
    # all_data = Asset.objects.all().values()
    # for line in all_data:
    #     line['create_date'] = line['create_date'].strftime('%Y-%m-%d %H:%M:%S')
    #     line['update_date'] = line['update_date'].strftime('%Y-%m-%d %H:%M:%S')
    #     result.append(line)
    return render(request, 'asset.html', locals())


def data(request):
    # 图表1
    asset_list_num = []
    asset_list = []
    asset_dic = {'server': "服务器", 'networkdevice': "网络设备", 'storagedevice': "存储设备",
                  'securitydevice': "安全设备", 'idcdevice': "IDC设备",
                 'accescories': "备件", 'software': "软件"}
    for item, value in asset_dic.items():
        res = Asset.objects.filter(asset_type=item).count()
        asset_list_num.append(res)
        asset_list.append(value)

    # 图表2
    status_list = []
    status_result = []
    status_dic = {0: '在线', 1: '已下线', 2: '未知', 3: '故障', 4: '备用'}

    for item, value in status_dic.items():
        status_tmp = {'value': 0, 'name': ""}
        res = Asset.objects.filter(status=item).count()
        status_list.append(value)
        status_tmp['value'] = res
        status_tmp['name'] = value
        status_result.append(status_tmp)

    data = {
        'p11': asset_list,
        'p12': asset_list_num,
        'p21': status_list,
        'p22': status_result
    }
    return HttpResponse(json.dumps(data))
