from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from data import Articles
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
import datetime
Articles = Articles()

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'
app.debug= True
ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:database@localhost/flask_db'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# init
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200), unique=True)
    email = db.Column(db.String(200), unique=True)
    username = db.Column(db.String(200), unique=True)
    passwort = db.Column(db.String(200))
    registerDate= db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self,name,email,username, passwort):
        self.name= name
        self.email = email
        self.username = username
        self.passwort = passwort
   


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/articles")
def articles():
    return render_template('articles.html', articles = Articles)


@app.route("/article/<string:title>/")
def article(title):
    return render_template('article.html', title = title)





def article(title):
    return render_template('article.html', title = title) 

if __name__ == '__main__':
    app.debug = True
  
