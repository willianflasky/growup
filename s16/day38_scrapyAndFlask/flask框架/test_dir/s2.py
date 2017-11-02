from flask import Flask

app = Flask(__name__)


# 1. app.route('/xxxxxxx'),返回了一个函数，decorator
# 2. decorator(hello_world)


@app.route('/xx/<int:nid>/<int:bid>')
def hello_world(nid,bid):
    return 'Hello World!'+ str(nid)



if __name__ == '__main__':
    app.run()