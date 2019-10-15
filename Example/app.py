from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from User.models import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import psycopg2


Base = declarative_base()

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:pineapple@123@localhost:15432/postgres'

db = SQLAlchemy()
db.init_app(app)
create_database = 'create database Example;'
use_database = 'use Example;'
create_table = 'create table IF NOT EXISTS User1(id integer PRIMARY KEY,name varchar(32) NOT NULL,email varchar(32) NOT NULL,status varchar(32) NOT NULL)'
insert_record = 'insert into User1(id, name, email, status) VALUES(%s,%s,%s,%s)'
# if(cur.rowcount()):
# 	print("Exists!")
# else:
# 	db.create_all()
conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' port=5432 password='einfochips'")
cur=conn.cursor()
	
@app.route('/',methods=["GET","POST"])
def home():
	
	return render_template('home.html',data="Hello World!!")
	

@app.route('/data',methods=["GET","POST"])
def index():

	print("index")

	if(request.method == "POST"):
		id = request.form['id']
		name= request.form['name']
		email = request.form['email']
		status = request.form['status']
		user = User(id=id,user_name=name,user_email=email,status=status)
		record_to_insert = (id, name, email, status)
		#cur.execute(use_database)
		cur.execute(create_table)
		cur.execute(insert_record,record_to_insert)
		#db.session.add(user)
		conn.commit()
		#db.session.close()
	return render_template('index.html')

@app.route('/fetch/<int:id>')
def get(id):
	#id1 = request.args['id']
	#print(id1)
	#id1=[2]
	fetch = 'select * from user1 where id= %s ;'
	cur.execute(fetch,(id,))
	result = cur.fetchall()
	#print(result)
	# name = result[0]
	# email = result[1]
	# status = result[2]
	#return render_template('fetch.html',Name=name,Email = email,status = status)
	return render_template('fetch.html',data=result)

@app.route('/fetchall')
def all():
	#id1 = request.args['id']
	#print(id1)
	#id1=[2]
	fetch = 'select * from user1;'
	cur.execute(fetch)
	result = cur.fetchall()
	#print(result)
	# name = result[0]
	# email = result[1]
	# status = result[2]
	#return render_template('fetch.html',Name=name,Email = email,status = status)
	return render_template('fetch.html',data=result)
@app.route('/delete/<int:id>')
def delete(id):
	#id1 = request.args['id']
	#print(id1)
	#id1=[2]
	fetch = 'delete from user1 where id= %s ;'
	cur.execute(fetch,(id,))
	result = cur.fetchall()
	#print(result)
	# name = result[0]
	# email = result[1]
	# status = result[2]
	#return render_template('fetch.html',Name=name,Email = email,status = status)
	return render_template('fetch.html',data=result)

if __name__ == '__main__':
	#app = create_app("config")
	app.run()
	cur.execute(create_database)

	

	
