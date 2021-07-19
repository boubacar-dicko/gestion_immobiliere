from flask import render_template, session, redirect, url_for 
from . import customer

@customer.route('/customer', methods=['GET']) 
def accueil():
    return render_template('customer/customerviews/accueil.html')