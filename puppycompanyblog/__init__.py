from flask import Flask

app = Flask(__name__)

# 注册蓝图
from puppycompanyblog.core.views import core
from puppycompnayblog.error_pages.handler import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)