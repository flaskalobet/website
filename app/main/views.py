from . import main
from app import models
from forms import LoginForm
from flask import current_app, request, render_template
from flask.ext.login import login_user, logout_user

@main.route('/')
def index():
    current_app.logger.info('Main function index and from IP: %s', request.remote_addr)
    return '<h1>hello</h1>'

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return '<h1>Login Successfull</h1>'
    return render_template('login.html', form=form)
