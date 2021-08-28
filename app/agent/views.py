from flask import render_template, session, redirect, url_for, flash, request
from . import agent
from .forms import  BienForm
from flask_login import login_required, login_user, logout_user, current_user
from ..models import  Bien
from .. import db  

@agent.route('/agent', methods=['GET']) 
@login_required
def accueil():
    return render_template('agent/agentviews/accueil.html')



@agent.route('/addBien', methods=['GET', 'POST']) 
@login_required
def addBien():
    form = BienForm()
    
    if form.validate_on_submit():
        bien = Bien(name=form.name.data, typeBien=form.typeBien.data, adresseBien=form.adresseBien.data, descriptionBien=form.descriptionBien.data, firstname=form.firstname.data, lastname=form.lastname.data, adresse=form.adresse.data, email=form.email.data, telephone=form.telephone.data, user_id=current_user.id)
        db.session.add(bien)
        db.session.commit()
        flash('Bien enregistré avec succés!!!')
        return redirect(url_for('agent.listBien'))
    return render_template('agent/agentviews/addBien.html', form=form)


@agent.route('/listBien', methods=['GET', 'POST'])
@login_required
def listBien():
    all_bien = Bien.query.all()
 
    return render_template("/agent/agentviews/listBien.html", bien = all_bien)

@agent.route('/deleteBien/<id>/', methods = ['GET', 'POST'])
@login_required
def deleteBien(id):
    my_data = Bien.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")
 
    return redirect(url_for('agent.listBien'))


@agent.route('/updateBien/<int:id>/', methods = ['GET', 'POST'])
@login_required
def updateBien(id):
    all_bien = Bien.query.get(id)
    if request.method == 'POST':
        my_data = Bien.query.get(request.form.get('id'))
 
        my_data.name = request.form['name']
        my_data.typeBien = request.form['typeBien']
        my_data.adresseBien = request.form['adresseBien']
        my_data.descriptionBien = request.form['descriptionBien']
        my_data.firstname = request.form['firstname']
        my_data.lastname = request.form['lastname']
        my_data.adresse = request.form['adresse']
        my_data.email = request.form['email']
        my_data.telephone = request.form['telephone']
 
        db.session.commit()
        flash("Employee Updated Successfully")
 
        return redirect(url_for('agent.listBien'))
    return render_template("/agent/agentviews/updateBien.html", bien = all_bien)


@agent.route('/showBien/<int:id>/', methods = ['GET', 'POST'])
@login_required
def showBien(id):
    show_bien = Bien.query.get(id)

    return render_template("/agent/agentviews/showBien.html", bien = show_bien)