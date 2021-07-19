from flask import render_template, session, redirect, url_for 
from . import agent

@agent.route('/agent', methods=['GET']) 
def accueil():
    return render_template('agent/agentviews/accueil.html')