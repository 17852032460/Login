#encoding: utf-8

from flask import Flask, url_for, redirect
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    print url_for('article', id = 123)
    return 'Hello World!'

@app.route('/article/<id>')
def article(id):
    return id

if __name__ == '__main__':
    app.run()
