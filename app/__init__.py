from flask import Flask # grab flask class to use for our object
import os # import for database
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

myapp_obj = Flask(__name__) # create instance of flask class object

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj.config.update(
    SECRET_KEY = 'bR|?*8]kfxvQ[K+1Bfq6',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy(myapp_obj)

login = LoginManager(myapp_obj)

login.login_view = 'login'

from app import routes, models # makes init be able to see our routes