from django.shortcuts import render,HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from asset import utils
from asset import core
from asset import models

from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import serializers
from asset import rest_searilizers
from rest_framework import status
from rest_framework.response import Response


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







@api_view(['GET', 'POST'])
def eventlog_list(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        eventlogs = models.EventLog.objects.all()
        serializer = rest_searilizers.EventLogSerializer(eventlogs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print("request", request.data)
        serializer =rest_searilizers.EventLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
@csrf_exempt
def eventlog_detail(request, pk):
    """
    Retrieve, update or delete a code eventlog.
    """
    try:
        eventlog_obj = models.EventLog.objects.get(pk=pk)
    except models.EventLog.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = rest_searilizers.EventLogSerializer(eventlog_obj)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        print(request)
        data = JSONParser().parse(request)
        serializer = rest_searilizers.EventLogSerializer(eventlog_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        eventlog_obj.delete()
        return HttpResponse(status=204)