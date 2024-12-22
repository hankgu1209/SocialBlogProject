# puppycompanyblog/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManger, LoginManager

app = Flask(__name__)

############################
### DATABASE SETUP ##########
########################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#########################
# LOGIN CONFIGS
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

##################################################
# 注册蓝图
##################################################

from puppycompanyblog.core.views import core
from puppycompnayblog.error_pages.handler import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)