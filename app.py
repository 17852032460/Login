#encoding: utf-8

from flask import Flask, url_for, redirect, render_template, request
import config, pymysql

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/user_register/', methods=['GET', 'POST'])
def user_register():
    get_id = request.form['id']
    get_password = request.form['password']
    get_repassword = request.form['repassword']
    if get_password == get_repassword:
        db = pymysql.connect(host = 'localhost', port = 3306, user = 'root', password = '236326', db = 'myproj', charset = 'utf8')
        cursor = db.cursor()
        sql = "INSERT INTO users(id, password) VALUES('%s', '%s')" % (get_id, get_password)
        cursor.execute(sql)
        db.commit()
        db.close()
        return redirect('/login/')
    else:
        return redirect('/register/')

@app.route('/user_login/', methods=['GET', 'POST'])
def user_login():
    get_id = request.form['id']
    get_password = request.form['password']
    db = pymysql.connect(host='localhost', port=3306, user='root', password='236326', db='myproj', charset='utf8')
    cursor = db.cursor()
    sql = "SELECT password FROM users where id = '%s'" % get_id
    cursor.execute(sql)
    password = cursor.fetchone()
    db.commit()
    db.close()
    if password[0] == get_password:
        return redirect('/question')
    else:
        return redirect('/login/')

@app.route('/question/')
def question():
    return '查询页面'

if __name__ == '__main__':
    app.run()
