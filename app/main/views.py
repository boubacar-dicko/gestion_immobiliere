from flask import render_template, session, redirect, url_for, flash, request
from . import main
from flask_login import login_required, login_user, logout_user, current_user
from .forms import LoginForm, RegistrationForm
from ..models import User
from .. import db     

@main.route('/accueil', methods=['GET'])
@login_required
def accueil():
    auth=False
    return render_template('main/mainviews/accueil.html', auth=auth)

@main.route('/', methods=['GET','POST']) 
def login():
    if current_user.is_authenticated:
        return render_template('main/mainviews/accueil.html')
    else: 
        fl = LoginForm()
        if fl.validate_on_submit():
            user = User.query.filter_by(email=fl.email.data).first()
            if user is not None and user.verify_password(fl.password.data):
                login_user(user, fl.remember_me.data) 
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('main.accueil') 
                return redirect(next)
            flash('Invalid username or password.')
        return render_template('main/users_management/login.html',form=fl)
 
     
    

@main.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('Déconnexion réussie.') 
    return redirect(url_for('main.login'))

@main.route('/register', methods=['GET', 'POST']) 
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Inscription réussie. Veuillez vous authentifier à présent.')
        return redirect(url_for('main.login'))
    return render_template('main/users_management/register.html', form=form)