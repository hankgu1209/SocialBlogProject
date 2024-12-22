from flask import Flask

app = Flask(__name__)

# 注册蓝图
from puppycompanyblog.core.views import core
app.register_blueprint(core)