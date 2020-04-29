from flask import Flask,render_template,request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db = SQLAlchemy()
db.init_app(app)

import sys
import os
sys.path.append(os.getcwd() + '/Example/User')
from models import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

Base = declarative_base()
create_database = 'create database Example;'
use_database = 'use Example;'
create_table = 'create table IF NOT EXISTS User1(id integer PRIMARY KEY,name varchar(32) NOT NULL,email varchar(32) NOT NULL,status varchar(32) NOT NULL)'
insert_record = 'insert into User1(id, name, email, status) VALUES(%s,%s,%s,%s)'

conn = psycopg2.connect("dbname='postgres' user='postgres' host='postgres' port=5432 password='einfochips'")
cur=conn.cursor()
dirpath = os.getcwd()
print("PATH????? %s",dirpath)




@app.route('/',methods=["GET","POST"])
def home():
	return render_template('home.html',data="Hello World!version 2! from my laptop")


@app.route('/login',methods=["GET","POST"])
def login():

	if(request.method == "POST"):
		if(request.form['name']==request.form['password']):
			print("YAY")
			return redirect(url_for('index'))
	return render_template('login.html')


@app.route('/data',methods=["GET","POST"])
def index():
	if(request.method == "POST"):
		id = request.form['id']
		name= request.form['name']
		email = request.form['email']
		status = request.form['status']
		user = User(id=id,user_name=name,user_email=email,status=status)
		record_to_insert = (id, name, email, status)
		cur.execute(create_table)
		cur.execute(insert_record,record_to_insert)
		conn.commit()
	return render_template('index.html')

@app.route('/fetch/<int:id>')
def get(id):

	fetch = 'select * from user1 where id= %s ;'
	cur.execute(fetch,(id,))
	result = cur.fetchall()
	return render_template('fetch.html',data=result)

@app.route('/fetchall')
def all():
	fetch = 'select * from user1;'
	cur.execute(fetch)
	result = cur.fetchall()
	return render_template('fetch.html',data=result)
@app.route('/delete/<int:id>')
def delete(id):
	fetch = 'delete from user1 where id= %s ;'
	cur.execute(fetch,(id,))
	result = cur.fetchall()

	return render_template('fetch.html',data=result)

if __name__ == '__main__':
	h = os.system('curl http://169.254.169.254/latest/meta-data/public-ipv4')
	print("H")
	print(h)
	app.run(host=h,port=5002)

