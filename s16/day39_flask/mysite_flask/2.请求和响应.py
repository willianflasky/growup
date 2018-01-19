#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/1/18 上午10:59
__author__ = "willian"

from flask import Flask, render_template, request, redirect, session, url_for, views, jsonify, make_response
from urllib.parse import urlencode, quote, unquote

app = Flask(__name__, template_folder="templates", static_url_path="/static")

app.secret_key = 'xx'


@app.route('/index', methods=['get', 'post'])
def index():
    # get_data = request.args
    # v = request.args.to_dict()        # url变成字典
    # url = urlencode(v)                # 字典变成url
    # v = request.args.getlist('nid')
    # print(v)
    return "from index"


if __name__ == '__main__':
    app.run()
