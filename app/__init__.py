#!/usr/bin/env python3
"""Module"""

from flask import Flask
from flask_login import LoginManager
from .db import db
from .models.user import User
from .models.csv_file import CSVFile
from .models.csv_data import CSVData



# initialize flask
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'qwerty'
app.config['SQLALCHEMY_DATABASE_URI'] =\
  'mysql+mysqlconnector://analyst:project@localhost/user_data'


login_manager = LoginManager()
login_manager.logi_view = 'auth.login'
login_manager.init_app(app)

db.init_app(app)

# Creates all tables in the database if not present
with app.app_context():
  db.create_all()

@login_manager.user_loader
def load_user(user_id):
  """
  Callback used to reload the user object
  from the user ID stored in the session
  """
  return User.query.get(int(user_id))


# blueprint for auth routes in our app
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth routes in our app
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
