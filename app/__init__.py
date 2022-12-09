from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf import RecaptchaField
myapp_obj = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj.config.update(
    SECRET_KEY = 'bR|?*8]kfxvQ[K+1Bfq6',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    RECAPTCHA_PUBLIC_KEY = "6LcX0lojAAAAAJZaSKR5fW7EKqLd3RVucXyjfHDb",
    RECAPTCHA_PRIVATE_KEY = "6LcX0lojAAAAAPdliFCn65oPpYJ2S9jwXHq5IPM-",
)

db = SQLAlchemy(myapp_obj)

migrate = Migrate(myapp_obj, db)

login = LoginManager(myapp_obj)

login.login_view = 'login'

from app import routes, models