from django.shortcuts import render,HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from asset import utils
from asset import core
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
