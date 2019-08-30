from django.shortcuts import render,HttpResponse
from assets import utils
# Create your views here.

from django.views.decorators.csrf import csrf_exempt
import json
from assets import core,models


# 跳过csrf验证
@csrf_exempt
def asset_with_no_asset_id(request):
    if request.method == 'POST':
        ass_handler = core.Asset(request)
        # 重点在core里面
        res = ass_handler.get_asset_id_by_sn()
        # 通过sn拿到资产id
        # return render(request,'assets/acquire_asset_id_test.html',{'response':res})
        return HttpResponse(json.dumps(res))


@csrf_exempt
@utils.token_required
# api接口认证
def asset_report(request):
    if request.method == 'POST':
        ass_handler = core.Asset(request)
        if ass_handler.data_is_valid():
            # 插入更新数据
            ass_handler.data_inject()
        return HttpResponse(json.dumps(ass_handler.response))