import os
import sys
from sqlalchemy.exc import SQLAlchemyError
sys.path.append(os.getcwd() + '/..')
from Example.app import db

class User(db.Model):
	__table_args__ = {'extend_existing' : True}
	__tablename__ = "User1"
	id = db.Column(db.Integer(), primary_key=True)
	user_name = db.Column(db.String(255))
	user_email = db.Column(db.String(255))
	status = db.Column(db.String(255))
	def __repr__(self):
		return "fUser('{self.id}','{self.user_name}', '{self.user_email}', '{self.status}')"
