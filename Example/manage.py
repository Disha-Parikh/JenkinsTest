import sys
import os
sys.path.append(os.getcwd() + '/..')

from app import db
from Example.User.model import *

db.create_all()
db.session.commit()