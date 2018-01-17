from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__, template_folder="templates", static_url_path="/static")

app.secret_key = 'xx'


# 装饰器，认证
def auth(func):
    def wrapper(*args, **kwargs):
        if session.get('user_info'):
            res = func(*args, **kwargs)
            return res
        else:
            return redirect(url_for('login'))
    return wrapper


@app.route('/login', methods=['GET', 'POST'])
def login():
    # return 'login ....!'        # HttpResponse
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        print(request.values)  # get+post
        print(request.form)  # post请求的值
        print(request.query_string)  # get请求的值

        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'alex' and pwd == '123':
            session['user_info'] = user
            return redirect('/index')
        else:
            return render_template('login.html', msg="user or password error!")


@app.route('/index', methods=['get'])
@auth
def index():
    return "<h1>欢迎光临</h1>"


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('user_info', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
