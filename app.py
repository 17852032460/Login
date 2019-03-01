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

@app.route('/wrong/<be>', methods=['GET', 'POST'])
def wrong(be):
    if be == '1':
        return render_template("wrong1.html")
    elif be == '2':
        return render_template("wrong2.html")
    elif be == '3':
        return render_template("wrong3.html")

@app.route('/user_register/', methods=['GET', 'POST'])
def user_register():
    get_username = request.form['username']
    get_nickname = request.form['nickname']
    get_password = request.form['password']
    get_repassword = request.form['repassword']
    if get_password == get_repassword:
        db = pymysql.connect(host = 'localhost', port = 3306, user = 'root', password = '236326', db = 'myproj', charset = 'utf8')
        cursor = db.cursor()
        sql_query = "SELECT username FROM users where username = '%s'" % get_username
        sql_insert = "INSERT INTO users(username, nickname, password) VALUES('%s', '%s', '%s')" % (get_username, get_nickname, get_password)
        cursor.execute(sql_query)
        judgeUsername = cursor.fetchone()
        if judgeUsername != None:
            db.commit()
            db.close()
            return redirect('/wrong/3')
        else:
            cursor.execute(sql_insert)
            db.commit()
            db.close()
            return render_template('successlogin.html')
    else:
        return redirect('/wrong/2')

@app.route('/user_login/', methods=['GET', 'POST'])
def user_login():
    get_username = request.form['username']
    get_password = request.form['password']
    db = pymysql.connect(host='localhost', port=3306, user='root', password='236326', db='myproj', charset='utf8')
    cursor = db.cursor()
    sql = "SELECT password FROM users where username = '%s'" % get_username
    cursor.execute(sql)
    password = cursor.fetchone()
    db.commit()
    db.close()
    if password[0] == get_password:
        return redirect('/query/')
    else:
        return redirect('/wrong/1')

@app.route('/query/', methods=['GET', 'POST'])
def question():
    return render_template('query.html')

if __name__ == '__main__':
    app.run()
