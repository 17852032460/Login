#encoding: utf-8

from flask import Flask, url_for, redirect
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    login_url = url_for('login')
    return redirect(login_url)
    return u'首页'

@app.route('/login/')
def login():
    return u'登录页面'

@app.route('/question/')
def question():
    return '查询页面'

if __name__ == '__main__':
    app.run()
