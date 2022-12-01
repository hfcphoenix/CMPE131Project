from flask import Flask # grab flask class to use for our object
import os # import for database

myapp_obj = Flask(__name__) # create instance of flask class object

basedir = os.path.abspath
myapp_obj.config.update(
    SECRET_KEY = 'bR|?*8]kfxvQ[K+1Bfq6'
)

from app import routes # makes init be able to see our routes