from django.shortcuts import render,HttpResponse

# Create your views here.
import time
import requests
import re
import json

from bs4 import BeautifulSoup


def ticket(html):
    ret = {}
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.find(name='error').find_all():
        ret[tag.name] = tag.text
    return ret


def login(req):
    if req.method == 'GET':
        uuid_time = int(time.time()*1000)
        base_uuid_url = "https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={0}"
        uuid_url = base_uuid_url.format(uuid_time)
        r1 = requests.get(uuid_url)
        result = re.findall('= "(.*)";', r1.text)
        uuid = result[0]
        req.session['UUID_TIME'] = uuid_time
        req.session['UUID'] = uuid
        return render(req, 'login.html', {'uuid':  uuid})


def check_login(req):
    response = {'code': 408, 'data': None}

    ctime = int(time.time()*1000)
    base_login_url = "https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={0}&tip=0&r=-735595472&_={1}"
    login_url = base_login_url.format(req.session['UUID'], ctime)
    r1 = requests.get(login_url)
    if 'window.code=408' in r1.text:
        # 无人扫码
        response['code'] = 408
    elif 'window.code=201' in r1.text:
        # 扫码，返回头像
        response['code'] = 201
        response['data'] = re.findall("window.userAvatar = '(.*)';", r1.text)[0]
    elif 'window.code=200' in r1.text:
        # 扫码，并确认登录
        req.session['lOGIN_COOKIE'] = r1.cookies.get_dict()

        base_redirect_url = re.findall('redirect_uri="(.*)";', r1.text)[0]
        redirect_url = base_login_url + "&fun=new&version=v2"

        r2 = requests.get(redirect_url)
        ticket_dict = ticket(r2.text)
        req.session['TICKET_DICT'] = ticket_dict
        req.session['TICKET_COOKIE'] = r2.cookies.get_dict()

        # 初始化,获取最近联系人和公众号
        post_data = {
            "BaseRequest": {
                "DeviceID": "e384757757885382",
                'Sid': ticket_dict['wxsid'],
                'Uin': ticket_dict['wxuin'],
                'Skey': ticket_dict['skey'],
            }
        }

        # 用户初始化，讲最近联系人个人信息放在session中
        init_url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=-740036701&pass_ticket={0}".format(ticket_dict['pass_ticket'])
        r3 = requests.post(
            url=init_url,
            json=post_data
        )
        r3.encoding = 'utf-8'
        init_dict = json.loads(r3.text)

        response['code'] = 200

        # 获取凭证
        """
        window.code=200;
        window.redirect_uri="https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage?ticket=AeK6zEL_D6P7dYTg2VFe6ktB@qrticket_0&uuid=gZEMxSJoyg==&lang=zh_CN&scan=1503975940";
        """
        pass

    return HttpResponse(json.dumps(response))


def index(req):
    """
        显示最近联系人
    """
    return HttpResponse("");