import json
from django.shortcuts import render,HttpResponse,redirect
from repository import models
from utils import check_code as ac
from io import BytesIO


def index(request):
    news_list = models.News.objects.all()
    return render(request,'index.html',{'news_list': news_list})

def do_favor(request):
    """
    1. 获取新闻ID
    2. 当前登录的用户ID
    3. 在favor表中插入数据
    4. 新闻表中的favor_count + 1
    :param request:
    :return:
    """
    ret = {'status': 0, 'error': ''}
    if request.session.get('is_login'):
        news_id = request.GET.get('nid')
        current_user_id = request.session['user_info']['user_id']
        ct = models.Favor.objects.filter(user_info_id=current_user_id,news_id=news_id).count()
        if ct:
            models.Favor.objects.filter(user_info_id=current_user_id, news_id=news_id).delete()
            news_obj = models.News.objects.filter(nid=news_id).first()
            temp = news_obj.favor_count - 1
            models.News.objects.filter(nid=news_id).update(favor_count=temp)
            ret['status'] = 1
        else:
            models.Favor.objects.create(user_info_id=current_user_id,news_id=news_id)
            news_obj = models.News.objects.filter(nid=news_id).first()
            temp = news_obj.favor_count + 1
            models.News.objects.filter(nid=news_id).update(favor_count=temp)
            ret['status'] = 2
    return HttpResponse(json.dumps(ret))

def login(request):

    if request.method == 'GET':
        return render(request,'login.html')
    else:
        code = request.POST.get('code')
        if code.upper() == request.session['check_code'].upper():
            obj = models.UserInfo.objects.filter(username=request.POST.get('username'),password=request.POST.get('password')).first()
            if obj:
                request.session['is_login'] = True
                request.session['user_info'] = {'user_id': obj.nid,'user_name': obj.username}
                return redirect('/index/')
            else:
                return render(request, 'login.html')
        else:
            print('验证码错误')
            return render(request, 'login.html')


def check_code(request):
    # {  # 后台生成图片，并在图片上写文字#}
    # 自己写一个空白图片
    # 在图片上写文字
    img_obj, code = ac.create_validate_code()
    stream = BytesIO()
    img_obj.save(stream,'png')
    request.session['check_code'] = code
    return HttpResponse(stream.getvalue())





def comment(request):
    """
    ID      新闻ID    用户ID       评论给内容                             reply_id
    1         1        10           写的什么玩意呀                          null
    2         1        11           还真不是玩意                             1
    3         1        12           写的真好                                 1
    4         1        11           我总算看明白了，原来是我智商低            3
    """
    # models.Comment.objects.filter(news_id=1).values('nid','news_id','user_info_id','content','reply_id')

    comment_list = [
        {'id': 1, 'news_id': 1, 'user_id': 10, 'content': "写的什么玩意呀", 'reply_id': None},
        {'id': 2, 'news_id': 1, 'user_id': 11, 'content': "还真不是玩意 ", 'reply_id': 1},
        {'id': 3, 'news_id': 1, 'user_id': 12, 'content': "写的真好 ", 'reply_id': 1},
        {'id': 4, 'news_id': 1, 'user_id': 11, 'content': "写的真好 ", 'reply_id': 3},
        {'id': 5, 'news_id': 1, 'user_id': 19, 'content': "sdfsfsdsd ", 'reply_id': None},
        {'id': 6, 'news_id': 1, 'user_id': 11, 'content': "你可以趣事了 ", 'reply_id': 2},
        {'id': 7, 'news_id': 1, 'user_id': 11, 'content': "号的", 'reply_id': 6},
    ]

    comment_dict = {}
    for row in comment_list:
        row['child'] = []
        comment_dict[row['id']] = row

    for row in comment_list:
        if row['reply_id']:
            reply_id = row['reply_id']
            comment_dict[reply_id]['child'].append(row)

    commen_reuslt = {}
    for k, v in comment_dict.items():
        if v['reply_id'] == None:
            commen_reuslt[k] = v

    # 根据commen_reuslt生成
    cmt_str = create_html(commen_reuslt)
    return render(request,'comment.html',{'cmt_str': cmt_str})

def create_child_node(child_comment):
    prev = """
        <div class="comment">
            <div class="content">
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
    <div class="comment">
        <div class="content">
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












