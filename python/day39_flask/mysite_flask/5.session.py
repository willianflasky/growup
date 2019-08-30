
from flask import Flask
from flask import session
from lib.mysession import MySessionInterface

app = Flask(__name__)

app.secret_key = 'xx'
app.config['SESSION_COOKIE_NAME'] = "my_session"
app.session_interface = MySessionInterface()


@app.route('/login.html', methods=['GET', "POST"])
def login():
    print(session)
    session['user1'] = 'alex'
    session['user2'] = 'alex'
    del session['user2']

    return "内容"


if __name__ == '__main__':
    app.run()

