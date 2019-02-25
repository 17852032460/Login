#encoding: utf-8

from flask import Flask, url_for, redirect, render_template
import config, pymysql


app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/register/')
def register():
    return render_template('register.html')

@app.route('/user_register/')
def user_register():
    db = pymysql.connect('localhost', 'root', '236326', 'myproj', 3306)
    cursor = db.cursor()
    sql = "INSERT INTO users VALUES('%s', '%s') % (request.from.get('id'), request.from.get('password'))"
    cursor.execute(sql)
    db.commit()
    db.close()
    return render_template('login.html')

@app.route('/question/')
def question():
    return '查询页面'

if __name__ == '__main__':
    app.run()
