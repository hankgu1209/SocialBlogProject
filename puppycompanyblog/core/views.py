# core/views.py
from flask import render_template,Blueprint

core = Blueprint("core",__name__,template_folder="templates")

@core.route("/")
def index():
    # more to come
    return render_template("index.html")

@core.route('/info')
def info():
    return render_template('info.html')