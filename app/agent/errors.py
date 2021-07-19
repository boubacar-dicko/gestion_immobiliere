from flask import render_template
from . import agent

@agent.app_errorhandler(404) 
def page_not_found(e):
    return render_template('agent/errors/404.html'), 404

@agent.app_errorhandler(500) 
def internal_server_error(e):
    return render_template('agent/errors/500.html'), 500