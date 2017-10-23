from django.shortcuts import render,HttpResponse,redirect
import time
import requests
import re
import json
from utils.ticket import get_ticket_dict



def login(request):
    print('开始获取二维码')
    ctime = time.time()*1000
    login_url ="https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={0}".format(ctime)

    response = requests.get(login_url)
    result = re.findall('window.QRLogin.uuid = "(.*)";',response.text)
    qcode = result[0] if result else ""

    request.session['qcode'] = qcode
    request.session['ctime'] = ctime

    return render(request,'login.html',{'qcode':qcode})

def check_login(request):
    ret = {'code':408, 'data':None}
    tip = request.GET.get('tip')
    check_login_url = "https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={0}&tip={1}&_={2}"
    check_login_url = check_login_url.format(request.session['qcode'],tip,time.time()*1000)
    response = requests.get(check_login_url)
    print(response.text)
    if "window.code=408;" in response.text:
        return HttpResponse(json.dumps(ret))
    elif 'window.code=201;' in response.text:
        user_avatar = re.findall("window.userAvatar = '(.*)';",response.text)
        avatar= user_avatar[0] if user_avatar else ''
        ret['code'] = 201
        ret['data'] = avatar
        return HttpResponse(json.dumps(ret))
    elif 'window.code=200' in response.text:
        print('点击确认登录',response.text)

        login_cookie_dict = response.cookies.get_dict()
        request.session['login_cookie_dict'] = login_cookie_dict

        redirect_url = re.findall('window.redirect_uri="(.*)";',response.text)
        redirect_url = redirect_url[0] if redirect_url else ""
        func_version = "&fun=new&version=v2"
        redirect_url = redirect_url + func_version
        print(redirect_url)
        # 获取xml格式凭证
        ticket_response = requests.get(redirect_url)
        ticket_dict = get_ticket_dict(ticket_response.text)
        request.session['ticket_dict'] = ticket_dict
        request.session['ticket_dict_cookie'] = ticket_response.cookies.get_dict()

        print('获取到凭证',ticket_dict)
        ret['code'] = 200
        return HttpResponse(json.dumps(ret))
        # 访问： redirect_url
        # 获取：XML，cookie



    return HttpResponse('...')


def index(request):
    if not request.session.get('ticket_dict'):
        return redirect('/login.html')

    """
    https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=-1106484996&pass_ticket=
    POST
    requests.post(data="xxxx") FormData
    requests.post(json="xxxx") RequestPayload
    """
    ticket_dict = request.session['ticket_dict']

    init_url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=-1106484996&pass_ticket={0}"
    init_url = init_url.format(ticket_dict['pass_ticket'])
    post_data = {
        "BaseRequest":{
            "DeviceID": "e108459937477368",
            'Sid':ticket_dict['wxsid'],
            'Skey':ticket_dict['skey'],
            'Uin':ticket_dict['wxuin']
        }
    }
    # requests.post(init_url,json=post_data)
    response = requests.post(init_url,data=json.dumps(post_data),headers={'Content-Type':'application/json;charset=utf-8'})
    response.encoding = "utf-8"
    init_dict = json.loads(response.text)

    sync_key = init_dict.pop('SyncKey')

    request.session['sync_key'] = sync_key
    request.session['init_dict'] = init_dict



    request.session['init_cookie_dict'] = response.cookies.get_dict()


    return render(request,'index.html',{'init_dict':init_dict})


def get_user_avatar(request):
    print('开始获取头像')
    base_url = "https://wx.qq.com"
    k = request.GET.get('k')
    username = request.GET.get('username')
    skey = request.GET.get('skey')

    avatar_url = "{0}{1}&username={2}&skey={3}".format(base_url,k,username,skey)

    all_cookies = {}
    all_cookies.update(request.session['login_cookie_dict'])
    all_cookies.update(request.session['ticket_dict_cookie'])
    all_cookies.update(request.session['init_cookie_dict'])

    print(avatar_url)
    response = requests.get(avatar_url,
                            headers={
                                'Referer': 'https://wx.qq.com/?&lang=zh_CN',
                                'Host': 'wx.qq.com',
                                'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
                                'Accept': "image/webp,image/apng,image/*,*/*;q=0.8",
                            },
                            cookies=all_cookies)
    """
    1. 请求头: referer
    2. 请求头: host
    3. cookie
    """
    print(response.text)
    return HttpResponse(response.content)

    # f = open('111.png',mode='rb')
    # data = f.read()
    # f.close()
    # return HttpResponse(data)


def contact_list(request):

    print(request.session['init_dict'])


    # https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=zh_CN&r=1508653488963&seq=0&skey=@crypt_186472eb_95d2032db06d08ec291875c72509f1bf
    # GET
    ticket = request.session['ticket_dict']
    contact_list_url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=zh_CN&r=1508653488963&seq=0&skey={0}".format(ticket['skey'])

    all_cookies = {}
    all_cookies.update(request.session['login_cookie_dict'])
    all_cookies.update(request.session['ticket_dict_cookie'])
    all_cookies.update(request.session['init_cookie_dict'])

    response = requests.get(url=contact_list_url,cookies=all_cookies)
    response.encoding = 'utf-8'
    contact_list = json.loads(response.text)
    print(json.loads(response.text))

    return render(request,'contact_list.html',{'contact_list': contact_list})

def send_msg(request):
    ticket_dict = request.session['ticket_dict']
    to_user = request.GET.get('to_user')
    msg = request.GET.get('msg')
    send_msg_url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg?lang=zh_CN"
    # POST
    ctime = time.time()*1000
    post_data = {
        "BaseRequest":{
            "DeviceID": "e108459937477368",
            'Sid':ticket_dict['wxsid'],
            'Skey':ticket_dict['skey'],
            'Uin':ticket_dict['wxuin']
        },
        "Msg":{
            "ClientMsgId": ctime,
            'LocalID': ctime,
            'Content':msg,
            'FromUserName': request.session['init_dict']['User']['UserName'],
            'ToUserName': to_user,
            'Type':1
        },
        'Scene':0
    }

    all_cookies = {}
    all_cookies.update(request.session['login_cookie_dict'])
    all_cookies.update(request.session['ticket_dict_cookie'])
    all_cookies.update(request.session['init_cookie_dict'])

    # response = requests.post(url=send_msg_url,json=post_data,cookies=all_cookies)
    # print(response.text)
    # requests.post(url=send_msg_url,data=json.dumps(post_data,ensure_ascii=False),headers={'Content-Type':'application/json'})
    response = requests.post(url=send_msg_url,data=json.dumps(post_data,ensure_ascii=False).encode('utf-8'),headers={'Content-Type':'application/json'},cookies=all_cookies)
    print(response.text)
    return HttpResponse('....')


def get_msg(request):
    ctime = time.time()*1000
    ticket_dict = request.session['ticket_dict']
    sync_key = request.session['sync_key']

    sync_key_list = []
    for item in sync_key['List']:
        tpl = "%s_%s" %(item['Key'],item['Val'],)
        sync_key_list.append(tpl)


    params_dict = {
        'r':ctime,
        'skey':ticket_dict['skey'],
        'sid':ticket_dict['wxsid'],
        'uin':ticket_dict['wxuin'],
        'deviceid':"e108459937477368",
        'synckey':"|".join(sync_key_list),
        '_':ctime
    }
    all_cookies = {}
    all_cookies.update(request.session['login_cookie_dict'])
    all_cookies.update(request.session['ticket_dict_cookie'])
    all_cookies.update(request.session['init_cookie_dict'])

    # 检测是否有新消息到来
    response = requests.get('https://webpush.wx.qq.com/cgi-bin/mmwebwx-bin/synccheck',params=params_dict,cookies=all_cookies)
    print(response.text)
    if 'window.synccheck={retcode:"0",selector:"2"}' in response.text:
        # 获取新消息
        # https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsync?sid=RkeVqEgBw5LODupt&skey=@crypt_186472eb_95d2032db06d08ec291875c72509f1bf&lang=zh_CN
        get_msg_url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsync?sid={0}&skey={1}&lang=zh_CN".format(ticket_dict['wxsid'],ticket_dict['skey'])
        # post
        post_dict = {
            "BaseRequest": {
                "DeviceID": "e108459937477368",
                'Sid': ticket_dict['wxsid'],
                'Skey': ticket_dict['skey'],
                'Uin': ticket_dict['wxuin']
            },
            'SyncKey':sync_key
        }
        msg_response = requests.post(get_msg_url,json=post_dict,cookies=all_cookies)
        msg_response.encoding = 'utf-8'
        msg_dict = json.loads(msg_response.text)

        for row in msg_dict['AddMsgList']:
            print(row.get('Content'))

        request.session['sync_key'] = msg_dict['SyncKey']

    return HttpResponse('...')


def api(request):
    name = request.GET.get('name')
    msg = request.GET.get('msg')
    return HttpResponse('...')


