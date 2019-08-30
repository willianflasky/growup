from django.shortcuts import render, HttpResponse, redirect
from repository.models import *
# Create your views here.
from utils.page import PageInfo
import json
from utils import check_code as ac
from io import BytesIO
from utils.formtable import LoginForm


def editor(request):
    return render(request, 'editor.html')


def upload_img(request):
    """
    文件上传
    :param request:
    :return:
    """
    dic = {
        'error': 0,
        'url': '/static/20130809170025.png',
        'message': '错误了...'
    }
    return HttpResponse(json.dumps(dic))


def index(request):
    try:
        if request.session['user_info']:
            avatar = UserInfo.objects.filter(username=request.session['user_info']['user_name']).values('img')[0]
    except KeyError as e:
        pass
    
    all_count = News.objects.all().count()
    page_info = PageInfo(request.GET.get('p'), 6, all_count, request.path_info, page_range=3)
    objs = News.objects.filter().order_by('-nid').prefetch_related('user_info', 'news_type')[page_info.start():page_info.end()]

    return render(request, 'index.html', locals())


def qu(request, page):
    return render(request, 'qu.html', locals())


def dz(request):
    return render(request, 'dz.html', locals())


def tp(request):
    return render(request, 'tp.html', locals())


def at(request):
    return render(request, 'at.html', locals())


def nw(request):
    return render(request, 'nw.html', locals())


def favor(request):
    """
    1. 获取新闻ID
    2. 当前登录的用户ID
    3. 在favor表中插入数据
    4. 新闻表中的favor_count + 1
    :param request:
    :return:
    """
    ret = {'status': True, 'code': 0}
    if request.session.get('is_login'):
        news_id = request.POST.get('nid')
        current_user_id = request.session['user_info']['user_id']
        ct = Favor.objects.filter(user_info_id=current_user_id, news_id=news_id).count()
        if ct:
            Favor.objects.filter(user_info_id=current_user_id, news_id=news_id).delete()
            news_obj = News.objects.filter(nid=news_id).first()
            temp = news_obj.favor_count - 1
            News.objects.filter(nid=news_id).update(favor_count=temp)
            ret['code'] = 2302
        else:
            Favor.objects.create(user_info_id=current_user_id, news_id=news_id)
            news_obj = News.objects.filter(nid=news_id).first()
            temp = news_obj.favor_count + 1
            News.objects.filter(nid=news_id).update(favor_count=temp)
            ret['code'] = 2301
    return HttpResponse(json.dumps(ret))


def login(request):
    response = {'status': False, 'message': None, 'code': 200}
    if request.method == 'POST':
        code = request.POST.get('code')
        if code.upper() == request.session['check_code'].upper():
            obj_dic = LoginForm(request.POST)
            if obj_dic.is_valid():
                obj = UserInfo.objects.filter(username=obj_dic.cleaned_data['user'], password=obj_dic.cleaned_data['pwd']).first()
                if obj:
                    request.session['is_login'] = True
                    request.session['user_info'] = {'user_id': obj.nid, 'user_name': obj.username}
                    response['status'] = True
                    response['code'] = 200
                    return HttpResponse(json.dumps(response))
                else:
                    response['message'] = '用户或者密码不正确'
                    response['code'] = 400
                    return HttpResponse(json.dumps(response))
            else:
                response['status'] = False
                response['message'] = obj_dic.errors
                response['code'] = 401
                print(obj_dic.errors)
                return HttpResponse(json.dumps(response))
        else:
            response['code'] = 402
            return HttpResponse(json.dumps(response))

    return render(request, 'login.html')


def check_code(request):
    # 后台生成图片，并在图片上写文字
    # 自己写一个空白图片
    # 在图片上写文字
    img_obj, code = ac.create_validate_code()
    stream = BytesIO()
    img_obj.save(stream, 'png')
    request.session['check_code'] = code
    return HttpResponse(stream.getvalue())


def logout(request):
    request.session.clear()
    return redirect("/")


def comment(request):
    # 模拟数据
    # comment_list = [
    #     {'id': 1, 'news_id': 1, 'user_id': 10, 'content': "写的什么玩意呀", 'reply_id': None},
    #     {'id': 2, 'news_id': 1, 'user_id': 11, 'content': "还真不是玩意 ", 'reply_id': 1},
    #     {'id': 3, 'news_id': 1, 'user_id': 12, 'content': "写的真好 ", 'reply_id': 1},
    #     {'id': 4, 'news_id': 1, 'user_id': 11, 'content': "写的真好 ", 'reply_id': 3},
    #     {'id': 5, 'news_id': 1, 'user_id': 19, 'content': "balabala ", 'reply_id': None},
    #     {'id': 6, 'news_id': 1, 'user_id': 11, 'content': "你可以趣事了 ", 'reply_id': 2},
    #     {'id': 7, 'news_id': 1, 'user_id': 11, 'content': "号的", 'reply_id': 6},
    # ]
    comment_list = []

    new_nid = request.GET.get('nid')
    obj = News.objects.filter(nid=new_nid)[0]
    for row in obj.comment_set.values():
        comment_list.append(row)

    # 一.变成字典,id为K, 字典为V
    comment_dict = {}
    for row in comment_list:
        row['child'] = []  # 增加空字段
        comment_dict[row['nid']] = row  # ID做为K,行数据做V

    # 二.找到replay_id后,加到后面的child, python数据类型,除了int,str其它都是引用.
    for row in comment_list:
        if row['reply_id_id']:
            replay_id = row['reply_id_id']
            comment_dict[replay_id]['child'].append(row)

    # 三.这样回复链就做好了.
    commen_reuslt = {}
    for k, v in comment_dict.items():
        if v['reply_id_id'] == None:
            commen_reuslt[k] = v

    commen_reuslt = create_html(commen_reuslt)
    return HttpResponse(json.dumps(commen_reuslt, ensure_ascii=False))


def create_child_node(child_comment):
    prev = """
        <div class="comment1">
            <div class="content1">
        """
    for child in child_comment:
        tpl = '<div class="item">%s</div>'
        content = tpl % child['content']
        prev = prev + content
        if child['child']:
            # 有子评论
            node = create_child_node(child['child'])
            prev = prev + node

    end = """
            </div>
        </div>
        """
    return prev + end


def create_html(comment_result):
    prev = """
    <div class="comment1">
        <div class="content1">
    """

    for k,v in comment_result.items():
        tpl = '<div class="item">%s</div>'
        content = tpl %v['content']
        prev = prev + content
        if v['child']:
            # 有子评论
            node = create_child_node(v['child'])
            prev = prev + node

    end = """
        </div>
    </div>
    """
    return prev + end