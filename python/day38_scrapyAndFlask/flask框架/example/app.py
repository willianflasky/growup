from flask import Flask, render_template, request, redirect
from flask import url_for, session, make_response, get_flashed_messages, message_flashed, flash, views

# 指定静态文件目录 static_folder指定静态目录， static_url_path引用别名(默认不指定，则等于"/static")
app = Flask(__name__, static_folder='static')

# session放在cookie加密的密码
app.secret_key = "password"


DB = {
    "1": ['赵凤凤', '女'],
    "2": ['银秋良', '女'],
    "3": ['吴一飞', '女'],
}


@app.route('/login', methods=['GET', 'POST'])
def login():
    print(request.method)   # get or post方法
    print(request.args)     # get 参数
    print(request.form)     # post表单
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form.get('username')
        pwd = request.form.get('password')

        if user == 'alex' and pwd == '123':
            # return redirect('http://www.baidu.com')
            session['user_info'] = 'alex'  # 用户信息存放在session
            return redirect(url_for('index'))  # redirect到 index函数名
        else:
            return render_template('login.html', msg="用户名或密码")


@app.route('/index', methods=['GET', ])
def index():
    if not session.get('user_info'):
        return redirect(url_for('login'))

    return render_template('index.html', data_list=DB)


def func(a1, a2):
    return "<a href='http://www.baidu.com'>百度云</a>"


@app.route('/detail/<nid>', methods=['GET', ])
def detail(nid):
    if not session.get('user_info'):
        return redirect(url_for('login'))

    user_detail = DB[nid]
    return render_template('detail.html', **{'user_detail': user_detail, 'func': func})


# 测试message功能，闪现
@app.route('/test1')
def test1():
    val = request.args.get('p')
    # 在这里将参数存入
    flash(val)
    return "test1"


@app.route('/test2')
def test2():
    # 将test1存入的参数在这里取到
    messages = get_flashed_messages()
    print(messages)
    return "test2"


if __name__ == '__main__':
    app.run()
