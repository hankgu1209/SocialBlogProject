# users /views.py

from flask import render_template,url_for,flash, redirect,request,Blueprint
from flask_login import current_user,login_required,login_user,logout_user
from puppycompanyblog import db
from puppycompanyblog.models import User,BlogPost
from puppycompanyblog.users.forms import RegistrationForm,UpdateUserForm,LoginForm
from puppycompanyblog.users.picture_handler import add_profile_pic


users = Blueprint('users',__name__)

# register
@users.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('users.login'))
    return render_template('register.html',form=form)

# login
@users.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Login Success!')

            next = request.args.get('next')
            if next==None or not next.startswith('/'):
                next = url_for('core.index')
            return redirect(next)
    return render_template('login.html',form=form)

# logout
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.login'))

# account (update UserForm)
# user's list of Blog Posts
@users.route('/account',methods=['GET','POST'])
@login_required
def account():
    form = UpdateUserForm()
    if form.validate_on_submit():
        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.pic.data,username)
            current_user.profile_image = pic
            db.session.commit()

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User Account Updated!')
        return redirect(url_for('users.account'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for('static',filename='profile_pics/'+current_user.profile_image)
    return render_template('account.html',profile_image=profile_image,form=form)
